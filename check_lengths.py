import os, json
import matplotlib.pyplot as plt
import numpy as np

dir_path = '/home/coinse/kimnal/autofl_with_passingtest/results/d4j_autofl_1/gpt-3.5-turbo-0125'

results = os.listdir(dir_path)

lengths = {True: [], False: []}

for result in results:
    file_path = os.path.join(dir_path, result)
    with open(file_path, 'r') as f:
        content = json.load(f)
        length = len(content["messages"])
        if isinstance(content["buggy_methods"], dict):
            buggy_methods = content["buggy_methods"].keys()

            for method in buggy_methods:
                is_found = content["buggy_methods"][method]["is_found"]

                if is_found:
                    lengths[True].append(length)
                else:
                    lengths[False].append(length)
true_length = [0]*max(lengths[True])
false_length = [0]*max(lengths[False])
for i in range(len(true_length)):
    true_length[i] = lengths[True].count(i)
for i in range(len(false_length)):
    false_length[i] = lengths[False].count(i)

true_sum = sum(true_length)
false_sum = sum(false_length)

for i in range(len(true_length)):
    true_length[i] /= true_sum
for i in range(len(false_length)):
    false_length[i] /= false_sum

x_axis = []
false_x_axis = []
true_y_axis = []
false_y_axis = []
for i, length in enumerate(true_length):
    if length != 0:
        x_axis.append(i)
        true_y_axis.append(length)
for i, length in enumerate(false_length):
    if length != 0:
        false_x_axis.append(i)
        false_y_axis.append(length)
print(x_axis)
print(true_y_axis)
print(false_y_axis)

# plt.bar(x_axis, true_y_axis)
# plt.title('Interaction length of true FL')
# plt.savefig('len_true_fl')

# plt.bar(false_x_axis, false_y_axis)
# plt.title('Interaction length of false FL')
# plt.savefig('len_false_fl')

# 막대 그래프의 너비와 위치 설정
bar_width = 0.35
index = np.arange(len(x_axis))

# 그래프 그리기
fig, ax = plt.subplots()
bar1 = ax.bar(index - bar_width/2, true_y_axis, bar_width, label='True')
bar2 = ax.bar(index + bar_width/2, false_y_axis, bar_width, label='False')

# 그래프 속성 설정
ax.set_xlabel('Length of interaction')
ax.set_title('Length of interaction')
ax.set_xticks(index)
ax.set_xticklabels(x_axis)
ax.legend()

# 그래프 보여주기
plt.savefig("length of interaction")