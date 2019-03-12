add_llvm_loadable_module(TaffoAutotuner
    TaffoTunerPass.cpp
    TaffoTunerPass.h
  
  PLUGIN_TOOL
  opt
)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  set_property(TARGET TaffoAutotuner APPEND_STRING PROPERTY
    LINK_FLAGS " -undefined dynamic_lookup")
endif()

set_property(TARGET TaffoAutotuner PROPERTY CXX_STANDARD 11)
set_property(TARGET TaffoAutotuner PROPERTY CXX_STANDARD_REQUIRED ON)

target_link_libraries(TaffoAutotuner TaffoUtils)
