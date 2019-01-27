# AR_DRONE_ROS_GUI
#
Primer Proyecto con GitHub
prueba de GitHub para poder suber los codigos desarrollados
Esto es un tutorial

## Prerequisites
* Operation System
  * Ubuntu 16.04
  
* Middleware 
  * [ROS](http://wiki.ros.org/kinetic/Installation/Ubuntu) (Kinetic)

This package depends on:
* [ardrone_autonomy package](https://github.com/AutonomyLab/ardrone_autonomy)
* [tum_simulator](https://github.com/eborghi10/AR.Drone-ROS)
* [GAZEBO](http://gazebosim.org/) (Version 7.0 If you install ROS Desktop-Full(Recommended) GAZEBO will be automatically installed.) 

## Getting started

Make sure ROS and GAZEBO are correctly installed

1. Create a workspace for the simulator

```
$ mkdir -p ~/drone_simulation_ws/src
$ cd ~/drone_simulation_ws/src
$ catkin_init_workspace
```

2. Download dependencies

```
$ git clone  https://github.com/AutonomyLab/ardrone_autonomy          # AR. Drone ROS Driver
$ git clone  https://github.com/eborghi10/AR.Drone-ROS                # Tum Simulator ROS Driver
$ cd ..
$ rosdep install --from-paths src --ignore-src --rosdistro kinetic -y

```

3. Built the simulator

```
$ catkin_make 

```

4. Source the environment 

```
$ source devel/setup.bash

```

To check that everything has been installed correctly

```
$ roslaunch cvg_sim_gazebo ardrone_testworld.launch

```

If everything went well, you should see something like this.
![](https://github.com/dvalenciar/AR_Drone_ROS_GUI/blob/master/pics/pic_1.jpg)


## GUI AR.Drone
Time to fly your drone!!!. To take off, landing, and move the  AR.Drone is necessary to publish the respectively topics, such as: 

* Take off
 ```
  $ rostopic pub -1 /ardrone/takeoff std_msgs/Empty
  ```
 * Land 
  ```
  $ rostopic pub -1 /ardrone/land std_msgs/Empty
  ```
 * Fly forward
 ```
 $ rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
 ```

However, this can be a bit confusing sometimes. Instead of publishing each topic, we have designed a GUI graphic interface that will allow you to operate the drone in a much easier way. In addition, you can see information related to the drone such as the  altitude, position, etc.

In order to use the GUI, all you need to do is:

1. Download and install the package in your workspace

```
$ cd ~/drone_simulation_ws/src
$ git clone https://github.com/dvalenciar/AR_Drone_ROS_GUI.git
$ cd ..
$ catkin_make 
```

2. Source the environment 
```
$ source devel/setup.bash
```

3. Run the GUI node
```
$ rosrun graphic_interface Graphical_Interf.py
```


you should see a window like this. 

![](https://github.com/dvalenciar/AR_Drone_ROS_GUI/blob/master/pics/pic_2.png)

That's it, now you can fly your AR.Drone in Gazebo and ROS
