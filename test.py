import json

# file_path = './results/passing_test_and_explain_5/gpt-3.5-turbo-0125/XFL-Chart_15.j/son'

file_path = './test.json'
file_path = '/home/coinse/kimnal/autofl_with_passingtest/results/coverage_fun_cov_sim_1/gpt-3.5-turbo-0125/XFL-Chart_11.json'
with open(file_path, 'r') as f:
    dialog = json.load(f)

start = dialog["messages"][1]["content"]

print(start)