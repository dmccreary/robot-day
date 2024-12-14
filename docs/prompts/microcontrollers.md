# MicroControllers

![](../img/microcontrollers.jpg)

!!! prompt "Prompt Text"
    The image above is a board we are using in our "Robot Day" 
    to explain microcontrollers.  The centerpiece of robot day
    is a large robot corral full of about a dozen $19 collision
    avoidance robots built around the RP2040 microcontroller from
    the Raspberry Pi Foundation.  We want to get across the point
    the the new $4 Raspberry Pi Pico is a LOT more powerful then
    the old expensive $30 Arduino microcontrollers.  They all run
    MicroPython in our school's coding classes.

    Please generate a sample 5 minute dialog that a teacher/mentor/volunteer
    might have with an 8-year student that comes up to the table to
    talk about microcontrollers in our collision avoidance robots.

## Sample Dialog for 8-Year Old

**Teacher:** Hi there! I see you’re interested in our robot station. Do you know what a microcontroller is?

**Student:** Not really. What is a microcontroller?

**Teacher:** Great question! A microcontroller is like a tiny computer chip that can control things. It’s the brain of our robots—helping them move, avoid obstacles, and listen to instructions we write in code.

**Student:** So it’s like a mini computer?

**Teacher:** Exactly. Just like a big computer can run programs, these little chips run special programs that tell the robot when to go forward, when to turn, or when to stop so it doesn’t crash into things.

**Student:** Cool. Which one is inside the robot?

**Teacher:** We’re using one called the Raspberry Pi Pico. See this little green board here? That’s the Pico. It’s a lot smaller than the bigger blue boards we used to use called Arduinos, but it’s actually more powerful.

**Student:** More powerful than that big one? How?

**Teacher:** Well, the older Arduino boards—like the Arduino Uno—came out many years ago, and they were really good at the time. But the Raspberry Pi Pico came out more recently, in 2021, and technology has improved a lot since then. The Pico can run faster, handle more complex tasks, and store more data, even though it’s only about $4 compared to the Arduino Uno’s $30 price tag.

**Student:** So cheaper and more powerful?

**Teacher:** That’s right! The Pico can run at 133 megahertz, which means it can do a whole lot more instructions every second than the Arduino Uno, which runs at only 16 megahertz. Also, the Pico can run MicroPython—do you do any coding in your school?

**Student:** We have a coding class, and we learned a little bit of Python. Is that the same?

**Teacher:** Yes! MicroPython is like a smaller version of Python that these little devices can understand. Instead of a complicated language, you can write simple Python code to make your robot drive around and avoid bumping into walls.

**Student:** That sounds much easier!

**Teacher:** It is easier. And because MicroPython is similar to what you learn in class, you can write simple commands like “forward()” or “stop()” and the robot’s microcontroller will follow those instructions. It makes learning how to control robots a lot more fun.

**Student:** So the robot listens to the code I write, just like a program on my computer?

**Teacher:** Exactly. You write the code on a computer, send it to the robot’s microcontroller, and then it will remember it and follow what you said—driving around the corral, turning away from obstacles, and never crashing.

**Student:** That’s so cool! Can I try to see how it works?

**Teacher:** Sure! We have a sample code here that says “go straight until you see something in front, then turn left.” We can load this code into the Pico on the robot. When I place the robot in the corral, it will start moving forward. When its sensor notices a wall, it’ll turn left to avoid it. Let’s watch together.

**Student:** Wow, it did it! It turned by itself!

**Teacher:** Isn’t that great? All that is possible because the Raspberry Pi Pico is running the code you gave it. That’s the power of modern microcontrollers. They’re small, inexpensive, and easy to program with something you’re already learning—Python. By understanding how these tiny “robot brains” work, you can create your own inventions and solve problems in creative ways.

**Student:** I want to learn more and build my own robot!

**Teacher:** That’s the spirit! Keep practicing your coding, and soon you’ll be able to design your own robots and programs. Technology keeps improving, and the more you learn, the more you can do. Just remember, every big invention starts with small steps—just like the robots here.

## Sample Dialog with a 13-Year Old Student

**Teacher:** Hi there! Welcome to our robot station. I noticed you’re checking out our microcontrollers. Do you know much about how these little boards work inside the robot?

**Student (13-year-old):** I know a bit. They’re like small computers, right?

**Teacher:** Exactly. Microcontrollers are small, self-contained computers that handle all the robot’s logic—things like interpreting sensor data, making decisions, and controlling the motors. They don’t need a separate operating system like a laptop does; instead, they just run one program at a time.

**Student:** So these robots are using microcontrollers to move around and not crash into each other?

**Teacher:** That’s right. We’re using a newer microcontroller called the Raspberry Pi Pico. It’s relatively new and costs about $4, which is pretty amazing compared to older boards like the Arduino Uno that cost around $30.

**Student:** So the Pico is cheaper. Is it also better?

**Teacher:** In many ways, yes. The Raspberry Pi Pico runs at a much higher clock speed—about 133 MHz compared to the Arduino Uno’s 16 MHz. That means it can execute a lot more instructions per second. It also has more memory and can handle more complex tasks. Plus, it supports MicroPython, which makes programming more accessible if you’re familiar with Python from school.

**Student:** We’ve actually learned a bit of Python in our coding class. Is MicroPython just a smaller version of Python?

**Teacher:** Exactly. MicroPython is a streamlined version of Python that’s designed to run efficiently on microcontrollers. Instead of dealing with more complex languages like C or C++—which you’d typically use for Arduino—you can use a language that’s closer to what you’re learning now. It makes the coding part feel less intimidating and more direct.

**Student:** So I can use Python to tell the robot what to do, and the Pico will just run it?

**Teacher:** Yes! You write your Python code on a computer, upload it to the Pico, and then the Pico “remembers” the instructions. Whenever you power it on, it’ll run those instructions, controlling the motors and reading sensors—like the ultrasonic sensor that tells the robot when it’s close to an obstacle.

**Student:** Wait, so the Pico can handle inputs from sensors and then quickly adjust the robot’s movements in real-time?

**Teacher:** Exactly. That’s what makes a robot seem “smart.” The microcontroller constantly reads sensor data and uses the logic you’ve written to decide how to move next. With the Pico’s speed and memory, it can handle more sensors or more complex algorithms if you want.

**Student:** That sounds way more flexible than older boards. Is that why you’re using the Pico for these collision avoidance robots?

**Teacher:** Yes. The Pico’s flexibility, cost-effectiveness, and Python support make it ideal for teaching. It’s powerful enough for advanced projects, yet simple enough for beginners to dive in. And the fact that it’s cheaper means we can have more robots for students to experiment with.

**Student:** That’s really cool. I guess with Arduino, you had to know C/C++ and deal with a slower processor?

**Teacher:** Right, and Arduino boards often have more limited RAM. The Arduino Uno has only a couple kilobytes of RAM, while the Pico has around 264 kilobytes. That doesn’t sound huge compared to a laptop, but it’s a big difference in the microcontroller world. More memory means more complex logic and bigger programs you can run.

**Student:** So basically, these Pico-powered robots are more cost-effective and more powerful, and they’re easier to program because I can use Python. That’s a huge advantage.

**Teacher:** You’ve got it. Technology has progressed, and these newer microcontrollers let us do more, teach more, and learn more at a lower cost. It means you can spend your time being creative and experimenting with code, instead of fighting with old limitations.

**Student:** That makes me want to try coding something for these robots. Maybe I can write a program that makes the robot zigzag around or follow a line.

**Teacher:** That’s a great idea. You could start by writing a simple loop in MicroPython that reads a sensor and adjusts the motor speeds. Before you know it, you’ll be implementing more advanced features like pathfinding or pattern recognition. The possibilities are open to whatever you can imagine.

**Student:** Thanks for explaining all this. I feel more confident now. I’m excited to try something with the Pico.

**Teacher:** Anytime. Your understanding of the tools you’re using will help you become a more creative and capable engineer or programmer. Feel free to come back with any questions as you get started!
















