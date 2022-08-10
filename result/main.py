import torch
import numpy
from PIL import Image, ImageFont, ImageDraw

model_light = torch.hub.load('ultralytics/yolov5', 'custom', './light_weight/light.pt')
model_sign = torch.hub.load('ultralytics/yolov5', 'custom', './sign_weight/sign.pt')

r = model_light('vid1.mp4')
r.save()

# source_img = Image.open("im1.png")
# draw = ImageDraw.Draw(source_img)

# results_sign = model_sign('im1.png')
# results_light = model_light('im1.png')

# res_sign_arr = numpy.array(results_sign.pandas().xyxy[0].to_dict(orient="records"))
# res_light_arr = numpy.array(results_light.pandas().xyxy[0].to_dict(orient="records"))

# x = numpy.concatenate((res_sign_arr, res_light_arr))

# for result in x:
#     confidence = result['confidence']
#     name = result['name']
#     clas = result['class']
#     x1 = int(result['xmin'])
#     y1 = int(result['ymin'])
#     x2 = int(result['xmax'])
#     y2 = int(result['ymax'])

#     draw.rectangle(((x1, y1), (x2, y2)), outline="white", width=2)
#     draw.text((x1+3, y1-20), name, font=ImageFont.truetype("OpenSans-VariableFont_wdth,wght.ttf", 16))

# source_img.show()








# source_img.save("i3.png")

# results_sign.show()

# print(results_sign.pandas().xyxy[0])