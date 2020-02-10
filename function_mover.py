import sys
import os
import shutil

print("Source Directory: ", end='')
source_dir = input()
print("Destination Directory: ", end='')
destination_dir = input()

dir_dict = {"source":source_dir, "destination":destination_dir}

print("The number of target files: ", end='')
n = input()

while type(n) != int:
    try:
        n = int(n)
    except:
        print("Please give the integer for the number of target files")
        print("The number of target files: ", end='')
        n = input()
        n = int(n)

for i in dir_dict.keys():
    dir_name = dir_dict[i]
    
    if dir_name.endswith("\\") is False:
        dir_name += "\\"

    dir_dict[i] = dir_name


move_file_list = []

print("Give me the filenames.")

num_of_file = n
for i in range(n):
    file_name = input()
    print(file_name)
    if file_name in os.listdir(dir_dict["destination"]):
        print("There is the %s that have the same name in destination directory" % file_name)
        print("If you move the file from source to destination, please give the [y] ", end = '')
        answer = input()
        if answer == 'y':
            move_file_list.append(file_name)
        else:
            num_of_file -= 1
    else:
        move_file_list.append(file_name)

for i in range(num_of_file):
    file_name = move_file_list.pop(0)
    shutil.move(dir_dict["source"]+file_name, dir_dict["destination"]+file_name)