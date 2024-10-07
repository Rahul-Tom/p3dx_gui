from PyQt5 import QtCore, QtGui, QtWidgets

from pop_up1 import Ui_MainWindow

import os
import sys
import time
import subprocess

class ButtonDefinition(Ui_MainWindow):
    def _init_(self):
        super().__init__()
        self.exportNum=0
        self.extractNum=0


    def init(self):
        self.init__window()

    def execCommand(self, cmd: str):
        cmd_base_head = "gnome-terminal -- bash -c '"
        cmd_base_tail = "'&"
        cmd_full =   cmd_base_head + cmd + cmd_base_tail  

        print(f"#COMMAND: {cmd_full}")
        os.system(cmd_full)

    # def run_ros2_node(cmd):
    # # Construct the ros2 run command
    #     command = ["ros2", "run", "PACKAGE_NAME", "NODE_NAME"]

    # # Run the command and capture the output
    #     try:
    #         subprocess.run(command, check=True)
    #     except subprocess.CalledProcessError as e:
    #         print(f"Error occurred: {e}")    

    def init__window(self):
        # self.pushButton_ConnectToRobot.clicked.connect(self.pushButton_ConnectToRobot_action)
        self.pushButton_JoyStickControl.clicked.connect(self.pushButton_JoyStickControl_action)
        self.pushButton_AutoNavig.clicked.connect(self.pushButton_AutoNavig_action)

        

    def pushButton_JoyStickControl_action(self):
        cmd = "source /opt/ros/humble/setup.bash && ros2 run teleop_twist_joy teleop_node --ros-args -r cmd_vel:=RosAria/cmd_vel"
        self.execCommand(cmd)   

    def pushButton_AutoNavig_action(self):
        cmd = "ros2 run rviz2 rviz2"
        self.execCommand(cmd)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ButtonDefinition()
    ui.setupUi(MainWindow)
    ui.init()
    MainWindow.show()
    sys.exit(app.exec_())