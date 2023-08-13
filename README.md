# marvin
El siguiente repositorio contiene todos los paquetes necesarios para la instalacion y uso del simulador del vehiculo M.A.R.V.I.N

docker run -it --device=/dev/myserial --device=/dev/rplidar --device=/dev/video0 --device=/dev/video1  --device=/dev/video2 --device=/dev/video3 --device=/dev/video4 --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix marvin:01 /bin/bash
