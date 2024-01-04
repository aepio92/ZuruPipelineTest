import maya.OpenMaya as om


def modify_selected_object():
    selection = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selection)

    dag_path = om.MDagPath()
    selection.getDagPath(0, dag_path)

    transform_fn = om.MFnTransform(dag_path)

    translation = transform_fn.translation(om.MSpace.kTransform)

    new_translation = om.MVector(translation.x + 2.0, translation.y + 2.0, translation.z)
    transform_fn.setTranslation(new_translation, om.MSpace.kTransform)

    mesh_fn = om.MFnMesh(dag_path)

    # Example: Move the first face outwards by 4 units
    face_id = 0
    vertices = om.MIntArray()
    mesh_fn.getPolygonVertices(face_id, vertices)

    translation_vector = om.MVector(0.0, 0.0, 4.0)

    for vertex_id in vertices:
        current_position = om.MPoint()
        mesh_fn.getPoint(vertex_id, current_position, om.MSpace.kWorld)
        new_position = current_position + translation_vector
        mesh_fn.setPoint(vertex_id, new_position, om.MSpace.kWorld)


# Execute Modification
modify_selected_object()
