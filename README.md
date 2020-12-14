## $5 Tech Unlocked 2021!
[Buy and download this Book for only $5 on PacktPub.com](https://www.packtpub.com/product/python-programming-with-raspberry-pi/9781786467577)
-----
*If you have read this book, please leave a review on [Amazon.com](https://www.amazon.com/gp/product/1786467577).     Potential readers can then use your unbiased opinion to help them make purchase decisions. Thank you. The $5 campaign         runs from __December 15th 2020__ to __January 13th 2021.__*

# Python Programming with Raspberry Pi
This is the code repository for [Python Programming with Raspberry Pi](https://www.packtpub.com/hardware-and-creative/python-programming-raspberry-pi-zero?utm_source=github&utm_medium=repository&utm_content=9781786467577), published by Packt. It contains all the supporting project files necessary to work through the book from start to finish.

## About the Book
Raspberry Pi Zero is a super-small and super-affordable product from Raspberry Pi that is packed with a plethora of features and has grabbed the notice of programmers, especially those who use Python.

This step-by-step guide will get you developing practical applications in Python using a Raspberry Pi Zero. It will become a valuable resource as you learn the essential details of interfacing sensors and actuators to a Raspberry Pi, as well as acquiring and displaying data.

You will get started by writing a Python program that blinks an LED at 1-second intervals. Then you will learn to write simple logic to execute tasks based upon sensor data (for example, to control a motor) and retrieve data from the web (such as to check e-mails to provide a visual alert). Finally, you will learn to build a home automation system with Python where different appliances are controlled using the Raspberry Pi.

The examples discussed in each chapter of this book culminate in a project that help improve the quality of people’s lives.

## Instructions and Navigations
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter5


The code will look like the following:

       
         static int ngpios;
       
         static int gpios[2] = { -1 , -1 };
       
         module_param_array(gpios, int, &ngpios, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
       
       
         MODULE_PARM_DESC(gpios, "Defines the GPIOs number to be used as a list of"
       
                          " numbers separated by commas.");

         /* Logging stuff */
       
         #define __message(level, fmt, args...)                                  \
       
                         printk(level "%s: " fmt "\n" , NAME , ## args)


There are no code files for the following chapters:

- **Chapter 1**  - Getting Started with Python and the Raspberry Pi Zero
- **Chapter 2**  - Arithmetic Operations, Loops, and Blinky Lights
- **Chapter 3**  - Conditional Statements, Functions, and Lists
- **Chapter 4**  - Communication Interfaces
- **Chapter 5**  - Data Types and Object-Oriented Programming in Python

### Software and hardware requirements:

Chapter 1:

Software: Python 3.x, IDLE3, SD Formatter (Windows), Raspbian OS (latest version)
Hardware: Raspberry Pi Zero with headers soldered, Keyboard, mouse, display cables etc.

Chapter 2:

Software:Raspbian OS installed on the software etc, Python3.x, IDLE3 (Comes installed by default).
Hardware:Raspberry Pi Zero with headers soldered, resistors, Red LED, Powerswitchtail ii (optional:http://www.powerswitchtail.com/Pages/default.aspx)

Chapter 3:

Software: Raspbian OS installed on the software etc, Python3.x, IDLE3 (Comes installed by default).
Hardware: Tactile push buttons (https://www.adafruit.com/products/1400), Motor control board of your choice (https://www.pololu.com/product/2753), DC motors of your choice.

Chapter 11:
Software: (On a Windows environment): Putty (http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), WinSCP (https://winscp.net/eng/download.php), git for windows, text editor like Notepad++ etc.


## Related Products:

* [Python Machine Learning]( https://www.packtpub.com/big-data-and-business-intelligence/python-machine-learning?utm_source=github&utm_medium=repository&utm_content=9781783555130 )

* [Python Data Analysis]( https://www.packtpub.com/big-data-and-business-intelligence/python-data-analysis?utm_source=github&utm_medium=repository&utm_content=9781783553358 )

* [Python Design Patterns [Video]]( https://www.packtpub.com/application-development/python-design-patterns-video?utm_source=github&utm_medium=repository&utm_content=9781786460677 )

* [Python: Penetration Testing for Developers]( https://www.packtpub.com/networking-and-servers/python-penetration-testing-developers?utm_source=github&utm_medium=repository&utm_content=9781787128187 )

### Suggestions and Feedback
[Click here]( https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform ) if you have any feedback or suggestions.


