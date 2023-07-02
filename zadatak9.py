import cv2
import numpy as np

img_map = cv2.imread("karta_s_legendom.jpg")
img_hsv = cv2.cvtColor(img_map, cv2.COLOR_BGR2HSV)

replace_color = img_map[:1, -1:]
search_color = img_hsv[-1:, -1:]

low_b = np.array([search_color[0][0][0] - 20,
                  search_color[0][0][1] - 32, search_color[0][0][2] - 25])
upper_b = np.array([search_color[0][0][0] + 35,
                    search_color[0][0][1] + 35, search_color[0][0][2] + 35])


mask = cv2.inRange(img_hsv, low_b, upper_b)
filtered_img = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
img_map[mask > 0] = replace_color

croped_img = img_map[:, 0:-170]

cv2.imshow("map", croped_img)

cv2.waitKey()
cv2.destroyAllWindows()
