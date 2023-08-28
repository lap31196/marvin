from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_gmapping',
            node_namespace='transform',
            node_executable='transform',
            output='screen',
            parameters=[{'parents_frame': "odom",
                         'child_frame': "base_footprint",
                         'x': 0.0, 'y': 0.0, 'z': 0.5,
                         'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}],
        ),
        Node(
            package='slam_gmapping',
            node_executable='slam_gmapping',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("slam_gmapping"), "params", "slam_gmapping.yaml")])

    ])
