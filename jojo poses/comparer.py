from scipy.spatial import distance as dist

from compareradiusfinder import radiusfinder

from comparemoments import zernikemoments

import pickle

import cv2


def compare(jojo, featagainst):
    results = {} #info storage

    for (name, features) in jojo.items(): #runs through existing pickle file of with imagemoments of jojo photos
        print(name, features)

        d = dist.euclidean(featagainst, features) #finds the distance between the input image moments and the jojo moments

        results[name] = d

    results = sorted([(v,k) for (k,v) in results.items()])

    finalanswer = results[0][1].replace("poses","").replace("blackandwhite.jpg","")

    finalanswer = finalanswer[1:]

    return finalanswer
    


def main():

    radius = radiusfinder()
    features = zernikemoments(radius)
    print(features)
    infile = open("moment_dict.p","rb")
    new_dict = pickle.load(infile)

    finalanswer = compare(new_dict, features)
    
    infile.close()

    print("Is this pose? "+finalanswer)

if __name__ == "__main__":
    main()



#https://www.pyimagesearch.com/2014/05/19/building-pokedex-python-comparing-shape-descriptors-opencv/
