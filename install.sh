#!/bin/sh
sudo apt-get install apt-utils
sudo mkdir -p /etc/apt/keyrings
curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null
sudo apt-get install apt-transport-https
echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \
sudo tee /etc/apt/sources.list.d/librealsense.list
sudo -y apt-get update 
sudo -y apt-get install librealsense2-dkms
sudo -y apt-get install librealsense2-utils

sudo apt-get -y install ros-foxy-depthimage-to-laserscan
sudo apt-get -y install ros-foxy-gazebo-ros-pkgs
sudo apt-get -y install ros-foxy-opencv-python
sudo apt-get -y install ros-foxy-turtlesim
sudo apt-get -y install ros-foxy-librealsense2
sudo apt-get -y install ros-foxy-xacro
