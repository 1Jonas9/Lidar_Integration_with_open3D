import open3d as o3d
import time
import preprocessing as p

def create_coordinate_axis(cas):
    coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(*cas)
    return coordinate_frame

def create_car(car_size):
    car = o3d.geometry.TriangleMesh.create_box(*car_size)
    car.compute_vertex_normals()
    car.paint_uniform_color([1, 0.54, 0])
    return car

def draw_geometries(geometries, view):
    o3d.visualization.draw_geometries(geometries, *view)
    
    
def visualize(car,coordinate_axis, window_size, number_of_loops, path, files):
    vis = o3d.visualization.Visualizer()
    vis.create_window(*window_size)
    
    for i in range(number_of_loops):
        pcd = p.read_data(path, files, i)
        update_loop(vis, pcd, car, coordinate_axis)

     
def update_loop(vis, pcd, car, coordinate_axis):
    vis.clear_geometries()
    # vis.poll_events()
    # vis.update_renderer()
    vis.add_geometry(pcd, False)
    vis.add_geometry(car)
    vis.add_geometry(coordinate_axis)
    vc = vis.get_view_control()
    vc.set_front([-1,0,1])
    vc.set_lookat([0,0,2])
    vc.set_up([0,0,1])
    vis.poll_events()
    vis.update_renderer()
    # time.sleep(0.05)
    
   