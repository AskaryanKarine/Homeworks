import os
import subprocess

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

os.system('pip install -r reqs.txt')
os.remove('reqs.txt')