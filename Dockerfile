FROM yahboomtechnology/ros-foxy:3.5.3
WORKDIR /marvin
COPY . .
RUN colcon build