import cv2
import easyocr
image = cv2.imread(r'C:\Users\korapan\Desktop\project\image_test.png')
image2 = cv2.imread(r'C:\Users\korapan\Desktop\project\image_test2.png')
image3 = cv2.imread(r'C:\Users\korapan\Desktop\project\image_test3.png')
image4 = cv2.imread(r'C:\Users\korapan\Desktop\project\image_test4.png')
image5 = cv2.imread(r'C:\Users\korapan\Desktop\project\image_test5.jpg')
image8 = cv2.imread(r'C:\Users\korapan\Desktop\project\image_test8.png')
image_gray = cv2.cvtColor(image8, cv2.COLOR_BGR2GRAY)
image_wb = cv2.threshold(image_gray,160,225,cv2.THRESH_BINARY)[1]

#desired_width = 702
#desired_height = 904

# ปรับขนาดภาพ
#resized_image = cv2.resize(image_wb, (desired_width, desired_height))

#cv2.imshow('Dee',image5)
#cv2.imshow('Dee1',resized_image)
#cv2.imshow('Dee',image_gray)

roi = image_wb[385:512,87:752]
#roi = resized_image
reader = easyocr.Reader(['en'])
result = reader.readtext(roi,detail=0)
print(result)
#print(result)
#cv2.imshow('1',resized_image[296:328,341:433 ])
#cv2.imshow('2',resized_image[356:385,383:471 ])
#cv2.imshow('3',resized_image[417:445,369:459 ])
cv2.imshow('4',image_wb[385:512,87:752 ])
cv2.waitKey(0)
cv2.destroyAllWindows