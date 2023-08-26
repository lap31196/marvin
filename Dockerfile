FROM yahboomtechnology/ros-foxy:3.5.3
WORKDIR /root/marvin
COPY . .
#WORKDIR /root/marvin/marvin_ws
#RUN colcon build
RUN chmod +x /root/marvin/install.sh
RUN /root/marvin/install.sh
#RUN colcon build 
