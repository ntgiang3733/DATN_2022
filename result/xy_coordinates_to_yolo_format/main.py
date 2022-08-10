import torch
import numpy
import utils_yolo
import os

model_light = torch.hub.load('ultralytics/yolov5', 'custom', '../light_weight/light.pt')
model_sign = torch.hub.load('ultralytics/yolov5', 'custom', '../sign_weight/sign.pt')

def getFileContent(src_img):
    results_sign = model_sign(src_img)
    results_light = model_light(src_img)

    res_sign_arr = numpy.array(results_sign.pandas().xyxy[0].to_dict(orient="records"))
    res_light_arr = numpy.array(results_light.pandas().xyxy[0].to_dict(orient="records"))
    x = numpy.concatenate((res_sign_arr, res_light_arr))

    result_yolo_txt = ''
    for result in x:
        name = result['name']
        x1 = int(result['xmin'])
        y1 = int(result['ymin'])
        x2 = int(result['xmax'])
        y2 = int(result['ymax'])
        result_yolo_txt += utils_yolo.get_class_number(name) + ' ' + utils_yolo.convert(src_img, (x1, x2, y1, y2))
    
    return result_yolo_txt

le = len(os.listdir(os.getcwd()))
count = 0
for filename in os.listdir(os.getcwd()):
    count += 1
    if filename != 'main.py' and filename != 'utils_yolo.py' and filename != 'res' and filename != '__pycache__':
        with open('./res/' + filename.replace('.png', '.txt').replace('.jpg', '.txt'),'w',encoding = 'utf-8') as f: 
            f.write(getFileContent(filename))
            print(str(count) + '/' + str(le) + ' : ' + filename)
            f.close()