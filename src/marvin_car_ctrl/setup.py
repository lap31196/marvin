from setuptools import setup
import os
from glob import glob

package_name = 'marvin_car_ctrl'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']), (os.path.join('share',package_name,'launch'),glob(os.path.join('launch','*launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nx-ros2',
    maintainer_email='nx-ros2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'marvin_car_keyboard	= marvin_car_ctrl.marvin_car_keyboard:main',
        'marvin_car_joy	= marvin_car_ctrl.marvin_car_joy:main',
        ],
    },
)
