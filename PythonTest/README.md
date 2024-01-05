To Install the pyproject.toml file
1. Open cmd in the directory
2. Type in the following command

   'pip install .'
   
3. Once build is done a folder will be created called build/lib/pyls
4. include the desired_path/build/lib/pyls inside system environment variables under Path.   

5. Once the path is included can be executed the following commands

     pyls --help           = to see the commands avaliable.
     pyls -A	           = to see the structure avaliable in the json file including the names starts with '.'
	 pyls -l               = to see the content in the list format
	 pyls -r               = to see the content in the reverse order
	 pyls -t               = to sort the content according to the date modified
	 pyls -filter=file/dir = to filter the contents
	 pyls <name of the directory> = to browse inside a directory 