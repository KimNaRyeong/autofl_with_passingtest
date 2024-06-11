import json

file_path = './test.json'

with open(file_path, 'r') as f:
    dialog = json.load(f)

start = dialog["messages"][1]["content"]

print(start)