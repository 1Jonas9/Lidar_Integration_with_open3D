import open3d as o3d

# Erstellen der Koordinatenachsen
def create_coordinate_axis(cas):
    coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(*cas)
    return coordinate_frame

# Visualisierung des Autos
def create_car(car_size):
    car = o3d.geometry.TriangleMesh.create_box(*car_size)
    car.compute_vertex_normals()
    car.paint_uniform_color([1, 0.54, 0])
    return car

def draw_geometries(geometries, view):
    o3d.visualization.draw_geometries(geometries, *view)
    