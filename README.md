# ScrollySign
A few fun pieces of software to use with our MAX7219 LED Matrix Display.
Our display is available here for sale: https://inductivetwig.com/products/led-matrix-display


![ScrollyNews Demo](https://cdn.shopify.com/s/files/1/0925/9692/files/scrollynews_480x480.gif?v=1580860076)


# Hardware Requirements

* Arduino Uno: https://inductivetwig.com/products/arduino-uno-r3-with-atmega328p
* Our LED Matrix display product: https://inductivetwig.com/products/led-matrix-display
* Some jumper wire: https://inductivetwig.com/products/10cm-jumper-wire-120-pcs
* A power supply (to run independently): https://inductivetwig.com/products/ac-power-adapter

# Software Requirements

* LED Matrix Driver: https://github.com/bartoszbielawski/LEDMatrixDriver
* (If using python script): feedparser and pyserial -- available on pip

# Hookup Guide

To hook up to an Arduino Uno, just use the following pins. Be sure to connect up to the "IN" port, labeled on the back. 

1. Connect Pin 9 on Arduino to CS (Chip Select)
2. Connect Pin 11 (MOSI) on Arduino to	DIN (Data In)
3. Connect Pin 13 (SCK) on Arduino to	CLK (Clock)
4. Connect 5V (Power) on Arduino to VCC
5. Connect GND (Ground) on Arduino to GND

# Control ScrollySign From Serial Console

1. Program ScrollySign sketch to your Arduino
2. Verify that you see the "Waiting for Message" with two cat icons on either side
3. Open up the terminal
4. Set line termination to "none"
5. TURN ON YOUR CAPS LOCK KEY! The sketch only supports capitalized letters
6. Type in some text and hit enter

When the sign is done scrolling the current text, it will move on to the next. It also sends a # to indicate when the message completes, so you can time new messages to follow.

# Display an RSS Feed Using ScrollySign

1. Install the Arduino sofwtware as indicated above, taking note what serial port your Arduino Uno is showing up as
2. We assume you have installed Python, if not, please do so. Its pre-installed on mac and can be accessed via "Terminal"
3. Use pip (the Python package manager) to install the pyserial library. IE: pip install pyserial
4. Use pip (the PYthon package manager) to install the feedparser library. IE: pip install feedparser
4. Edit scrollynews.py and change serialport = "" to your serial port of choice. Ours showed up as /dev/tty.usbmodem145301
5. Type: python scrollynews.py

The script will reach out to a news RSS feed and show the top stories of each title.

# Displaying Any RSS Feed

Modify scrollynews.py above, and change rss_feed = "" to any other feed. If the feed supports titles, you will see the news scroll by.

# Making Your Own Internet Connected ScrollySign

You can modify our script to send text over the serial port to make your own signs. Show sweets, mentions, weather, time, or connect it to a web form! 

Our script waits for the "#" to appear (signals start of a new message) to load into the buffer a new message to follow. Take note that we do limit the serial transmission speed a little bit, as the Arduino Uno's CPU is quite heavily used. We found that without a serial delay, messages longer than 64 characters can become truncated or corrupted.

# Notes

Due to the way the fonts are configured, only upper case text is supported. You must send upper case letters for it to work. We replaced the * symbol with a Cat. If you want to create custom characters, check out this link here and replace the hex line for the character of interest: https://gurgleapps.com/tools/matrix
