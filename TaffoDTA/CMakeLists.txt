add_llvm_library(TaffoDTA OBJECT BUILDTREE_ONLY
  TaffoDTA.cpp

  ADDITIONAL_HEADERS
  TaffoDTA.h
)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  set_property(TARGET obj.TaffoDTA APPEND_STRING PROPERTY
    LINK_FLAGS " -undefined dynamic_lookup")
endif()

set_property(TARGET obj.TaffoDTA PROPERTY CXX_STANDARD 11)
set_property(TARGET obj.TaffoDTA PROPERTY CXX_STANDARD_REQUIRED ON)
set_property(TARGET obj.TaffoDTA PROPERTY POSITION_INDEPENDENT_CODE ON)
