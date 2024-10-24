## RPi Set up
### Install OpenSSH
Install OpenSSH for  remotely controlling RPi using the command in the terminal (Ctrl + Alt + T)
```sh
sudo apt update
sudo apt install openssh-server -y
sudo systemctl start ssh
hostname -I
```
Now you will see your ip address let it be $ip_address
Get inter your RPi using shh
```sh
##command
ssh -X p3dx@$ip_address
##password
p3dX
```
Verify the ubantu version
```sh
lsb_release -a
```

Make ROS2 workspace
```sh
mkdir ~/Project/p3dx_ws/src && cd ~/Project/p3dx_ws/
colcon build
```

Download the necssary packages
```sh
cd
sudo apt update
sudo apt install ros-$ROS_DISTRO-navigation2 -y
sudo apt install ros-$ROS_DISTRO-nav2-bringup -y
sudo apt install ros-$ROS_DISTRO-robot-localizatio -y
sudo apt install ros-$ROS_DISTRO-slam-toolbox -y
sudo apt install python3 python3-pip -y
sudo apt install python3-pyqt5 -y
sudo apt install pyqt5-dev-tools -y
sudo apt install ros-jazzy-twist-mux -y
```
Download Docker Engine
```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo apt  install docker-compose -y

```

Clone the repo
```sh
cd ~/Project/p3dx_ws/src/
git clone https://github.com/Rahul-Tom/p3dx_description_ros.git
git clone https://github.com/AlexKaravaev/csm.git
git clone https://github.com/AlexKaravaev/ros2_laser_scan_matcher.git
```

Build the workspace
```sh
cd ~/Project/p3dx_ws
colcon build --symlink install
```
If you are getting error during colcon build replace #include <tf2_geometry_msgs/tf2_geometry_msgs.h> with #include <tf2_geometry_msgs/tf2_geometry_msgs.hpp> in line 47 of header file in include directory of ros2_laser_scan_matcher package.

clone the docker and gui repo

```sh
git clone https://github.com/Rahul-Tom/p3dx_gui.git
git clone https://github.com/Rahul-Tom/p3dx_docker.git
```
building the docker containers
#### Before building comment or uncomment every docker files' since RPi architecture (arm64 ) is different from nomal PC/Laptop's architecutre.
#### Docker files are located with name "Dockerfile" in every folder(humble, noetic, bridge, )
If you have ROS2 installation on your system consider commenting ros2 serivce called humble from docker-compose file

```sh
cd ~Project/p3dx_docker
docker-compose -f arm64_compose.yaml up --build
```
Note that for the first time building it will take some time. Go and get your coeffee

If you don't build the ros2 service consider adding the sourcing to the envionment variable
```sh
echo "source/opt/jazzy/setup.bash">>~/.bashrc
echo "source~/Project/p3dx_ws/install/setup.bash">>~/.bashrc
```