FROM yahboomtechnology/ros-foxy:3.5.3
WORKDIR /root/marvin
COPY . .
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
WORKDIR /root/marvin/software/library_ws
RUN colcon build
WORKDIR /root/marvin/marvin_ws
RUN colcon build
#RUN chmod +x /root/marvin/install.sh
#RUN /root/marvin/install.sh
#RUN colcon build 
