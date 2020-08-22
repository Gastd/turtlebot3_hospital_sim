# Running the Simulation

To run the basic simulation run `morse run turtlebot_hospital_sim` after starting ros with `roscore`.

To run the ros navigation module you need to install the turtlebot3 and ros_nav packages from your distribution. Then you may append the current directory to your $ROS_PACKAGE_PATH and run it with `roslaunch morse_nav sim.launch`.

The ros navigation module is not needed for the robot/pose and robot/odom sensors.