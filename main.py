import os
import numpy as np
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
    coordinate_axis = v.create_coordinate_axis(cas)
    car = v.create_better_car(car_size)
    v.visualize(car, coordinate_axis, window_size, len(files), path, files)

main()
    