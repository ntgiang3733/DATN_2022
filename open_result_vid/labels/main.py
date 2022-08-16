import os.path
import json

def get_class_name(classNum):
    switcher = { 
        '0' : 'cấm ngược chiều' ,
        '1' : 'cấm dừng và đỗ' ,
        '2' : 'cấm rẽ' ,
        '3' : 'giới hạn tốc độ' ,
        '4' : 'cấm còn lại' ,
        '5' : 'nguy hiểm' ,
        '6' : 'hiệu lệnh' 
    } 
    return switcher.get(classNum+3, "nothing") 

def get_data(data):
    newdata = []
    x = data.split('\n')
    for item in x:
        if len(item) > 0:
            newdata.append("class_" + str(int(item[0])+3))
    return newdata




res = []
for x in range(710):
    if os.path.exists('v2_' + str(x+1) + '.txt'):
        f = open('v2_' + str(x+1) + '.txt', 'r')
        res.append(get_data(f.read()))
    else:
        res.append([])


jsonStr = json.dumps(res)

f = open('res/a.txt', 'w')
f.write(jsonStr)
f.close()
