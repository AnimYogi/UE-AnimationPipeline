# Detailed Installation and Usage Guide

## Part 1: Installation & Setup
Before running the script, Unreal Engine needs to know how to read Python code and manipulate editor assets.

1. **Enable the Python Plugin:** Navigate to **Edit > Plugins**. Search for **Python Editor Script Plugin** and enable it. 
2. **Enable Editor Utilities:** In the same Plugins window, search for **Editor Scripting Utilities** and enable it.
3. **Restart Unreal:** Restart the engine when prompted.
4. **Prepare the Output Log:** Open the **Output Log**, click the bottom-left dropdown, and change it to **Cmd**.

## Part 2: How to Run the Script
1. In the **Cmd** input bar, type \py\ followed by the path to the script in quotes, and then the name of the animation.
2. **Example Command:**
   \py "C:\YourPath\yTools\AnimationPipeline.py" "Sword_Slash"\
3. Press **Enter**. 

## Part 3: What the Script Does (Under the Hood)
1. **Defines the Hierarchy:** Reads the argument you typed to format the asset names. Defaults to \Hammer_Melee\.
2. **Generates the Folder:** Creates \/Game/source/\ in your Content browser.
3. **Creates the Sub-Level:** Creates and opens the Sub-level (e.g., \L_Sword_Slash\).
4. **Generates the Sequence:** Creates a new Level Sequence asset. 
5. **Spawns and Links the Actor:** Spawns a Level Sequence Actor into the Sub-level and assigns the Level Sequence asset to it.
6. **Spawns Cameras:** Automatically spawns two Cine Camera Actors, naming them \Camera_FP\ (First Person) and \Camera_TP\ (Third Person) with predefined offset coordinates, and saves the Sub-level.
7. **Assembles the Master Level:** Generates the \L_Animation_Master\ level, streams the Sub-level into it, and saves.
