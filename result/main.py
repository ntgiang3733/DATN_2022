import torch

model_light = torch.hub.load('ultralytics/yolov5', 'custom', './light_weight/light.pt')
model_sign = torch.hub.load('ultralytics/yolov5', 'custom', './sign_weight/sign.pt')

# results_light = model_light('im1.png')

# results_light.show()

# print(results_light.pandas().xyxy[0])

results_sign = model_sign('im1.png')

results_sign.show()

# print(results_sign.pandas().xyxy[0])