import subprocess
import os


# Define the path to the CMake executable
cmake_executable = r'C:\Program Files\CMake\bin\cmake.exe'

# Define the path to the CMakeLists.txt file
cmake_file_path = r"C:\Users\USER\OneDrive - ort braude college of engineering\Desktop\MyProject_1\CMakeLists.txt"

# Define the build directory
build_directory = r'C:\Users\USER\OneDrive - ort braude college of engineering\Desktop\MyProject_1\build'

# Run the CMake command to generate the build files
# cmake_command = [cmake_executable, cmake_file_path, '-B', build_directory]
cmake_command = [cmake_executable, cmake_file_path, '-B', build_directory]
subprocess.run(cmake_command, check=True)

# Change the current working directory to the build directory
os.chdir(build_directory)

# Run the build command (e.g., make)
build_command = ['make']
subprocess.run(build_command, check=True)
