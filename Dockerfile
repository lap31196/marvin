FROM yahboomtechnology/ros-foxy:3.5.3
WORKDIR /root/marvin
COPY . .
RUN chmod +x /install.sh
RUN /install.sh
RUN colcon build
