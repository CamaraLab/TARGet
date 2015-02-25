find_package                (PythonLibs)
link_libraries              (${PYTHON_LIBRARIES})
include_directories         (${PYTHON_INCLUDE_PATH})
link_libraries              (${Boost_PYTHON_LIBRARY})

# currently can't build bindings with counters support, eventually FIXME
set                         (sources
                                                dionysus.cpp 
                                                filtration.cpp
                                                chain.cpp
                                                static-persistence.cpp
                                                dynamic-persistence.cpp
                                                persistence-diagram.cpp
                                                simplex.cpp
                                                birthid.cpp
                                                rips.cpp
                                                distances.cpp
                            )
set                         (bindings_libraries ${libraries})

add_library                 (_dionysus SHARED   ${sources})
target_link_libraries       (_dionysus          ${libraries})


# Python files and the symlink
add_custom_target           (dionysus ALL
                             ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR}/dionysus ${CMAKE_CURRENT_BINARY_DIR}/dionysus
                             DEPENDS            dionysus/__init__.py
                                                dionysus/distances.py
                            )

get_target_property         (_dionysus_location _dionysus LOCATION)
add_custom_target           (dionysus-link ALL 
                             ${CMAKE_COMMAND} -E create_symlink ${_dionysus_location} ${CMAKE_CURRENT_BINARY_DIR}/dionysus/_dionysus.so
                             DEPENDS _dionysus)
