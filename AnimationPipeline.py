# -----------------------------------------------------------------------------
# Tool: Unreal Engine Animation Pipeline Setup
# Author: Yogesh Batra (GitHub: AnimYogi)
# Assistance: Co-created with Google Gemini
# License: MIT
# Description: Automates the creation of Levels, Sequences, Cameras, Environment,
#              and automatically binds actors to the Sequencer.
# -----------------------------------------------------------------------------

import unreal
import sys

def generate_level_setup(animation_name):
    # --- 1. Define Names and Paths ---
    folder_path = "/Game/source"
    master_level_name = "L_Animation_Master"
    sub_level_name = f"L_{animation_name}"
    seq_name = f"LS_{animation_name}"
    
    master_level_path = f"{folder_path}/{master_level_name}"
    sub_level_path = f"{folder_path}/{sub_level_name}"
    
    # --- 2. Create the Source Directory ---
    unreal.EditorAssetLibrary.make_directory(folder_path)
    
    # --- 3. Create & Open the Sub-level First ---
    unreal.EditorLevelLibrary.new_level(sub_level_path)
    
    # --- 4. Create the Level Sequence Asset ---
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    seq_factory = unreal.LevelSequenceFactoryNew()
    
    seq_asset_path = f"{folder_path}/{seq_name}"
    if not unreal.EditorAssetLibrary.does_asset_exist(seq_asset_path):
        sequence_asset = asset_tools.create_asset(seq_name, folder_path, unreal.LevelSequence, seq_factory)
    else:
        sequence_asset = unreal.EditorAssetLibrary.load_asset(seq_asset_path)
        
    # --- 5. Spawn Sequence Actor ---
    seq_actor_class = unreal.LevelSequenceActor
    seq_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(seq_actor_class, unreal.Vector(0,0,0))
    
    if seq_actor and sequence_asset:
        seq_actor.set_sequence(sequence_asset)
        # [FEATURE 1] Rename the actor in the Outliner to match the sequence asset
        seq_actor.set_actor_label(seq_name)

    # --- 6. Spawn Cameras and Bind to Sequencer ---
    camera_class = unreal.CineCameraActor
    
    cam_fp = unreal.EditorLevelLibrary.spawn_actor_from_class(camera_class, unreal.Vector(0, 0, 160), unreal.Rotator(0, 0, 0))
    if cam_fp:
        cam_fp.set_actor_label("Camera_FP")
        # [FEATURE 2] Add First Person Camera to the Level Sequence automatically
        sequence_asset.add_possessable(cam_fp)
        
    cam_tp = unreal.EditorLevelLibrary.spawn_actor_from_class(camera_class, unreal.Vector(-250, 0, 160), unreal.Rotator(0, 0, 0))
    if cam_tp:
        cam_tp.set_actor_label("Camera_TP")
        # [FEATURE 2] Add Third Person Camera to the Level Sequence automatically
        sequence_asset.add_possessable(cam_tp)

    # --- 7. Spawn Environment (Lighting & Floor Plane) ---
    dir_light = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.DirectionalLight, unreal.Vector(0, 0, 1000), unreal.Rotator(0, -45, -45))
    if dir_light:
        dir_light.set_actor_label("DirectionalLight_Main")
        
    sky_light = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyLight, unreal.Vector(0, 0, 1000), unreal.Rotator(0, 0, 0))
    if sky_light:
        sky_light.set_actor_label("SkyLight_Main")
        
    plane_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))
    if plane_actor:
        plane_actor.set_actor_label("Floor_Plane")
        plane_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Plane.Plane")
        if plane_mesh:
            plane_actor.static_mesh_component.set_static_mesh(plane_mesh)
            plane_actor.set_actor_scale3d(unreal.Vector(10.0, 10.0, 1.0))
        
    # Save the Sub-level with all new actors inside
    unreal.EditorLevelLibrary.save_current_level()
    
    # --- 8. Create & Open the Master Level ---
    unreal.EditorLevelLibrary.new_level(master_level_path)
    editor_world = unreal.EditorLevelLibrary.get_editor_world()
    
    # --- 9. Add Sub-level to Master Level ---
    level_streaming_class = unreal.LevelStreamingDynamic
    unreal.EditorLevelUtils.add_level_to_world(editor_world, sub_level_path, level_streaming_class)
    
    unreal.EditorLevelLibrary.save_current_level()
    
    unreal.log(f"Success! {animation_name} Levels, Sequence, Bound Cameras, and Environment created successfully.")

# --- 10. Read Console Arguments ---
if __name__ == "__main__":
    anim_name_arg = "Hammer_Melee" 
    
    if len(sys.argv) > 1:
        anim_name_arg = sys.argv[1]
        
    generate_level_setup(anim_name_arg)