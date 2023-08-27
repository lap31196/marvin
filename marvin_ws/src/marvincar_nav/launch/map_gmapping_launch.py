#!/usr/bin/env python3
import os
from time import sleep

import launch
from launch.actions import TimerAction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python import get_package_share_directory

'''
parameters=[
        {'product_name': 'LDLiDAR_LD19'},
        {'topic_name': 'LiDAR/LD19 '},
        {'port_name': '/dev/ttyUSB0'},
        {'frame_id': 'lidar_frame'},
        {'laser_scan_dir': True},
        {'enable_angle_crop_func': False},
        {'angle_crop_min': 135.0},
        {'angle_crop_max': 225.0}
      ]
---
Parameter Description:
---
- Set laser scan directon: 
  1. Set counterclockwise, example: {'laser_scan_dir': True}
  2. Set clockwise,        example: {'laser_scan_dir': False}
- Angle crop setting, Mask data within the set angle range:
  1. Enable angle crop fuction:
    1.1. enable angle crop,  example: {'enable_angle_crop_func': True}
    1.2. disable angle crop, example: {'enable_angle_crop_func': Fnalse}
  2. Angle cropping interval setting:
  - The distance and intensity data within the set angle range will be set to 0.
  - angle >= 'angle_crop_min' and angle <= 'angle_crop_max' which is [angle_crop_min, angle_crop_max], unit is degress.
    example:
      {'angle_crop_min': 135.0}
      {'angle_crop_max': 225.0}
      which is [135.0, 225.0], angle unit is degress.
'''


def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration(
        'use_sim_time', default='False')
    return LaunchDescription([
        # Node(
        #    # ldlidar publisher node
        #    package='marvin_lidar',
        #    node_executable='marvin_lidar_node',
        #    name='marvin_lidar_node',
        #    output='screen',
        #    parameters=[
        #        {'product_name': 'LDLiDAR_LD19'},
        #        {'topic_name': '/scan'},
        #        {'port_name': '/dev/rplidar'},
        #        {'frame_id': 'lidar'},
        #        {'laser_scan_dir': True},
        #        {'enable_angle_crop_func': False},
        #        {'angle_crop_min': 135.0},
        #        {'angle_crop_max': 225.0}
        #    ]
        # ),
        # Node(
        #    package='slam_gmapping',
        #    node_namespace='transform',
        #    node_executable='transform',
        #    output='screen',
        #    parameters=[{'parents_frame': "odom",
        #                 'child_frame': "base_footprint"}]
        # ),
        # TimerAction(period=1.0, actions=[
        #     Node(
        #         package='slam_gmapping',
        #         node_namespace='slam_gmapping',
        #         node_executable='slam_gmapping',
        #         output='screen',
        #         parameters=[{'use_sim_time': use_sim_time}]
        #     )]),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('slam_gmapping'), 'launch'),
             '/slam_gmapping.launch.py'])
        )
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=['0.0435', '5.258E-05', '0.11',
        #                '3.14', '0', '0', 'base_link', 'lidar']
        # )
    ])
