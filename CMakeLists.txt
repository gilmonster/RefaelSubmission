cmake_minimum_required(VERSION 3.0)

project(Encripter)

add_subdirectory(package)

add_custom_target(Package ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_CURRENT_SOURCE_DIR}/package ${CMAKE_CURRENT_BINARY_DIR}/package
    COMMENT "Copying Python package files"
)

# add_dependencies(MyExecutable Package)

find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Set the source files for your Python project
set(SOURCES
    Encripter.py
    # Add more source files if necessary
)


# Create a target for your Python project
add_executable(MyExecutable main.cpp)

# Link against the Python libraries
target_link_libraries(MyExecutable PRIVATE Python::Python)

# Set the C++ compiler for building the CMake wheel
set(CMAKE_CXX_COMPILER "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx86/x86/cl.exe")

# Build the CMake Python wheel
add_custom_target(
    BuildCMakeWheel
    COMMAND mkvirtualenv build-cmake
    COMMAND pip install -r requirements-dev.txt
    COMMAND python setup.py bdist_wheel -- -DBUILD_CMAKE_FROM_SOURCE:BOOL=ON
        -DCMakePythonDistributions_ARCHIVE_DOWNLOAD_DIR:PATH=C:\\Users\\USER\\OneDrive - ort braude college of engineering\\Desktop\\MyProject_1\\cmake_cache
        -DCMakeProject_BINARY_DIR:PATH=C:\\Users\\USER\\OneDrive - ort braude college of engineering\\Desktop\\MyProject_1\\standalone-build
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Building the CMake Python wheel"
)

# Add the BuildCMakeWheel target to the default build target
add_dependencies(MyExecutable BuildCMakeWheel)




# cmake_minimum_required(VERSION 3.0)

# project(Encripter)

# add_subdirectory(package)

# add_custom_target(MyPackage ALL
    # COMMAND ${CMAKE_COMMAND} -E copy_directory
        # ${CMAKE_CURRENT_SOURCE_DIR}/package ${CMAKE_CURRENT_BINARY_DIR}/my_package
    # COMMENT "Copying Python package files"
# )

# add_dependencies(MyExecutable Package)



# find_package(Python REQUIRED COMPONENTS Interpreter Development)

# # Set the source files for your Python project
# set(SOURCES
    # Encripter.py
    # # Add more source files if necessary
# )

# # Create a target for your Python project
# add_executable(MyExecutable main.cpp)

# # Link against the Python libraries
# target_link_libraries(MyEncripter PRIVATE Python::Python)

# # Set the C++ compiler for building the CMake wheel
# set(CMAKE_CXX_COMPILER "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.29.30133\\bin\\Hostx86\\x86\\cl.exe")

# # Build the CMake Python wheel
# add_custom_target(
    # BuildCMakeWheel
    # COMMAND mkvirtualenv build-cmake
    # COMMAND pip install -r requirements-dev.txt
    # COMMAND python setup.py bdist_wheel -- -DBUILD_CMAKE_FROM_SOURCE:BOOL=ON
        # -DCMakePythonDistributions_ARCHIVE_DOWNLOAD_DIR:PATH=C:\\Users\\USER\\OneDrive - ort braude college of engineering\\Desktop\\MyProject_1\\cmake_cache
        # -DCMakeProject_BINARY_DIR:PATH=C:\\Users\\USER\\OneDrive - ort braude college of engineering\\Desktop\\MyProject_1\\standalone-build
    # WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    # COMMENT "Building the CMake Python wheel"
# )

# # Add the BuildCMakeWheel target to the default build target
# add_dependencies(MyEncripter BuildCMakeWheel)
