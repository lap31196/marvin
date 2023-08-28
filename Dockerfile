FROM yahboomtechnology/ros-foxy:3.5.3
WORKDIR /root/marvin
COPY . .
COPY ./configurations/.bashrc ..
WORKDIR /root/marvin/marvin_ws
RUN colcon build
WORKDIR /root/marvin/software/library_ws
RUN colcon build
