# marvin
El siguiente repositorio contiene todos los paquetes necesarios para la instalacion y uso del simulador del vehiculo M.A.R.V.I.N

docker run -it --device=/dev/myserial --device=/dev/rplidar --device=/dev/video0 --device=/dev/video1  --device=/dev/video2 --device=/dev/video3 --device=/dev/video4 --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix marvin:01 /bin/bash

instrucciones para descargar librealsense
sudo mkdir -p /etc/apt/keyrings
curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null
sudo apt-get install apt-transport-https
echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \
sudo tee /etc/apt/sources.list.d/librealsense.list
sudo apt-get update
sudo apt-get install librealsense2*
