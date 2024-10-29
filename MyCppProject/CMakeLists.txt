cmake_minimum_required(VERSION 3.10)

project(MyCppProject VERSION 1.0.0 LANGUAGES CXX)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add your source files
add_executable(MyCppProject main.cpp)