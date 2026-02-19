# -----------------------------------------------------------------------------
# Tool: yTools | Animation Pipeline
# Version: 1.2
# Author: Yogesh Batra (AnimYogi)
# GitHub: https://github.com/AnimYogi/UE-AnimationPipeline
# Description: Professional-grade automation for UE animation environments.
# -----------------------------------------------------------------------------

import unreal

def generate_level_setup(anim_name):
    try:
        # 1. Clean the input name
        clean_name = str(anim_name).replace("{", "").replace("}", "").strip()
        if not clean_name:
            unreal.log_warning("yTools: Name was empty.")
            return

        root_path = f"/Game/Animations/{clean_name}"
        level_name = f"L_{clean_name}_Master"
        
        # 2. Create the Directory (Safe)
        if not unreal.EditorAssetLibrary.does_directory_exist(root_path):
            unreal.EditorAssetLibrary.make_directory(root_path)

        # 3. Create the Level Asset (But DON'T load it yet)
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        full_level_path = f"{root_path}/{level_name}"
        
        if not unreal.EditorAssetLibrary.does_asset_exist(full_level_path):
            asset_tools.create_asset(level_name, root_path, unreal.World, unreal.WorldFactory())
            unreal.log(f"yTools: Created level asset at {full_level_path}")

        # 4. Spawn Cameras in the CURRENT world (Safe)
        # Instead of switching levels, we'll set up the current scene
        # You can manually open the new level after the script finishes
        cam_3p = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector(-500, 0, 150))
        if cam_3p:
            cam_3p.set_actor_label(f"Cam_{clean_name}_3P")
            
        cam_1p = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector(0, 0, 160))
        if cam_1p:
            cam_1p.set_actor_label(f"Cam_{clean_name}_1P")

        unreal.log(f"yTools: Folders, Level Asset, and Cameras created for '{clean_name}'!")

    except Exception as e:
        unreal.log_error(f"yTools Python Error: {str(e)}")