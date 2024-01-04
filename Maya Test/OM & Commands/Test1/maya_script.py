import maya.standalone

# starting Maya Standalone mode
maya.standalone.initialize(name='python')

import maya.cmds as cmds
import maya.api.OpenMaya as om

# Creating a new scene
cmds.file(new=True, force=True)

# Creating a cube
cube = cmds.polyCube(width=2, height=2, depth=2)[0]

# Adding a custom boolean attribute "ShowDuplicate" to the cube
cmds.addAttr(cube, longName="showDuplicate", attributeType="bool", defaultValue=False, keyable=True)

# Setting the "ShowDuplicate" attribute to True (1)
cmds.setAttr(cube + ".showDuplicate", 1)

# Duplicating the cube using cmds.duplicate
duplicate_cube_name = cmds.duplicate(cube)[0]

# Converting the duplicate cube name to PyNode
duplicate_cube = om.MGlobal.getSelectionListByName(duplicate_cube_name).getDagPath(0).node()

# Parenting the duplicate cube under the original cube
cmds.parent(duplicate_cube_name, cube)

# Renaming the duplicate cube to "CubeB"
cmds.rename(duplicate_cube_name, "CubeB")

# Moving "CubeB" by 10 units on the X-axis
cmds.move(10, 0, 0, "CubeB", relative=True)

# Adding a custom boolean attribute "Duplicate" to "CubeB"
cmds.addAttr("CubeB", longName="Duplicate", attributeType="bool", defaultValue=False, keyable=True)

# Connecting "ShowDuplicate" attribute to drive the visibility of "CubeB"
cmds.connectAttr(cube + ".showDuplicate", "CubeB.visibility")

# Connecting "Duplicate" attribute to drive the visibility of "CubeB"
cmds.connectAttr(cube + ".showDuplicate", "CubeB.Duplicate")

# Querying the geometry of "CubeB"
vertices = cmds.polyInfo("CubeB", faceToVertex=True)[0].split(':')[1].split()
vertices = [int(v) for v in vertices]

# Deleting the top face of "CubeB"
cmds.select("CubeB.f[1]")
cmds.polyDelFacet()

# Saving the scene
scene_path = "d:/scene.ma"  # Provide the desired path here to save the maya file
cmds.file(rename=scene_path)
cmds.file(save=True, type="mayaAscii")

# Stopping Maya standalone mode
maya.standalone.uninitialize()
