import json
filename="C:\\Users\\ASUS\\Desktop\\1.json"
#dumps：将python中的 字典 转换为 字符串
test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}#测试字典
print(test_dict)
print(type(test_dict))
#dumps 将数据转换成字符串
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))

#loads: 将 字符串 转换为 字典
new_dict = json.loads(json_str)

#dump: 将数据写入json文件中
with open(filename,"w") as f:
     json.dump(new_dict,f)
     print("加载入文件完成...")