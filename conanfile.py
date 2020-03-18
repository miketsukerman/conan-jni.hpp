#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class RapidjsonConan(ConanFile):
    name = "jni.hpp"
    version = "4.0.1"
    description = "jni.hpp is a modern, type-safe, header-only, C++14 wrapper for JNI (Java Native Interface)"
    homepage = "https://github.com/mapbox/jni.hpp"
    url = "https://github.com/mapbox/jni.hpp"
    author = "Michael Tsukerman <miketsukerman@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.txt"]
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/mapbox/jni.hpp"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="license.txt", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
