import open3d as o3d
import preprocessing as p

def create_coordinate_axis(cas):
    coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(*cas)
    return coordinate_frame

def create_car(car_size):
    car = o3d.geometry.TriangleMesh.create_box(*car_size)
    car.compute_vertex_normals()
    car.paint_uniform_color([1, 0.54, 0])
    return car

def create_better_car(car_size):
    length = car_size[0]
    width = car_size[1]
    height = car_size[2]
    points =[  [length, -width/2, 0],
                [0, -width/2, 0],
                [0, width/2, 0],
                [length, width/2, 0],
                [length, -width/2, height],
                [0, -width/2, height],
                [0, width/2, height],
                [length, width/2, height],
                [length,0,0],
                [length+2,0,0]
            ]
    
    lines = [   [0,1],
                [1,2],
                [2,3],
                [3,0],
                [0,4],
                [1,5],
                [2,6],
                [3,7],
                [4,5],
                [5,6],
                [6,7],
                [7,4],
                [8,9]
            ]

    line_set = o3d.geometry.LineSet(
        points=o3d.utility.Vector3dVector(points),
        lines=o3d.utility.Vector2iVector(lines),
    )
    return line_set
    
def draw_geometries(geometries, view):
    o3d.visualization.draw_geometries(geometries, *view)
    
    
def visualize(car,coordinate_axis, window_size, number_of_loops, path, files):
    vis = o3d.visualization.Visualizer()
    vis.create_window(*window_size)
    
    for i in range(number_of_loops):
        pcd = p.read_data(path, files, i)
        pcd_down = p.voxel_downsampling(pcd, 0.1)
        update_loop(vis, pcd_down, car, coordinate_axis)

     
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
    
   