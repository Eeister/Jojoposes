import cv2
import mahotas

def zernikemoments(radius):
    image = cv2.imread("foregroundextrpart3blackandwhite.jpg", 0) #converts image to gray scale so it is a 2d array

    features = mahotas.features.zernike_moments(image,radius)

    return features
