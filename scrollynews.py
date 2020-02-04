# scrollynews.py
# InductiveTwig.com
# Displays an RSS news feed, defaults to CNN's RSS

# Configuration

serialport = "/dev/tty.usbmodem145301"  # Change this to your serial port
rss_feed = "http://rss.cnn.com/rss/cnn_topstories.rss" # Change to your news source

# Import required modules

import serial
import feedparser 
import time


ser = serial.Serial(port=serialport,baudrate=9600)

ser.isOpen()
ser.flushInput()

while 1==1:
  NewsFeed = feedparser.parse(rss_feed)
  ser.flushInput()
  while 1==1:
        a = ser.read(1)
        if a == "#": break
  for i in range(0,len(NewsFeed.entries)):
     entry = NewsFeed.entries[i]
     print entry.title
     ascii = entry.title.encode("ascii").upper()
     if len(ascii) > 60:					# if a long message, put in a delay so the serial buffer doesnt lose data
           for i in range(0,len(ascii)):
                ser.write(ascii[i])
                time.sleep(0.01)
     else:
           ser.write(ascii)
     while 1==1:
        a = ser.read(1)
        if a == "#": break

