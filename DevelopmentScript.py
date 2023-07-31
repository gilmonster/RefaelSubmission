import subprocess
import os

# Define the path to the CMake executable
cmake_executable = r'C:\Program Files\CMake\bin\cmake.exe'

# Define the path to the CMakeLists.txt file
cmake_file_path = r"C:\Users\USER\OneDrive - ort braude college of engineering\Desktop\MyProject_1\CMakeLists.txt"

# Define the build directory (use absolute path)
build_directory = os.path.abspath('MyProject_1/build')

# Create the build directory if it doesn't exist
os.makedirs(build_directory, exist_ok=True)

# Run the CMake command to generate the build files
cmake_command = [cmake_executable, cmake_file_path, '-B', build_directory]
subprocess.run(cmake_command, check=True)

# Change the current working directory to the build directory
os.chdir(build_directory)

# Run the build command (use absolute path for 'make')
build_command = ['cmake', cmake_file_path]
subprocess.run(build_command, check=True)

#cmake [options] -S <path-to-source> -B <path-to-build>

#subprocess.run('make', 'Encripter', check=True)