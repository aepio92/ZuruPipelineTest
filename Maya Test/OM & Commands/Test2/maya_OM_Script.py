import maya.OpenMaya as om


def modify_selected_object():
    selection = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selection)  # storing the selected objects in the scene

    # getting & storing the DAG path of the first selected object
    dag_path = om.MDagPath()
    selection.getDagPath(0, dag_path)

    transform_fn = om.MFnTransform(dag_path)  # This function set allows manipulation of transformation attributes

    translation = transform_fn.translation(om.MSpace.kTransform)  # storing the current translation

    new_translation = om.MVector(translation.x + 2.0, translation.y + 2.0, translation.z)  # creating a new translation vector
    transform_fn.setTranslation(new_translation, om.MSpace.kTransform)  # setting the new translation

    mesh_fn = om.MFnMesh(dag_path)  # creating new function set to manipulate the geometry

    # getting the vertices of the indexed face and storing it into an array.
    face_id = 0
    vertices = om.MIntArray()
    mesh_fn.getPolygonVertices(face_id, vertices)

    translation_vector = om.MVector(0.0, 0.0, 4.0)  # creating a new translation vector

    # adding the new translation to all the vertices
    for vertex_id in vertices:
        current_position = om.MPoint()
        mesh_fn.getPoint(vertex_id, current_position, om.MSpace.kWorld)
        new_position = current_position + translation_vector
        mesh_fn.setPoint(vertex_id, new_position, om.MSpace.kWorld)


# Executing Modification
modify_selected_object()
