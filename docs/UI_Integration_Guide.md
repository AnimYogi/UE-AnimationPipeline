# yTools UI Integration Guide

This document outlines the Blueprint logic required to connect the Editor Utility Widget (`EUW_yToolsLauncher`) to the Python pipeline.

## UI Elements Required
1. **Editable Text (TextBox):** Named `Input_AnimName`. This is where the user types the animation name.
2. **Button:** Named `Btn_Generate`.

## Blueprint Logic (OnClicked Event)
When the user clicks `Btn_Generate`, the Blueprint must fire an **Execute Python Command** node.

To pass the text from the UI into the Python script dynamically, we use Unreal's string formatting in Blueprint before passing it to Python. The raw Python command string should look like this:

```python
import yTools.AnimationPipeline
yTools.AnimationPipeline.generate_level_setup('{}')