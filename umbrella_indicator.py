# DontGetMeWet
# The Umbrella Indicator
#
#
# Created by Rishabh Tewari on 7/03/16.
# Copyright © 2016 Rishabh Tewari. All rights reserved.
#

'''
    MIT License
    
    Copyright (c) [2016] [DontGetMeWet]
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    
    '''








'''


WARNING: ONLY WORKS ON THE RASPBERRY PI WITH AN LED
CONNECTION OF THE LED MUST BE ON BCM PIN 12 or normal pin 30 if counted

GROUND CONNECTION IS RECOMMENDED ON PIN 30 FROM COUNTING, ABOVE THE BCM PIN 12

BCM PIN                      PERCNTAGE
12                               30%+
21                               40%+
20                               50%+ 
16                               60%+
25                               70%+

This is the Umbrella Indicator
'''
#import required packages
import requests
from gpiozero import LED
import time
#setting up gpio pins
led1 = LED(12)
led2 = LED(21)
led3 = LED(20)
led4 = LED(16)
led5 = LED(25)

#setting Variables for API    
global key = 'ENTER YOUR KEY '    #Enter your API key supplied from the Weather underground Website
global ApiUrl = 'Enter the API URL ' #Enter your API URL supplied from the Weather underground Website
# Start Function
def getForecast():
    while True: #Loop forever
        r = requests.get(ApiUrl)
        forecast = r.json #get data in JSON format
        popValue = forecast['forecast']['txt_forecast']['forecastday'][0]['pop']
        popValue  = int(popValue) #change value into integer

        if popValue >= 30: #intergrating API with the gpio
            led1.on()
            print("30 percent plus chance of rain")
            if popValue >= 40:
                led2.on()
                print("40 percent plus chance of rain")
                if popValue >= 50:
                    led3.on()
                    print("50 percent plus chance of rain")
                    if popValue >= 60:
                        led4.on()
                        print("60 percent plus chance of rain")
                        if popValue >= 70:
                            led5.on()
                            print("70 percent or more chance of rain! An umbrella is a MUST!")


        print(popValue + "Percent chance of rain")
            time.sleep(180) #wait for 3 minutes to refresh feed

