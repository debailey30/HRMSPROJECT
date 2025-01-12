cmake_minimum_required(VERSION 3.14)

# Define the project
project(HRMSProject VERSION 1.0 LANGUAGES CXX)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set the path to your Qt installation
set(CMAKE_PREFIX_PATH "C:/Qt/6.8.1/msvc2022_64")

# Enable debug output for finding packages
set(QT_DEBUG_FIND_PACKAGE ON)

# Find the required Qt packages
find_package(Qt6 6.8.1 REQUIRED COMPONENTS Widgets Gui Core Quick)

# Include the Qt modules
include_directories(${Qt6Widgets_INCLUDE_DIRS})
include_directories(${Qt6Gui_INCLUDE_DIRS})
include_directories(${Qt6Core_INCLUDE_DIRS})
include_directories(${Qt6Quick_INCLUDE_DIRS})

# Include the directory where the generated UI header files are located
include_directories(${CMAKE_BINARY_DIR})

# Set the MySQL directory
set(MySQL_INCLUDE_DIR "C:/Program Files/MySQL/MySQL Server 8.0/include")
set(MySQL_LIBRARY "C:/Program Files/MySQL/MySQL Server 8.0/lib/libmysql.lib")

# Include directories for MySQL
include_directories(${MySQL_INCLUDE_DIR})

# Add your source files
set(SOURCES
    src/main.cpp
    src/MainWindow.cpp
    src/LoginDialog.cpp
)

# Add the header files
set(HEADERS
    src/MainWindow.h
    src/LoginDialog.h
    src/UserRoles.h
)

# Add the UI files
set(UIS
    src/MainWindow.ui
    src/LoginDialog.ui
)

# Generate MOC files
qt6_wrap_cpp(MOC_SOURCES ${HEADERS})

# Generate UI files
qt6_wrap_ui(UI_HEADERS ${UIS})

# Add the executable
add_executable(HRMSProject ${SOURCES} ${MOC_SOURCES} ${UI_HEADERS})

# Link the Qt6 libraries
target_link_libraries(HRMSProject Qt6::Widgets ${MySQL_LIBRARY})