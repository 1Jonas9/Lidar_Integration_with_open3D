import os
import numpy as np
import Preprocessing as p, Visualizing as v

#Constants
path =r"C:\Users\jonas\Desktop\Lidar_Integration\Scala 1\Kegeltests\Test1"
files = os.listdir(path)
view = ["Output", 1280, 720, 325, 100, False, False, False, [0,0,5] ,[0,0,1], [-1,0,1], 0.05]
window_size = [720, 325, 100]
car_size = [0.8, 0.5, 0.3]
cas = [2, [0, -5, 0]]

def main():
    geometries = []
    geometries.append(v.create_coordinate_axis(cas))
    geometries.append(v.create_car(car_size))
    for i in range(5):  
        geometries.append(p.read_data(path, files, i))
        v.draw_geometries(geometries, view)
        
main()
    