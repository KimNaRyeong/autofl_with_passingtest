import json

file_path = './results/passing_test_and_explain_5/gpt-3.5-turbo-0125/XFL-Chart_15.json'
file_path = './test.json'
# file_path = '/home/coinse/kimnal/autofl_with_passingtest/results/results/real_coverage_fun_token_sim_1/gpt-3.5-turbo-0125/XFL-Chart_1.json'
file_path = '/home/coinse/kimnal/autofl_with_passingtest/results/with_passing_test_1/gpt-3.5-turbo-0125/XFL-Chart_1.json'

with open(file_path, 'r') as f:
    dialog = json.load(f)

start = dialog["messages"][1]["content"]

print(start)