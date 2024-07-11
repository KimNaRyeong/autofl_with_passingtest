import os, json
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

original = './combined_fl_results/d4j_gpt3-0125_results_R5_full.json'
passing_test = './combined_fl_results/d4j_token_sim_results_R5_full.json'

with open(original, 'r') as f:
    original_content = json.load(f)
with open(passing_test, 'r') as f:
    passing_content = json.load(f)

original_acc1 = set()
passing_acc1 = set()

for project in original_content["buggy_methods"].keys():
    for bug in original_content["buggy_methods"][project].keys():
        if original_content["buggy_methods"][project][bug]["autofl_rank"] == 1:
            original_acc1.add(project)

for project in passing_content["buggy_methods"].keys():
    for bug in passing_content["buggy_methods"][project].keys():
        if passing_content["buggy_methods"][project][bug]["autofl_rank"] == 1:
            passing_acc1.add(project)

# venn2([original_acc1, passing_acc1], ('original', 'with_passing_test'))
# plt.savefig('venn')

print(original_acc1-passing_acc1)
print("==========")
print(passing_acc1-original_acc1)