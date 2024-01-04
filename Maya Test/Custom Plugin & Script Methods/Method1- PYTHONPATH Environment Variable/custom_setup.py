import sys
import os

# Adding the custom folder to sys.path
custom_folder = r'D:\repos'
sys.path.append(custom_folder)

# adding subdirectories within the custom folder to sys.path
scripts_folder = os.path.join(custom_folder, 'scripts')
plugins_folder = os.path.join(custom_folder, 'plug-ins')

sys.path.append(scripts_folder)
sys.path.append(plugins_folder)

# Printing Message to indicate the successful integration of custom paths
print(f"Custom paths added to sys.path: {custom_folder}, {scripts_folder}, {plugins_folder}")
