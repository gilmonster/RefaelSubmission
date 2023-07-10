cmake_minimum_required(VERSION 3.0)

project(Encripter)

find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Set the source files for your Python project
set(SOURCES
    Encripter.py
    # Add more source files if necessary
)

# Create a target for your Python project
add_executable(MyEncripter ${SOURCES})

# Link against the Python libraries
target_link_libraries(MyEncripter PRIVATE Python::Python Python::Module)

# Link against the random library
target_link_libraries(MyEncripter PRIVATE random)

