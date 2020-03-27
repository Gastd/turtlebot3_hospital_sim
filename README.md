# turtlebot3_hospital_sim

## Overview

The purpose of this package is to simulate a group of three turtlebots 3 in a Hospital environment. 
This package was inspired by the tutorials from [ROBOTIS](http://robotis.com/) for [turtlebot3](http://emanual.robotis.com/docs/en/platform/turtlebot3/specifications/).
Each robot has a 360° lidar, two wheels and a camera and they can be controlled using the topic _/cmd_vel_ as any other mobile robot in ROS ([REP-105](https://www.ros.org/reps/rep-0105.html)).

The code in this package can be used either with **simulated robots** or with **real robots**:

<p float="left">
  <img src="/docs/gif1.gif" width="430" />
  <img src="/docs/gif2.gif" width="430" /> 
</p>

### License

The source code is released under a [MIT license](LICENSE).

**Author: Gabriel F P Araujo<br />
Affiliation: [LES](https://github.com/lesunb)<br />
Maintainer: [Gabriel F P Araujo](mailto:gabriel.fp.araujo@gmail.com)**

The turtlebot3_hospital_sim package has been tested under Ubuntu 18.04, [ROS Melodic](https://wiki.ros.org/melodic/Installation/Ubuntu) and Gazebo 9.
This is a research code, expect that it changes often and any fitness for a particular purpose is disclaimed.

<p float="center">
  <img src="/docs/gif-presentation.gif" width="860" />
</p>

<!-- [![Build Status](http://rsl-ci.ethz.ch/buildStatus/icon?job=ros_best_practices)](http://rsl-ci.ethz.ch/job/ros_best_practices/) -->

## Usage

Clone this repository to your catkin workspace.

```bash
cd ${YOUR_WORKSPACE_PATH}/src
git clone https://github.com/Gastd/turtlebot3_hospital_sim.git
cd ../
source devel/setup.bash
catkin_make
```


## Run the Simulation
The Simulation uses the well known Gazebo Simulator that is shipped with ROS.

#### Dependencies

* Before running the simulation, you must install the turtlebot3 packages.

    ```bash
    sudo apt install ros-melodic-turtlebot3-simulations ros-melodic-turtlebot3-bringup
    catkin_make
    ```

#### Running

Run the simulation to test the code:

* In a terminal with your ros workspace
    ```
    roslaunch turtlebot3_hospital_sim turtles_in_a_hospital.launch
    ```

This will open the Gazebo with the robots in position and ready to go.

## Youtube Video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=YcMHVNv3jME
" target="_blank"><img src="http://img.youtube.com/vi/YcMHVNv3jME/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="860" border="10" /></a>

### Navigation Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=tlY0Dh7u6Jk
" target="_blank"><img src="http://img.youtube.com/vi/tlY0Dh7u6Jk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="860" border="10" /></a>


## Some kind of Road map

In a hospital environment, many different robots with different capabilities can be used where they can reach some goals as a team without constraints. So a team with robots with or without manipulation, with or without mobility, can be built and simulated to reach cooperative goals.


## Bugs & Feature Requests

Please report bugs and request features using the [Issue Tracker](https://github.com/Gastd/turtlebot3_hospital_sim/issues).
