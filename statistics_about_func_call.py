import os, json
import matplotlib.pyplot as plt

func_calls = {'get_failing_tests_covered_classes': 0, "get_passing_tests_covered_classes": 0, "get_failing_tests_covered_methods_for_class": 0, "get_passing_tests_covered_methods_for_class": 0, "get_code_snippet": 0, "get_comments": 0}


data_dir = './results/coverage_fun_token_sim_1/gpt-3.5-turbo-0125'
data_dir = './results/coverage_fun_cov_sim_1/gpt-3.5-turbo-0125'

projects = os.listdir(data_dir)

for project in projects:
    file_name = os.path.join(data_dir, project)
    with open(file_name, 'r') as f:
        content = json.load(f)
        for message in content["messages"]:
            if "function_call" in message.keys():
                if message["function_call"]["name"] == 'get_failing_tests_covered_classes':
                    func_calls['get_failing_tests_covered_classes'] += 1
                elif message["function_call"]["name"] == "get_passing_tests_covered_classes":
                    func_calls["get_passing_tests_covered_classes"] += 1
                elif message["function_call"]["name"] == "get_failing_tests_covered_methods_for_class":
                    func_calls["get_failing_tests_covered_methods_for_class"] += 1
                elif message["function_call"]["name"] == "get_passing_tests_covered_methods_for_class":
                    func_calls["get_passing_tests_covered_methods_for_class"] += 1
                elif message["function_call"]["name"] == "get_code_snippet":
                    func_calls["get_code_snippet"] += 1
                elif message["function_call"]["name"] == "get_comments":
                    func_calls["get_comments"] += 1
for func_call in func_calls.keys():
    func_calls[func_call] /= len(projects)

x_axis = ['get_failing_tests_covered_classes', 'get_passing_tests_covered_classes', "get_failing_tests_covered_methods_for_class", "get_passing_tests_covered_methods_for_class", "get_code_snippet", "get_comments"]
y_axis = [func_calls[func_call] for func_call in x_axis]

x_axis = ['get_failing_tests\n_covered_classes', 'get_passing_tests\n_covered_classes', "get_failing_tests_covered\n_methods_for_class", "get_passing_tests_covered\n_methods_for_class", "get_code_snippet", "get_comments"]

plt.bar(x_axis, y_axis)

plt.title('Function calls of cov_sim_with_function')
plt.xlabel('function calls')
plt.xticks(rotation=45, fontsize=10)
plt.subplots_adjust(bottom=0.4)

plt.savefig('func_calls_cov_sim')

                