import os, json
from tqdm import tqdm

data_dir = './data/defects4j'

projects = os.listdir(data_dir)

for project in projects:
    test_snippet_file = os.path.join(data_dir, project, test_snippet.json)
    with open(test_snippet_file, 'r') as tf:
        tests = json.load(test_snippet_file)
    
    gzoltar_test_file = os.path.join('./coverage_data', project, 'tests.csv')

