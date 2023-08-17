import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    joy_launch_path = PathJoinSubstitution(
        [FindPackageShare('marvin_sim_bringup'), 'launch',
         'joy_teleop.launch.py']
    )

    description_launch_path = PathJoinSubstitution(
        [FindPackageShare('marvin_description'), 'launch',
         'description.launch.py']
    )

    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare('marvin_sim_gazebo'),
         'rviz', 'description.rviz']
    )

    rviz_slam_config_path = PathJoinSubstitution(
        [FindPackageShare('marvin_navigation'),
         'rviz', 'marvin_slam.rviz']
    )

    rviz_nav_config_path = PathJoinSubstitution(
        [FindPackageShare('marvin_navigation'),
         'rviz', 'marvin_navigation.rviz']
    )
    
    twist_mux_params = os.path.join(get_package_share_directory('marvin_navigation'),'config','twist_mux.yaml')


    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use sim time if true'
        ),

        DeclareLaunchArgument(
            name='rviz_gaz',
            default_value='false',
            description='Run rviz'
        ),

        DeclareLaunchArgument(
            name='rviz_slam',
            default_value='false',
            description='Run rviz_slam'
        ),

        DeclareLaunchArgument(
            name='rviz_nav',
            default_value='false',
            description='Run rviz_nav'
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(description_launch_path),
            launch_arguments={'use_sim_time': 'true',
                              }.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(joy_launch_path),
            launch_arguments={'use_sim_time': 'true'
                              }.items()
        ),

        Node(
            package="twist_mux",
            executable="twist_mux",
            parameters=[twist_mux_params, {'use_sim_time': True}],
            remappings=[('/cmd_vel_out','/diff_cont/cmd_vel_unstamped')]
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            output='screen',
            arguments=["-topic", "robot_description", "-entity", "marvin_description",
                       "-x", '-0.004612',
                       "-y", '0.000051',
                       "-z", '0.08',
                       "-Y", '0.0']
        ),

        Node(
            package='marvin_sim_gazebo',
            executable='command_timeout.py',
            name='command_timeout'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
            condition=IfCondition(LaunchConfiguration("rviz_gaz")),
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_slam_config_path],
            condition=IfCondition(LaunchConfiguration("rviz_slam")),
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_nav_config_path],
            condition=IfCondition(LaunchConfiguration("rviz_nav")),
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
        ),
    ])
