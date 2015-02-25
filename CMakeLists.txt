project                     (TARGet)
cmake_minimum_required      (VERSION 2.4)

# Find everything that's always required
find_package                (Boost REQUIRED COMPONENTS program_options python serialization signals)
set             			(cxx_flags                  ${CMAKE_CXX_FLAGS_RELEASE})
add_definitions             (${cxx_flags})

# Fix the XCode bug
add_definitions             (-ftemplate-depth=256)

# Set includes
include_directories         (${CMAKE_CURRENT_BINARY_DIR}
                             ${CMAKE_CURRENT_SOURCE_DIR}/include
                             ${Boost_INCLUDE_DIR}
                             ${cwd_INCLUDE_DIR})

# Process subdirectories
add_subdirectory            (bindings)
