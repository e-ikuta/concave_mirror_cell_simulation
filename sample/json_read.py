import json

f = open('sample.json')
l = json.load(f)

print(l['x_0'])
