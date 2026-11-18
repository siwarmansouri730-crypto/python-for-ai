import cv2
image = cv2.imread ("image.jpg")

if image is None :
 print("image introuvable")

else :
 gris = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 cv2.imshow("Originiale",image)
 cv2.imshow("Niveaux de gris",gris)
 cv2.waitkey(0)



 cv2.destroyALLWindows()
 