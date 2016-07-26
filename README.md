# DontGetMeWet
DontGetmeWet is a Python based program under the MIT to work on the Raspberry Pi platform telling the chances of rain on a particular day.

It runs only on the Raspberry Pi platform and requires 'Requests' module and the GPIOZero Module to run.

DEPENDENCIES:


1.GPIOZERO Moule


2.Requests Module


3.Time Module

Hardware Requirements :

1.Raspberry Pi(Any version will suffice but the code is specially meant for Raspbery Pi 2 and 3, if you're using some other Pi make sure to change GPIO pin values)

2.Breadboard and Jumper Wires for Prototyping.

3.A few LED's

4.Resistors

5.PCB, Soldering equipment and wires, enclosure(OPTIONAL)

Other Requirements:

1.Internet Connection


Instructions:
1 . Open the umbrella_indicator.py file and enter your API keys obtained from the Weather Underground Website and the website URL obtained from the website on the lines which instruct you to do so, look for the comments.

2. Connect LED's to resistors and connect them to GPIO pins 12, 21, 20, 16, 25 respectively via a common ground pin(ONLY FOR RPi 2 AND 3)

3.Start the umbrella_indicator.py file by running 'python umbrella_indicator.py' .


4. Set Up the enclosures if you want, and make changes to the code, have a few pull requests to make it even better, Check out my YouTube Channel-> https://www.youtube.com/channel/UCQPD8xK8uJwLaBjP2hp3qUg 
for updates and feel free to ask any questions!

Suggestions :

1.It updates the feed every 30 seconds, feel free to change the time limit


2.Add more features to this.


Enjoy!
