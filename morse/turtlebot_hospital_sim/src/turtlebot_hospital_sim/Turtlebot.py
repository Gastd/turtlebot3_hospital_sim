from morse.builder import *


PATH = "/".join(__file__.split("/")[:-3])


class Turtlebot(Robot):
    def __init__(self, name="turtlebot", path=f"{PATH}/models/turtlebot.blend"):
        Robot.__init__(self, path, name)
        self.name = name
        self.path = path

    def add_to_simulation(self, x=-19, y=-3, z=0,
                          x_rot=0, y_rot=0, z_rot=0):
        self.translate(x, y, z)
        self.rotate(x_rot, y_rot, z_rot)
        self.add_motion_sensor()
        self.add_pose_sensor()

    def add_motion_sensor(self):
        self.motion = MotionVW()
        self.append(self.motion)
        self.motion.add_interface('ros', topic=f"/cmd_vel_{self.name}")

    def add_pose_sensor(self):
        self.pose = Pose()
        self.append(self.pose)
        self.pose.add_interface('ros', topic=f"/pose_{self.name}")
