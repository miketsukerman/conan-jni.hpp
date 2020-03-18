project(test_package)
cmake_minimum_required(VERSION 2.8.11)

find_package(Java COMPONENTS Development Runtime REQUIRED)
find_package(JNI REQUIRED)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(${PROJECT_NAME} SHARED test.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC ${JNI_LIBRARIES})