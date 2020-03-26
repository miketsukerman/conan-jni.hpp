#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "java_installer/9.0.0@bincrafters/stable"

    def configure_cmake(self):
        cmake = CMake(self)
        if self.settings.compiler == "gcc" and \
            float(self.settings.compiler.version.value) <= 7:
                cmake.definitions["CMAKE_CXX_FLAGS"] = "-fPIC"
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("lib")
            self.run("LD_LIBRARY_PATH='{}' java -jar test.jar".format(os.curdir), run_environment=True)        