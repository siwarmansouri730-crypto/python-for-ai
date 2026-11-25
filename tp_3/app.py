import cv2
image = cv2.imread("opopo.jpg")

if image is not None:

    petite = cv2.resize(image,(400,300))

    cv2.imshow("Originale", image)
    cv2.imshow("Redimensionnee", petite)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
