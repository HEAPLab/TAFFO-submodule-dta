
add_llvm_library(TaffoDTA OBJECT BUILDTREE_ONLY
  TaffoDTA.cpp
  Optimizer.cpp
  Model.cpp
  OptimizerBinaryInstructions.cpp
  OptimizerInstructionHandling.cpp
  OptimizerConstantsHandling.cpp
  PhiWatcher.cpp
  CPUCosts.cpp
  MemWatcher.cpp
  LoopAnalyzerUtil.cpp
  MetricPerf.cpp
  MetricBase.cpp
  MetricPerfInstruction.cpp
  ADDITIONAL_HEADERS
  MetricBase.h
  MetricBaseForward.h
  TaffoDTA.h
  Optimizer.h
  Infos.h
  OptimizerInfo.h
  Model.h
  DTAConfig.h
  MemSSAUtils.hpp
  CPUCosts.h
  LoopAnalyzerUtil.h
  )

set_property(TARGET obj.TaffoDTA PROPERTY POSITION_INDEPENDENT_CODE ON)
