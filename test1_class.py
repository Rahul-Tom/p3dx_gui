from PyQt5 import QtWidgets

from test1 import Ui_MainWindow

import os
import sys
import time
import threading
import subprocess

class ButtonDefinition(Ui_MainWindow):
    def _init_(self):
        super().__init__()
        self.exportNum=0
        self.extractNum=0


    def init(self):
        self.init__control_panel()
    # Initially hide the horizontal layout widget
        self.horizontalLayoutWidget.hide()
        self.horizontalLayoutWidget_2.hide()
        self.lineEdit.hide()
        self.label.setText(f"Please Connect to Robot and wait for 30 seconds..")
        self.pushButton_StartStopRecord.hide()
        self.is_recording = False
        self.bag_file_name = "default_bag"

    def init__control_panel(self):
        self.pushButton_ConnectToRobot.clicked.connect(self.pushButton_ConnectToRobot_action)
        self.pushButton_RQt.clicked.connect(self.pushButton_RQt_action)
        self.pushButton_Rviz2.clicked.connect(self.pushButton_Rviz2_action)
        self.pushButton_Record.clicked.connect(self.pushButton_Record_action)
        self.pushButton_Autonomous.clicked.connect(self.pushButton_Autonomous_action)
        self.pushButton_JoyControl.clicked.connect(self.pushButton_JoyControl_action)
        self.pushButton_NewMap.clicked.connect(self.pushButton_NewMap_action)
        self.pushButton_withMap.clicked.connect(self.pushButton_withMap_action)
        self.pushButton_StartStopRecord.clicked.connect(self.pushButton_StartStopRecord_action)
    
    
    def pushButton_ConnectToRobot_action(self):
        cmd = "xhost + && ../../Docker/run.sh"
        self.execCommand(cmd)
        self.startDelayThread()
        # self.label.setText(f"P3DX is ready for the adventure")
    
    def pushButton_RQt_action(self):
        cmd="source /opt/ros/humble/setup.bash && rqt"
        self.execCommand(cmd)
        self.label.setText(f"RQt is started")    

    def pushButton_Rviz2_action(self):
        cmd = "ros2 run rviz2 rviz2"
        self.execCommand(cmd)
        self.label.setText(f"Rviz is running:")

    def pushButton_Record_action(self):
        self.lineEdit.show()
        self.pushButton_StartStopRecord.show()
        self.label.setText(f"Type the bag name here without any extension ->")
        # self.execCommand(cmd)
        

    def pushButton_Autonomous_action(self):
        self.horizontalLayoutWidget_2.show()
        # self.pushButton_JoyControl.hide()
        

    def pushButton_JoyControl_action(self):
        cmd = "source /opt/ros/humble/setup.bash && ros2 run teleop_twist_joy teleop_node --ros-args -r cmd_vel:=RosAria/cmd_vel"
        self.execCommand(cmd) 
        self.label.setText(f"Press and hold R1 and left control button to navigate")

    def pushButton_NewMap_action(self):
        self.lineEdit.show()
        
        self.label.setText(f"Mapping started. Save the map ....")
        pass

    def pushButton_withMap_action(self):
        self.label.setText(f"Use Rviz to navigate..")
        pass

    def pushButton_StartStopRecord_action(self):
        self.pushButton_Record.clicked.connect(self.toggle_recording)

    # Method to show the horizontal layout when pushButton_Record is clicked
    def showHorizontalLayout(self):
        self.horizontalLayout.show()
    
    # Function to run the delay using threading
    def startDelayThread(self):
        # Create a separate thread for the delay function
        thread = threading.Thread(target=self.delayAndShow)
        thread.start()
        # self.label.setText(f"P3DX is ready for the adventure")
    # Function that delays for 30 seconds and shows the horizontal layout
    def delayAndShow(self):
        time.sleep(2)  # 30-second delay
        self.horizontalLayoutWidget.show()
        self.label.setText(f"P3-DX is ready for the adventure")

    
    def toggle_recording(self):
        if self.is_recording==True:
            # Stop recording
            self.stop_recording()
        else:
            # Start recording
            self.start_recording()

    def start_recording(self):
        self.is_recording = True
        self.pushButton_Record.setText("Stop Recording")
        self.label.setText(f"Recording started")
        bag_file_name = self.lineEdit.text().strip()
        if bag_file_name:
            # Record bag file command
            cmd = f"ros2 bag record -o -a {bag_file_name}"
            self.execCommand(cmd)
        else:
            print("Please enter a valid name for the bag file.")

    def stop_recording(self):
        self.is_recording = False
        self.pushButton_Record.setText("Start Recording")
        self.label.setText(f"Recording stoped")
        # Send the command to stop the ROS bag record
        # You may need to use a specific command to stop recording based on your setup
        print("Recording stopped.")    
    ##executation method
    def execCommand(self, cmd: str):
        cmd_base_head = "gnome-terminal -- bash -c '"
        cmd_base_tail = "'&"
        cmd_full =   cmd_base_head + cmd + cmd_base_tail  

        print(f"#COMMAND: {cmd_full}")
        os.system(cmd_full)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ButtonDefinition()
    ui.setupUi(MainWindow)
    ui.init()
    MainWindow.show()
    sys.exit(app.exec_())