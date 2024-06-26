import json

# file_path = './results/passing_test_and_explain_5/gpt-3.5-turbo-0125/XFL-Chart_15.j/son'

# file_path = './test.json'
# file_path = '/home/coinse/kimnal/autofl_with_passingtest/results/coverage_fun_token_sim_1/gpt-3.5-turbo-0125/XFL-Chart_1.json'
# with open(file_path, 'r') as f:
#     dialog = json.load(f)

# start = dialog["messages"][1]["content"]

# print(start)

# =======================================================================================================
projects = {'Chart': 26, 'Closure': 133, 'Lang': 65, 'Math': 106, 'Time': 27}
file_path = "/home/coinse/kimnal/autofl_with_passingtest/combined_fl_results/coverage_fun_token_sim_results_R5_full_old.json"
with open(file_path, 'r') as f:
    content = json.load(f)

buggy_methods = content["buggy_methods"].keys()
num_buggy_methods = 0
total_num = 0
for project in projects.keys():
    for i in range(1, projects[project]+1):
        project_name = f"{project}_{str(i)}"
        if project_name not in buggy_methods:
            print(project_name)
        else:
            num_buggy_methods += 1
        total_num += 1
print(num_buggy_methods)
print(total_num)
print("=============================================================")

file_path = "/home/coinse/kimnal/autofl_with_passingtest/combined_fl_results/d4j_gpt3_results_R5.json"
with open(file_path, 'r') as f:
    content = json.load(f)

buggy_methods = content["buggy_methods"].keys()
num_buggy_methods = 0
total_num = 0
for project in projects.keys():
    for i in range(1, projects[project]+1):
        project_name = f"{project}_{str(i)}"
        if project_name not in buggy_methods:
            print(project_name)
        else:
            num_buggy_methods += 1
        total_num += 1
print(num_buggy_methods)
print(total_num)


# print(content["buggy_methods"]["Chart_1"])
