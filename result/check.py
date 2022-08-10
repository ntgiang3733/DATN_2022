# from PIL import Image, ImageFont, ImageDraw

# source_img = Image.open("im1.png")
# draw = ImageDraw.Draw(source_img)
# draw.rectangle(((0, 00), (100, 100)), outline="white", width=10)
# draw.text((20, 70), "cấm rẽ", font=ImageFont.truetype("OpenSans-VariableFont_wdth,wght.ttf", 56))

# source_img.show()
# source_img.save("i3.png")
#============================================================
import numpy as np
import cv2

cap = cv2.VideoCapture("vid1.mp4")

if not cap.isOpened():
    print("Cannot open camera")
    exit()
count = 0
while 1:
    print(count)
    count+=1
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", gray)
    if cv2.waitKey(1) == ord("q"):
        break

cap.realease()
cv2.destroyAllWindows()