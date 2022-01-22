import os
from re import L
import numpy as np
from Software.preprocessing import create_data_list, create_pcd_list
import preprocessing as p 
import visualizing as v
import functions as f


#Constants
path =r"C:\Users\jonas\Desktop\Lidar_Integration\Scala 1\Kegeltests\Test1"
files = os.listdir(path)
view = ["Output", 1280, 720, 350, 100, False, False, False, [0,0,5] ,[0,0,1], [-1,0,1], 0.05]
window_size = ["Output",1280, 720, 350, 100]
car_size = [0.8, 0.5, 0.3]
cas = [0.5, [0, -2, 0]]

def main():
    # geometries = []
    # geometries.append(v.create_coordinate_axis(cas))
    # geometries.append(v.create_car(car_size))
    # geometries.append(p.read_data(path, files, i))
    # v.draw_geometries(geometries, view)
    coordinate_axis = v.create_coordinate_axis(cas)
    car = v.create_car(car_size)
    v.visualize(car, coordinate_axis, window_size, len(files), path, files)

main()
    