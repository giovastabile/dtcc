# Copyright (C) 2023 Anders Logg
# Licensed under the MIT License
#
# This demo illustrates how to build a city model from raw data,
# and viewing the resulting mesh model together with the pointcloud.

from pathlib import Path
import dtcc

# Build a mesh from raw data
data_directory = Path("../data/helsingborg-residential-2022")
p = dtcc.builder.parameters.default()
p["data_directory"] = data_directory
p["domain_height"] = 75.0
dtcc.builder.build(p)

buildings_path = data_directory / "footprints.shp"
pointcloud_path = data_directory

origin, bounds = dtcc.builder.calculate_bounds(buildings_path, pointcloud_path, p)
city = dtcc.io.load_city(buildings_path, bounds=bounds)
pointcloud = dtcc.io.load_pointcloud(pointcloud_path, bounds=bounds)

# Build a city
city = dtcc.builder.build_city(city, pointcloud, bounds, p)

# From the city build meshes
volume_mesh, boundary_mesh = dtcc.builder.build_volume_mesh(city)

# From the city build meshes
ground_mesh, building_mesh = dtcc.builder.build_mesh(city, p)

# Remove unwanted outliers from the point cloud
pc = pointcloud.remove_global_outliers(3)

# Create a scene and window. Add geometry to scene
scene = dtcc.viewer.Scene()
window = dtcc.viewer.Window(1200, 800)
scene.add_mesh("Building mesh", building_mesh)
scene.add_mesh("Ground mesh", ground_mesh)
scene.add_mesh("Boundary mesh", boundary_mesh)
scene.add_pointcloud("Point cloud", pc)

# Render geometry
window.render(scene)