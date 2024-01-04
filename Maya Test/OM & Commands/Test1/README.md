1. Add mayapy.exe in System Environment Variable Path 
   (Sould be located in 'C:\Program Files\Autodesk\Maya20xx\bin' or Installation folder)
2. Open maya_script.py file
3. Under scene path section find the following line of code

   scene_path = "d:/scene.ma"  
4. Change the "d:/scene.ma" to desired path on system.

5. Open terminal in the directory where maya_script.py is located.
6. Type in the following command
   'mayapy maya_script.py'

NOTE: Make Sure your system environment variable path is set to the bin folder of your 'InstallDirectory\maya20xx\bin'   