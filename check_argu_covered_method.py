import os, json
import matplotlib.pyplot as plt

func_calls = {'get_failing_tests_covered_classes': 0, "get_passing_tests_covered_classes": 0, "get_failing_tests_covered_methods_for_class": 0, "get_passing_tests_covered_methods_for_class": 0, "get_code_snippet": 0, "get_comments": 0}


# data_dir = './results/coverage_fun_token_sim_1/gpt-3.5-turbo-0125'
data_dir = './results/coverage_fun_cov_sim_2/gpt-3.5-turbo-0125'

projects = os.listdir(data_dir)

from_ft_covered = 0
from_pt_covered = 0
both = 0
empty = 0
none_of_them = 0

num_ftcc = 0
num_ptcc = 0
num_ftcm = 0
num_ptcm = 0

# projects = ['XFL-Chart_1.json']
for project in projects:
    file_name = os.path.join(data_dir, project)
    ft_covered_class = set()
    pt_covered_class = set()
    with open(file_name, 'r') as f:
        content = json.load(f)
        for message in content["messages"]:
            if message["role"] == "function" and "function_call" not in message.keys():
                if message["name"] == "get_failing_tests_covered_classes":
                    num_ftcc += 1
                    output = eval(message["content"])
                    for front in output.keys():
                        for class_name in output[front]:
                            class_signature = front + '.' + class_name
                            ft_covered_class.add(class_signature)
                elif message["name"] == "get_passing_tests_covered_classes":
                    num_ptcc += 1
                    output = eval(message["content"])
                    for front in output.keys():
                        for class_name in output[front]:
                            class_signature = front + '.' + class_name
                            pt_covered_class.add(class_signature)
            
            if "function_call" in message.keys():
                # if message["function_call"]["name"] == "get_failing_tests_covered_methods_for_class":
                #     argument = eval(message["function_call"]["arguments"])["class_name"]
                #     num_ftcm += 1
                #     if argument in ft_covered_class:
                #         if argument in pt_covered_class:
                #             both += 1
                #         else:
                #             from_ft_covered += 1
                #     elif argument in pt_covered_class:
                #         from_pt_covered += 1
                #     else:
                #         none_of_them += 1
                #         print(argument)
                if message["function_call"]["name"] == "get_passing_tests_covered_methods_for_class":
                    argument = eval(message["function_call"]["arguments"])["class_name"]
                    num_ptcm += 1
                    if argument in ft_covered_class:
                        if argument in pt_covered_class:
                            both += 1
                        else:
                            from_ft_covered += 1
                    elif argument in pt_covered_class:
                        from_pt_covered += 1
                    else:
                        none_of_them += 1
                        print(project)
                        print(argument)
print(from_pt_covered)
print(from_ft_covered)
print(both)
print(none_of_them)

print("======================")
print(num_ftcc)
print(num_ptcc)
print(num_ftcm)
print(num_ptcm)

# x_axis = ['get_failing_tests_covered_classes', 'get_passing_tests_covered_classes', "get_failing_tests_covered_methods_for_class", "get_passing_tests_covered_methods_for_class", "get_code_snippet", "get_comments"]
# y_axis = [func_calls[func_call] for func_call in x_axis]
# 
# x_axis = ['get_failing_tests\n_covered_classes', 'get_passing_tests\n_covered_classes', "get_failing_tests_covered\n_methods_for_class", "get_passing_tests_covered\n_methods_for_class", "get_code_snippet", "get_comments"]
# 
# plt.bar(x_axis, y_axis)
# 
# plt.title('Function calls of cov_sim_with_function')
# plt.xlabel('function calls')
# plt.xticks(rotation=45, fontsize=10)
# plt.subplots_adjust(bottom=0.4)
# 
# plt.savefig('func_calls_cov_sim')
# 
                # 