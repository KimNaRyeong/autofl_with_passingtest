import json, os, shutil

dest_dir = './coverage_data'
source_dir = "/home/coinse/kimnal/CS453/defects4j/coverage_data"

# already_exist_project = os.listdir(dest_dir)
projects = os.listdir(source_dir)

for project in projects:
    shutil.copytree(source_dir, dest_dir, dirs_exist_ok = True)
