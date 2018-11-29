import sys
import json 

json_data=open('test.json').read()
data = json.loads(json_data)

print(data)

map=data['maps']
print(map)

maps=data['maps']
print(maps)

for i, map in enumerate(maps):
    print(i,map)
    id=map['id']
    cate=map['iscategorical']
    print(i,id,cate)
