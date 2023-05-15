import cv2
path = r"C:/Users/aspi/Downloads/abcd.jpg"
src = cv2.imread(path)
window_name = "Ima"
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0)





import cv2
path = r"C:/Users/aspi/Downloads/abcd.jpg"
src = cv2.imread(path)
window_name = "Ima"
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)



import cv2
path = r"C:\Users\Abdul\OneDrive\Pictures\Naruto WP\wallpaperflare.com_wallpaper.jpg"
src = cv2.imread(path)
window_name = "Ima"
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0)

