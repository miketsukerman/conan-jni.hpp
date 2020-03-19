project(test_package)
cmake_minimum_required(VERSION 2.8.11)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Java COMPONENTS Development Runtime REQUIRED)
find_package(JNI REQUIRED)
include(UseJava)

add_library(${PROJECT_NAME} SHARED test.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC ${JNI_LIBRARIES})

add_jar(test_package_jar 
        SOURCES NativePeer.java 
        OUTPUT_NAME test 
        OUTPUT_DIR ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}
        ENTRY_POINT jni/test/NativePeer)
add_dependencies(test_package_jar test_package)

