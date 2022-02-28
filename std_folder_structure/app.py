import os
from std_folder_structure.dir_names import * # Imports the list of folders from dir_names.py file


main_dir = [gryffindor, slytherin, hufflepuff, ravenclaw]			# Loading the list of sub-directories
root_dir = "~/dev/program/Hogwarts Houses"
main_dir_names = ['Gryffindor', 'Slytherin', 'Hufflepuff','Ravenclaw'] # Name of the sub-directories
def run():
	# Create directory
	for i in range(0, len(main_dir)):
		for j in range(0,len(main_dir[i])):
			dirName = str(root_dir) + '/' + str(main_dir_names[i]) +'/' + str(main_dir[i][j])
			try:
				# Create target Directory
				os.makedirs(dirName)
				print("Directory " , dirName ,  " Created ")
			except FileExistsError:
				print("Directory " , dirName ,  " already exists")        
		    
		    # Create target Directory if don't exist
			if not os.path.exists(dirName):
				os.makedirs(dirName)
				print("Directory " , dirName ,  " Created ")
			else:
				print("Directory " , dirName ,  " already exists")