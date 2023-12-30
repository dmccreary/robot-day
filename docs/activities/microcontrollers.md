# Robot Day Microcontroller Labs

![Microcontrollers Board](../img/microcontrollers.jpg)

In this activity, we are going to compare the last generation of microcontrollers with the current generation.  We are going
to find we can now build powerful robots that are inexpensive.

The last generation was called the [Arduino](https://store-usa.arduino.cc/collections/boards-modules/products/arduino-uno-rev3).  Its price was about $30.  The new generation is called the [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/).  It's price is only $4!.Let's compare the features of these two microcontrollers graphically.

## Memory Comparison

Memory is really important in computers.  The name of the
memory we use is called Random Access Memory or RAM. The more RAM you have, the better!  It means you can work on really fun problems without slowing down.

![](../img/memory-compare.png)

## Memory Usage

Now let's look at how we use this memory when we program graphic displays using MicroPython.

![](../img/memory-usage.png)

We can see that Python can't run on the old 2K Arduino Uno since it needs about 16K of RAM to run.

Using a framebuffer for a monochrome display is easy.  But powering a color smartwatch takes a LOT more memory.

## Clock Speed

Imagine you are running a race.  In a given amount of time, like one minute, a turtle will only go 16 feet.  But a rabbit could travel 133 feet.  This
is how we compare how quickly the old turtle Arduino compares with the
ultra-fast rabbit of the Raspberry Pi Pico.

![](../img/clock-speed.png)

## Microcontrollers on Breadboards

Most of our projects place a Raspberry Pi Pico directly on a breadboard.
The exception is when we use the Cytron Maker Pi RP2040 to drive our robots.

![](../img/microcontrollers-on-breadboards.jpeg)