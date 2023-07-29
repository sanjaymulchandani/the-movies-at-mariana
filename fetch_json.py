import json

file_op = open('movies\index.json')
data = json.load(file_op)

for i in data:
    print(i)

file_op.close()