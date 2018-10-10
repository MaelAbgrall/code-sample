cmake_minimum_required(VERSION 3.0)

project("Project_name")

enable_testing()

find_package(OpenCV REQUIRED)

add_executable(
    output_name
    main.cpp
    #every .cpp file, but no .h
)

target_link_libraries()