import os
import numpy as np
import preprocessing as p, visualizing as v

def get_distances(pcd):
    points = pcd.points
    distance = []
    for i in range(len(points)):
        distance.append(np.sqrt(points[i][0]**2 + points[i][1]**2))
    
    return distance 