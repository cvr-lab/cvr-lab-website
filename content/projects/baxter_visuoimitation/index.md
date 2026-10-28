---
title: Visuoimitation - Baxter imitates movements looking at an operator
summary: The objective of the system is to control a baxter robot using the kinect V2 and tis body structure extraction modules (body tracking) under the ROS (Robot Operating System) framework. Modules will be developed to make an interface between the robot and the Kinect body pose estimation so that the robot can imitate the movements of the operator in real time
date: '2018-04-27T00:00:00Z'
tags:
- Robotics
- Baxter
- Object classification
authors:
- Francisco Barranco
links:
- type: code
  url: https://github.com/cvr-lab/Visual-Imitation
  label: Code
  icon: brands/github
image:
  caption: ''
  focal_point: Smart
---

 The objective of the system is to control a baxter robot using the kinect V2 and tis body structure extraction modules (body tracking) under the ROS (Robot Operating System) framework. Modules will be developed to make an interface between the robot and the Kinect body pose estimation so that the robot can imitate the movements of the operator in real time. The system is developed in Ubuntu through the use of libraries usch as libfreenect2, openNI-2, and NITE2 becasue the ROS framework is developed for Ubuntu. 
 
## Installation
The project has been tested with the 14.04 STL Ubuntu distribution. Also, for the current project ROS indigo was installed. In case you need to install this ROS version, you need first:

Configure the source.list file
    
    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu \$ (lsb\_release -sc) main"> /etc/apt/sources.list.d/ros-latest.list'

Configure the keys
    
    $ sudo apt-key adv --keyserver hkp: //ha.pool.sks-keyservers.net: 80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

Installation
    
    $ sudo apt-get update sudo apt-get install ros-indigo-desktop-full

Before using ROS, update rosdep to install all the required dependencies
    
    $ sudo rosdep init
    $ rosdep update

Configure the environment for compilation
    
    $ echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
    $ source ~/.bashrc

Installing Gazebo for simulation: First we decided to use catkin
    
    $ mkdir -p ~/catkin_ws/src
    $ cd ~/catkin_ws/src
    $ catkin_init_workspace
    $ cd ~/catkin_ws
    $ catkin_make

Configure the environment
    
    $ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

Install Gazebo
    
    $ sudo apt-get install -y gazebo2

Donwload all the code for ROS indigo ad build Gazebo
    
    $ cd ~/catkin_ws/src
    $ git clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b indigo-devel
    $ cd ~/catkin_ws/
    $ catkin_make

Install the Baxter package to use it with the simulator now
    
    $ cd ~/ros_ws/src
    $ wstool init .
    $ wstool merge https://raw.githubusercontent.com/RethinkRobotics/
    $ baxter_simulator/master/baxter_simulator.rosinstall
    $ wstool update

Compile the package
    
    $ source /opt/ros/indigo/setup.bash
    $ cd ~/ros_ws
    $ catkin_make

Run Baxter for the simulator
    
    $ roslaunch baxter_gazebo baxter_world.launch****
   


## Workstation Setup
The required steps to setup your workstation are described in the tutorial from rethink robotics®. This include the installation of Ubuntu, ROS, the Baxter SDK and the first connection to the robot. The direct connection from the Baxter to your workstation also requires a [network connection from the type Ethernet](http://sdk.rethinkrobotics.com/wiki/Workstation_Setup).
        
        Example: Network Connection->Add->Ethernet
        Connection name: Baxter
        IPv4 Settings: Method: Manual
        Address: 169.254.0.10, Netmask: 255.255.0.0, Gateway: 0.0.0.0
        
        
## Gazebo (optional)

Gazebo is a powerful simulation tool for robots. It allows to use already existing robots like the Baxter or to create own one. It is very useful for people who have not the possibility to work with a physical robot. [Check the Gazebo instructions](http://sdk.rethinkrobotics.com/wiki/Using_Gazebo_and_Baxter).

It is more comfortable to have a separate workspace for the physical robot and the visual one in the simulation. It is for example not necessary to change everytime the baxter.sh file. The tutorial from the [github repository zengzhen](https://github.com/zengzhen/zhen_baxter_moveit) explains the steps and it is a good way to get in touch with gazebo.
        
If MoveIt is already installed the packages must be copied from the workspace ros_ws in the src folder from ros_gazebo_master. But to use the simulation from this website don't modify the following line from baxter_world.launch.

        <arg name="world_name" value="$(find baxter_gazebo)/worlds/baxter.world"/>

## Robot arm calibration

The calibration of the arms is recommended to get precisely results. There are two different calibration routines which are very well described on the website from rethink robotics. [Check the instructions from Rethink Robotics](http://sdk.rethinkrobotics.com/wiki/Arm_Calibration).
        

## Examples and code

The main objective of the project is described in the initial section of this page. The following videos show first and example of the setup with the code running, and the Baxter simulation in Gazebo imitating the movements of the operator. The next video shows a successful example of the robot imitating the operator movements. 

{{< youtube KZcqivsb1dM >}}

 The next video shows a successful example of the robot imitating the operator movements. 
 
 {{< youtube V6VbvJ-t0vg >}}


## Contact

Granada
Cristina Garrido
tinamay299@gmail.com
