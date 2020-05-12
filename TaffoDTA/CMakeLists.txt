add_llvm_library(TaffoDTA MODULE
        TaffoDTA.cpp
        TaffoDTA.h
        Optimizer.h
        Optimizer.cpp
        Infos.h
        OptimizerInfo.h
        Model.cpp
        Model.h
        OptimizerBinaryInstructions.cpp
        OptimizerInstructionHandling.cpp

        PLUGIN_TOOL
        opt
        )

if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set_property(TARGET TaffoDTA APPEND_STRING PROPERTY
            LINK_FLAGS " -undefined dynamic_lookup")
endif ()

set_property(TARGET TaffoDTA PROPERTY CXX_STANDARD 11)
set_property(TARGET TaffoDTA PROPERTY CXX_STANDARD_REQUIRED ON)

target_link_libraries(TaffoDTA TaffoUtils)
