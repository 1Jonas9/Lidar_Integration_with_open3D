import open3d as o3d

# Reading data in 
def create_pcd_list(path, files):
    data_list = []
    for i in range(len(files)):
        data_list.append(read_data(path, files, i))
    return data_list

def read_data(path, files, i):
    pcd = o3d.io.read_point_cloud(f"{path}\{files[i]}")
    return pcd
    
def voxel_downsampling(pcd, voxel_size):
    pcd_down = pcd.voxel_down_sample(voxel_size = voxel_size)
    return pcd_down

def normal_vectors(pcd_down):
    pcd_down.estimate_normals(search_param = o3d.geometry.KDTreeSearchParamHybrid(radius = 0.1, max_nn = 30))
    return pcd_down