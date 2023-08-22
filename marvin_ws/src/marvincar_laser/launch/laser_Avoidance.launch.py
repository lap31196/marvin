from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    laser_Avoidance_node = Node(
        package='marvincar_laser',
        executable='laser_Avoidance',
    )
    lidar_node = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('marvin_lidar'), 'launch'),
'/ld19.launch.py'])
)
    bringup_node = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('marvincar_bringup'), 'launch'),
'/marvincar_bringup_launch.py'])
)
    
    launch_description = LaunchDescription([laser_Avoidance_node,lidar_node,bringup_node]) 
    return launch_description
