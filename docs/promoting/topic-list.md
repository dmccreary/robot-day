# Robotics Day Topics List

## Hands-On Lab Topics for Collision Avoidance Robotics Class

Using the Cytron Maker Pi RP2040 board, here's a list of hands-on lab activities that focus on practical experiments and projects:

1. **Robot Chassis Assembly:** Hands-on experience in assembling a basic robot chassis.  Parts include motors, batteries, controller boards and sensors.
2. **Robot Chassis Design Tradeoffs:** What are the pros
and cons of placing the battery pack on the bottom of the
robot?  What if you want to add a breadboard or
display to the top of the robot in the future?
3. **Grove Connectors:** Learn about how Grove connectors
allow you to connect sensors to the Cytron board
without the need for soldering.
4. **Motor Connection Testing:** Use the buttons on
the Cytron board to test the motor connections.  Does
each wheel go both forward and reverse?
5. **Thonny Desktop Setup:** Learn how to download
and install Thonny on different platforms such as
Windows, Mac and Linux.
6. **Run Python in Thonny:** Run Python locally on
your desktop.  Show how you write code, run
the code and save the code into your workspace.
7. **Checkout Code from GitHub:** Learn to install
GitHub and run the git clone program from a terminal or command line shell window.
8. **Run MicroPython on the RP2040:** Learn how
to run MicroPython code on the Cytron microcontroller.
9. **Blink Onboard LED:** Blink one of the on-board blue LEDs.  Create a list of the LED pins and light them all up.
10. **Turn NeoPixels Colors:** Write a program to turn
the first NeoPixel red, green and blue.  Change the
relative brightness of the three colors.
11. **DC Motor Control:** Turn motors on or off.
Change motor direction.
12. **Change Motor Speed:**  Learn to use the PWM
library to control the motor speed.  Discover the
minimum power needed to turn a motor.
13. **MicroPython External Libraries:** Learn how to create the /lib folder on the RP2040 and load a library such as the
library for the time-of-flight sensor.
14. **I2C Bus Scanner:** How can you tell if your sensor is talking to the microcontroller?  The I2C scanner program can help.
15. **Sensor Data Collection:** Gathering and analyzing data from the time-of-flight distance sensor.
16. **Time of Flight Sensor Calibration:**  The raw data from the time-of-flight sensor is uncalibrated.  How do we calculate the distance in centimeters or inches?
17. **Time of Flight Range:**  How far away can the time-of-flight sensor detect objects?  What about objects that are near to robot?
18. **Time of Flight Alignment:** What happens if the sensor is pointed too far down?  What is the ideal angle for detecting objects in a robot corral?
19. **NeoPixel Programming Workshop:** Creating custom light patterns with NeoPixels.
20. **Sound Generation with MicroPython:** Write programs to display different sounds through the onboard speaker.
21. **Designing a Collision Avoidance System:** Building and programming a basic collision avoidance system.  Learn about backing up and turning.
22. **Distance Threshold:** Adjust the distance the robot
backs up and turns around.  Try different values of this parameter.
23. **Tuning Collision Avoidance Parameters:** Experimenting with different settings to optimize performance.  Adjust the speed, distance and turning time.
24.  **Randomizing Turn Direction:** Add code that
allows the robot to randomly turn right or left.
25.  **Logging Turn Events:** Add code that writes a log
file of turning events.  Upload this data to the host
computer and analyze the data.
26. **Battery Management and Monitoring:** Learning about power supply and battery management in robotics.  Study
the current draw on the motors at different speeds.
27.  **Battery Life Estimation:** Given a new set of
batteries, how long would the robot work under different
conditions?  How does the speed impact the time a robot
will last?
28. **Obstacle Detection and Navigation:** Programming the robot to navigate through a course with obstacles.  How can
our robot turn and decide if a right or left turn is better?
29. **Simple Mapping Techniques:** Introduction to basic mapping using sensor data.  What are the limitations of
the robot's ability to sense its direction?
30. **Using Buttons:**  The Cytron board includes two user-programmable momentary push buttons.  Add code to read the buttons and change
the speed of the robot.
31. **Playing Sound Files:** Play prerecorded sound files using the speaker.
31. **Robot Debugging:** Troubleshooting and fixing issues in the collision avoidance robot.

## Display Robot

These activities assume that the base robot kit has a 128x64 OLED display
added to it.

1. **Adding a Display:** Adding an OLED display to the robot.  Understand
the way that power, ground and the five data signals are used.
2. **Displaying the Robot State:** Display the basic state of the
robot on the screen including distance senor data and power.
22. **Building a User Interface:** Creating a basic UI for robot control.


