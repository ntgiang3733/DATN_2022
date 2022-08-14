import pickle
from flask import Flask, render_template, request
import os
from random import random
import cv2
import torch
import numpy
from PIL import Image, ImageFont, ImageDraw

import my_utils_yolo
import detect
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"

model_light = torch.hub.load('ultralytics/yolov5', 'custom', './runs/train_light/exp7/weights/best.pt')
model_sign = torch.hub.load('ultralytics/yolov5', 'custom', './runs/train_sign/exp6/weights/best.pt')

def get_file_content(src_img, file_name):
    source_img = Image.open(src_img)
    draw = ImageDraw.Draw(source_img)
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
        result_yolo_txt += my_utils_yolo.get_class_number(name) + ' ' + my_utils_yolo.convert(src_img, (x1, x2, y1, y2))
        draw.rectangle(((x1, y1), (x2, y2)), outline="white", width=4)
        print('TEST: ', name, int(source_img.size[0]) - x2)
        if (int(source_img.size[0]) - x2) < 200:
            w_name = len(name)*16
            draw.multiline_text((int(source_img.size[0])-w_name, y1-34), name, font=ImageFont.truetype("OpenSans-VariableFont_wdth,wght.ttf", 30), align="right")
        else:
            draw.text((x2, y1), name, font=ImageFont.truetype("OpenSans-VariableFont_wdth,wght.ttf", 30))

    source_img.save('static/results/' + file_name)
    return len(x)

def check_image(img):
    return img.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

@app.route("/", methods=['GET', 'POST'])
def home_page():
    if request.method == "POST":
         try:
            upload_file_name = request.files['file']
            image = False
            video = False
            if check_image(upload_file_name.filename):
                image = request.files['file']
            else:
                video = request.files['file']
            if image:
                path_to_save = os.path.join(app.config['UPLOAD_FOLDER'] + '/upload', image.filename)
                print("Save = ", path_to_save)
                image.save(path_to_save)

                ndet = get_file_content(path_to_save, image.filename)
                
                return render_template("index.html", image_0 = 'upload/' + image.filename, image_1 = 'results/' + image.filename, rand = str(random()),
                                           msg="Tải file lên thành công", ndet = ndet)
            elif video:
                path_to_save = os.path.join(app.config['UPLOAD_FOLDER'] + '/upload', video.filename)
                print("Save = ", path_to_save)
                video.save(path_to_save)

                detect.run(
                    weights='./runs/train_light/exp7/weights/best.pt',
                    conf_thres=0.5,
                    source=path_to_save,
                    exist_ok=True,
                    project='static/results',
                    name=''
                )
                return render_template("index.html", video_0 = 'upload/' + video.filename, video_1 = 'results/' + video.filename, rand = str(random()),
                                           msg="Tải file lên thành công", ndet=1)
            else:
                return render_template('index.html', msg='Hãy chọn file để tải lên')

         except Exception as ex:
            print(ex)
            return render_template('index.html', msg='Không nhận diện được vật thể')

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)