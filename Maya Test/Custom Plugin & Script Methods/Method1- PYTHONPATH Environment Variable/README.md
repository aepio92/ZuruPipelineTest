1. Copy the script to the d:/repos directory.
2. Open Maya
3. Open the Script Editor
4. Run the Following Command

"exec(open("D:/repos/custom_setup.py").read())"

Note: This will execute the custom_setup.py script, 
      adding the specified paths to the sys.path. 
	  custom modules, scripts, or plugins can be 
	  imported from D:/repos in Maya.