import json
filename="C:\\Users\\ASUS\\Desktop\\1.json"
with open(filename,'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
print(load_dict)

with open(filename,"w") as dump_f:
    json.dump(load_dict,dump_f)