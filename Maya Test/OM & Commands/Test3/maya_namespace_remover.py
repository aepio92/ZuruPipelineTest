import maya.cmds as cmds
import maya.OpenMaya as om


def remove_all_namespaces():
    # Get all namespaces in the scene
    all_namespaces = cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True, absoluteName=True)

    # Iterate through namespaces in reverse order to handle nested namespaces properly
    for ns in reversed(all_namespaces):
        # Skip the default namespace
        if ns == ":":
            continue

        # Remove the namespace
        try:
            cmds.namespace(removeNamespace=ns, mergeNamespaceWithRoot=True)
            print("Removed namespace:", ns)
        except Exception as e:
            print("Can Not Remove namespace:", ns, "-", e)


# Run the function to remove all namespaces
remove_all_namespaces()
