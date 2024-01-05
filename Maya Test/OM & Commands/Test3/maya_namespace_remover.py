import maya.cmds as cmds
import maya.OpenMaya as om


def remove_all_namespaces():
    # Getting all namespaces in the scene
    all_namespaces = cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True, absoluteName=True)

    # Iterating through namespaces in reverse order to handle nested namespaces properly
    for ns in reversed(all_namespaces):
        # Skipping the default namespace
        if ns == ":":
            continue

        # Removing the namespace
        try:
            cmds.namespace(removeNamespace=ns, mergeNamespaceWithRoot=True)
            print("Removed namespace:", ns)
        except Exception as e:
            print("Can Not Remove namespace:", ns, "-", e)


# Running the function to remove all namespaces
remove_all_namespaces()
