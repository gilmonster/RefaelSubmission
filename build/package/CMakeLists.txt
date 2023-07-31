cmake_minimum_required(VERSION 3.0)

project(Package)

# Copy the Python source files to the output directory
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/Encripter.py
    DESTINATION ${CMAKE_CURRENT_BINARY_DIR}
)

# Set the output directory for the Python package files
set(OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/my_package")

# Create an empty __init__.py file in the output directory
file(WRITE ${OUTPUT_DIRECTORY}/__init__.py "")

# Install the Python package
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/Encripter.py
    DESTINATION my_package
)

# Optionally, install other files such as scripts or data files
# install(FILES my_script.py DESTINATION my_package)

# Optionally, define additional installation rules

# ...
