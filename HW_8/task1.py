import os, shutil
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name')
parser.add_argument('-o', '--old_dir')
parser.add_argument('-new', '--new_dir')
args = parser.parse_args()


if args.old_dir is None:
    print("OLD FOLDER NOT FOUND") 
    raise SystemExit
elif not os.path.isdir(args.old_dir):
    print("OLD FOLDER NOT FOUND") 
    raise SystemExit


if args.name is None:
    print("FILE NOT FOUND") 
    raise SystemExit
elif not os.path.isfile(args.old_dir+'/'+args.name) :
    print("FILE NOT FOUND") 
    raise SystemExit

if args.new_dir is None and not os.path.isdir('None'):
    os.mkdir('None')
else:
    if not os.path.isdir(args.new_dir):
        os.mkdir(args.new_dir)
        

src = args.old_dir+'/'+args.name
shutil.move(src, str(args.new_dir))
