# CMakeList.txt : projet CMake pour wkbre2, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory ("imgui")

find_package (BZip2 REQUIRED)
find_package (SDL2 CONFIG REQUIRED)
find_package (nlohmann_json CONFIG REQUIRED)
find_package(OpenAL CONFIG REQUIRED)
find_package(mpg123 CONFIG REQUIRED)
find_package(glew CONFIG REQUIRED)
find_package(sol2 CONFIG REQUIRED)
find_package(Lua REQUIRED)

# Find enet
find_path(ENET_INCLUDE_DIR enet/enet.h)
find_library(ENET_LIBRARY enet)
message(${ENET_LIBRARY})
message(${ENET_INCLUDE_DIR})

# Find Discord-RPC
option(USE_DISCORD "Enables the most useless feature of all time. Setting it up and using it will waste tons of time. Not recommended if you want to keep your precious time." OFF)
if(${USE_DISCORD})
  find_path(DISCORDRPC_INCLUDE_DIR discord_rpc.h)
  find_library(DISCORDRPC_LIBRARY discord-rpc)
  add_compile_definitions(HAS_DISCORD)
endif()

# Ajoutez une source à l'exécutable de ce projet.
add_executable (wkbre2
  "AIController.cpp"
  "AIController.h"
  "anim.cpp"
  "anim.h"
  "BreakpointManager.cpp"
  "BreakpointManager.h"
  "Camera.cpp"
  "Camera.h"
  "client.cpp"
  "client.h"
  "common.cpp"
  "common.h"
  "file.cpp"
  "file.h"
  "FormationController.cpp"
  "FormationController.h"
  "GameObjectRef.h"
  "gameset/3DClip.cpp"
  "gameset/3DClip.h"
  "gameset/actions.cpp"
  "gameset/actions.h"
  "gameset/ArmyCreationSchedule.cpp"
  "gameset/ArmyCreationSchedule.h"
  "gameset/cameraPath.cpp"
  "gameset/cameraPath.h"
  "gameset/command.cpp"
  "gameset/command.h"
  "gameset/Commission.cpp"
  "gameset/Commission.h"
  "gameset/CommonEval.h"
  "gameset/condition.cpp"
  "gameset/condition.h"
  "gameset/finder.cpp"
  "gameset/finder.h"
  "gameset/Footprint.cpp"
  "gameset/Footprint.h"
  "gameset/GameObjBlueprint.cpp"
  "gameset/GameObjBlueprint.h"
  "gameset/gameset.cpp"
  "gameset/gameset.h"
  "gameset/GameTextWindow.cpp"
  "gameset/GameTextWindow.h"
  "gameset/GSTerrain.cpp"
  "gameset/GSTerrain.h"
  "gameset/ObjectCreation.cpp"
  "gameset/ObjectCreation.h"
  "gameset/OrderBlueprint.cpp"
  "gameset/OrderBlueprint.h"
  "gameset/Package.cpp"
  "gameset/Package.h"
  "gameset/Plan.cpp"
  "gameset/Plan.h"
  "gameset/position.cpp"
  "gameset/position.h"
  "gameset/reaction.cpp"
  "gameset/reaction.h"
  "gameset/ScriptContext.cpp"
  "gameset/ScriptContext.h"
  "gameset/Sound.cpp"
  "gameset/Sound.h"
  "gameset/values.cpp"
  "gameset/values.h"
  "gameset/WorkOrder.cpp"
  "gameset/WorkOrder.h"
  "gfx/bitmap.cpp"
  "gfx/bitmap.h"
  "gfx/D3D11EnhancedSceneRenderer.cpp"
  "gfx/D3D11EnhancedSceneRenderer.h"
  "gfx/D3D11EnhancedTerrainRenderer.cpp"
  "gfx/D3D11EnhancedTerrainRenderer.h"
  "gfx/DefaultParticleRenderer.cpp"
  "gfx/DefaultParticleRenderer.h"
  "gfx/DefaultSceneRenderer.cpp"
  "gfx/DefaultSceneRenderer.h"
  "gfx/DefaultTerrainRenderer.cpp"
  "gfx/DefaultTerrainRenderer.h"
  "gfx/ParticleRenderer.h"
  "gfx/renderer_d3d11.cpp"
  "gfx/renderer_d3d11.h"
  "gfx/renderer_d3d9.cpp"
  "gfx/renderer_ogl3.cpp"
  "gfx/renderer.cpp"
  "gfx/renderer.h"
  "gfx/SceneRenderer.h"
  "gfx/TerrainRenderer.h"
  "gfx/TextureCache.cpp"
  "gfx/TextureCache.h"
  "imguiimpl.cpp"
  "imguiimpl.h"
  "interface/ClientDebugger.cpp"
  "interface/ClientDebugger.h"
  "interface/ClientInterface.cpp"
  "interface/ClientInterface.h"
  "interface/GameSetDebugger.cpp"
  "interface/GameSetDebugger.h"
  "interface/QuickSkirmishMenu.cpp"
  "interface/QuickSkirmishMenu.h"
  "interface/QuickStartMenu.cpp"
  "interface/QuickStartMenu.h"
  "interface/ServerDebugger.cpp"
  "interface/ServerDebugger.h"
  "Language.cpp"
  "Language.h"
  "lzrw_headers.h"
  "lzrw3.c"
  "mesh.cpp"
  "mesh.h"
  "Model.cpp"
  "Model.h"
  "Movement.cpp"
  "Movement.h"
  "MovementController.cpp"
  "MovementController.h"
  "netenetlink.cpp"
  "netenetlink.h"
  "network.cpp"
  "network.h"
  "NNSearch.cpp"
  "NNSearch.h"
  "Order.cpp"
  "Order.h"
  "ParticleContainer.cpp"
  "ParticleContainer.h"
  "ParticleSystem.cpp"
  "ParticleSystem.h"
  "Pathfinding.h"
  "platform.cpp"
  "resources.rc"
  "scene.cpp"
  "scene.h"
  "server.cpp"
  "server.h"
  "settings.cpp"
  "settings.h"
  "SoundPlayer.cpp"
  "SoundPlayer.h"
  "StampdownPlan.cpp"
  "StampdownPlan.h"
  "tags.cpp"
  "tags.h"
  "terrain.cpp"
  "terrain.h"
  "test.cpp"
  "TimeManager.cpp"
  "TimeManager.h"
  "Trajectory.cpp"
  "Trajectory.h"
  "TrnTextureDb.cpp"
  "TrnTextureDb.h"
  "util/DynArray.h"
  "util/GSFileParser.cpp"
  "util/GSFileParser.h"
  "util/IndexedStringList.h"
  "util/TagDict.h"
  "util/util.cpp"
  "util/util.h"
  "util/vecmat.cpp"
  "util/vecmat.h"
  "WavDocument.cpp"
  "WavDocument.h"
  "window.cpp"
  "window.h"
  "wkbre2.cpp"
  "wkbre2.h"
)
target_link_libraries (wkbre2
  imgui
  SDL2::SDL2
  ${ENET_LIBRARY}
  BZip2::BZip2
  nlohmann_json::nlohmann_json
  OpenAL::OpenAL
  MPG123::libmpg123
  $<$<BOOL:${USE_DISCORD}>:${DISCORDRPC_LIBRARY}>
  GLEW::GLEW
  sol2::sol2
  ${LUA_LIBRARIES}
  $<$<PLATFORM_ID:Windows>:
    d3d9
    ws2_32
    winmm
    d3d11
    d3dcompiler
    opengl32
    dxgi
  >
)
target_include_directories(wkbre2
  PRIVATE
  ${ENET_INCLUDE_DIR}
  $<$<BOOL:${USE_DISCORD}>:${DISCORDRPC_INCLUDE_DIR}>
  ${LUA_INCLUDE_DIR}
)

# TODO: Ajoutez des tests et installez des cibles si nécessaire.
