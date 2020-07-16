import mahotas
import pickle
from imutils.paths import list_images
import cv2
import numpy as np



def zernikemoments(radii):
    momentdict = dict()
    for name,radius in radii.items():
        image = cv2.imread(name, 0) #converts image to gray scale so it is a 2d array
        cv2.imshow("dede", image)
        print(mahotas.features.zernike_moments(image, radius))

        momentdict[name] = mahotas.features.zernike_moments(image,radius)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return momentdict
        




def main():
    
    file = open("radius_dict.p" , "rb") #opens pickled file in binary
    radii = pickle.load(file) #makes the dictionary in pickle file readable
    momentdict = zernikemoments(radii)
    file.close() #closes file

    pickle.dump(momentdict, open("moment_dict.p", "wb"))

    

if __name__ == "__main__":
    main()


#https://www.pyimagesearch.com/2014/05/19/building-pokedex-python-comparing-shape-descriptors-opencv/

#date accessed 6/18/2020 https://www.pyimagesearch.com/2014/04/07/building-pokedex-python-indexing-sprites-using-shape-descriptors-step-3-6/
    
