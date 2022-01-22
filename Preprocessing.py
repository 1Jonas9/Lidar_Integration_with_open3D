import open3d as o3d

def read_data(path, files, i):
    pcd = o3d.io.read_point_cloud(f"{path}\{files[i]}")
    return pcd
    
def voxel_downsampling(pcd, voxel_size):
    pcd_down = pcd.voxel_down_sample(voxel_size = voxel_size)
    return pcd_down

def normal_vectors(pcd_down):
    pcd_down.estimate_normals(search_param = o3d.geometry.KDTreeSearchParamHybrid(radius = 0.1, max_nn = 30))
    return pcd_down
