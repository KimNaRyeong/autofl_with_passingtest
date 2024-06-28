import os, json
import matplotlib.pyplot as plt



data_dir = './results/coverage_fun_token_sim_1/gpt-3.5-turbo-0125'

projects = os.listdir(data_dir)

for project in projects:
    file_name = os.path.join(data_dir, project)
    with open(file_name, 'r') as f:
        content = json.load(f)
        for message in content["messages"]:
            if message["role"] == "function" and message["name"] == "get_passing_tests_covered_classes":
                print(project)
                print(content["messages"][1]["content"])
                print(message["content"])
                print()