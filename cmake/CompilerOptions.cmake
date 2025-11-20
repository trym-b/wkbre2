set(CMAKE_CXX_STANDARD 17)

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")
elseif("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
else()
    # message(FATAL_ERROR "TEST: ${CMAKE_CXX_COMPILER}")
    message(WARNING "Unknown compiler, not able to set compiler options for '${CMAKE_CXX_COMPILER_ID}'")
endif()