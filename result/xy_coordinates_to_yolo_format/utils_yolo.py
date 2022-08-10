from PIL import Image

def convert(img_path, box):
    im=Image.open(img_path)
    size = (int(im.size[0]), int(im.size[1]))
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = round(x*dw, 6)
    w = round(w*dw, 6)
    y = round(y*dh, 6)
    h = round(h*dh, 6)
    return str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n'


def get_class_number(className):
    switcher = { 
        'đèn đỏ' : '0',
        'đèn xanh' : '1',
        'đèn vàng' : '2',
        'cấm ngược chiều' : '3',
        'cấm dừng và đỗ' : '4',
        'cấm rẽ' : '5',
        'giới hạn tốc độ' : '6',
        'cấm còn lại' : '7',
        'nguy hiểm' : '8',
        'hiệu lệnh' : '9'
    } 
    return switcher.get(className, "nothing") 


if __name__ == '__main__':
    className = 'giới hạn tốc độ'
    print(get_class_number(className))
