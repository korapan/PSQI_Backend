import cv2
import easyocr

image = cv2.imread(r'C:\Users\korapan\Desktop\project\image_test.png')

def pre(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_wb = cv2.threshold(image_gray,160,225,cv2.THRESH_BINARY)[1]

    desired_width = 702
    desired_height = 904

    # ปรับขนาดภาพ
    resized_image = cv2.resize(image_wb, (desired_width, desired_height))

    #roi = resized_image
    roi = resized_image[268:301,80:545]
    reader = easyocr.Reader(['en'])
    result = reader.readtext(roi,detail=0)
    #print(result)

    return result

ss = pre(image)
print(type(ss))
