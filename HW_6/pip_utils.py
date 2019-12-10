import os
import subprocess

def get_update_list() -> str:
    """
    A function to create a list of libraries that need to be updated.
    The function returns a string containing a list of updated functions 
    in the format old_lib_name==new_version
    The string is written to a file reqs.txt
    """
    libs=[]
    s=''
    code2 = subprocess.check_output(['pip','list', '-o'],universal_newlines=False)

    with open('reqs.txt', 'w') as f:
        f.write(code2.decode('utf-8').strip())

    with open('reqs.txt', 'r') as f:
        for line in f.readlines():
            x = line.split()
            if len(x)>0: libs.append(x)

    for i in range(2, len(libs)):
        s+=str(libs[i][0])+'=='+libs[i][2]+'\n'

    with open('reqs.txt', 'w') as f:
        f.write(s)
    return s

def updating() -> None:
    """
    Function to install library updates.
    The function installs libraries from the file reqs.txt and deletes this file.
    """
    os.system('pip install -r reqs.txt')
    os.remove('reqs.txt')