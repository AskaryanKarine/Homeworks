import argparse, os, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--info', action='store_true', help='shows the project directory tree')
args = parser.parse_args()

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}/{}'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f != 'task3.py':
                print('{}{}'.format(subindent, f))
            
if args.info:
    print('Here some info about this directory:')
    list_files(os.getcwd())
else:
    print("The program displays a tree of the project directory. For output, specify the flag '-i'.")