from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node
import os


def generate_launch_description():
    package_share_path = str(get_package_share_path('marvincar_nav'))
    package_path = os.path.abspath(os.path.join(
        package_share_path, "../../../../src/marvincar_nav"))
    map_name = "marvincar"
    default_map_path = os.path.join(package_path, 'maps', map_name)

    map_arg = DeclareLaunchArgument(name='map_path', default_value=str(default_map_path),
                                    description='The path of the map')

    map_saver_node = Node(
        package='nav2_map_server',
        executable='map_saver_cli',
        arguments=[
            '-f', LaunchConfiguration('map_path'), '--ros-args', '-p', 'save_map_timeout:=10000'],
    )

    return LaunchDescription([
        map_arg,
        map_saver_node
    ])
