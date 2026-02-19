# UE Animation Pipeline 🎬

An automated Unreal Engine Python script for technical animators. 

## Overview
This script provides a one-click automated setup for animation pipelines. It generates a Master Level, a Sub-level, a Level Sequence, and predefined Cine Camera setups (First & Third Person), automatically spawning and linking them together in your Content folder.

**Author:** Yogesh Batra ([AnimYogi](https://github.com/AnimYogi))
**Assistance:** Co-created with Google Gemini
**License:** MIT

## Requirements
* Unreal Engine (Tested on UE5+)
* **Python Editor Script Plugin** (Enabled in Edit > Plugins)
* **Editor Scripting Utilities Plugin** (Enabled in Edit > Plugins)

## Usage

1. Place AnimationPipeline.py in your desired directory.
2. Open Unreal Engine.
3. Open the **Output Log**, set the console dropdown to **Cmd**.
4. Run the script with the default name (Hammer_Melee) or pass a custom name as an argument.

**Example with custom name (Cmd console):**
\\\	ext
py "C:\YourPath\yTools\AnimationPipeline.py" "Sword_Slash"
\\\

## Features
* Auto-creates /Game/source directory.
* Auto-generates L_Animation_Master and custom-named Sub-levels.
* Auto-generates custom Level Sequences and links them to the Sub-level via a Level Sequence Actor.
* **[NEW]** Auto-spawns and positions First Person (Camera_FP) and Third Person (Camera_TP) Cine Camera Actors in the Sub-level.
* Auto-nests the Sub-level into the Master level using Dynamic Streaming.
