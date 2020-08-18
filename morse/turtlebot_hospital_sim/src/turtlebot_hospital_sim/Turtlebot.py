from morse.builder import *


PATH = "/".join(__file__.split("/")[:-3])


class Turtlebot(Robot):
    def __init__(self, name="turtlebot", path=f"{PATH}/models/turtlebot.blend"):
        Robot.__init__(self, path, name)
        self.name = name
        self.path = path

    def add_to_simulation(self, x=-19, y=-3, z=0,
                          x_rot=0, y_rot=0, z_rot=0):
        self.rotate(x_rot, y_rot, z_rot)
        self.add_motion_sensor()
        self.add_pose_sensor()
        self.add_lidar_sensor()

    def add_lidar_sensor(self):
        self.lidar = Hokuyo()
        self.append(self.lidar)
        self.lidar.properties(Visible_arc = False)
        self.lidar.properties(laser_range = 30.0)
        self.lidar.properties(resolution = 1.0)
        self.lidar.properties(scan_window = 180.0)
        self.lidar.create_laser_arc()
        self.lidar.add_interface('ros', topic=f"{self.name}/lidar")

    def add_motion_sensor(self):
        self.motion = MotionVW()
        self.append(self.motion)
        self.motion.add_interface('ros', topic=f"{self.name}/cmd_vel")

    def add_pose_sensor(self):
        self.pose = Pose()
        self.append(self.pose)
        self.pose.add_interface('ros', topic=f"{self.name}/pose")
