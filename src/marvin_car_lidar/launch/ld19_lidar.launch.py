#!/usr/bin/env python3
import os
from time import sleep

import launch
from launch.actions import TimerAction
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python import get_package_share_directory



def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='False')
    return LaunchDescription([
        Node(
            # ldlidar publisher node
            package='ldlidar_stl_ros2',
            node_executable='ldlidar_stl_ros2_node',
            name='ldlidar_stl_ros2_node',
            output='screen',
            parameters=[
                {'product_name': 'LDLiDAR_LD19'},
                {'topic_name': '/scan'},
                {'port_name': '/dev/rplidar'},
                {'frame_id': 'lidar'},
                {'laser_scan_dir': True},
                {'enable_angle_crop_func': False},
                {'angle_crop_min': 135.0},
                {'angle_crop_max': 225.0}
            ]
        ),
        Node(
            package='slam_gmapping',
            node_namespace='transform',
            node_executable='transform',
            output='screen',
            parameters=[{'parents_frame': "odom",
                         'child_frame': "laser",
                         'x': 0.1, 'y': 0.2, 'z': 0.5,
                         'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}],
        ),
        TimerAction(period=1.0, actions=[
            Node(
                package='slam_gmapping',
                node_namespace='slam_gmapping',
                node_executable='slam_gmapping',
                output='screen',
                parameters=[{'use_sim_time': use_sim_time}]
            ),
          ])
    ])
