import maya.OpenMaya as om
import maya.cmds as cmds


def move_selected_object():
    # Check if any object is selected
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("No objects selected. Please select an object.")
        return

    # Start an undo chunk
    om.MGlobal.executeCommand("undoInfo -openChunk")

    try:
        # Move selected object in X and Y by 2
        for obj in selected_objects:
            cmds.move(2, 2, 0, obj, relative=True, objectSpace=True)

        # Select the first face of the first selected object
        cmds.select(selected_objects[0] + '.f[0]', replace=True)

        # Move the selected face outwards in Z by 4
        cmds.move(0, 0, 4, relative=True, objectSpace=True)
    finally:
        # End the undo chunk
        om.MGlobal.executeCommand("undoInfo -closeChunk")


# Call the function to execute the actions
move_selected_object()
