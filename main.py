from selenium import webdriver
import time
from datetime import datetime
import random

#+-+-+-+-+-+-+-+-+-+-+-+-+- GLOBAL DECLARATIONS +-+-+-+-+-+-+-+-+-
chat_name = ['Trial','Trial2']  #names of people you want to send the message to
messages = ['Hello, Good Morning',
			'I hope you have a good day',
			'Good to be awake',
			'Got up early today',
			'How are you doing today?'] #list of messages you want to send
timeToSend = ['06:00 AM','06:30 AM'] #list of times you want the message to be sent
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-++-+-+-+-

class WhatsAppBot():
	def __init__(self):
		#initialize the driver and open chrome
		self.driver = webdriver.Chrome()
	
	def login(self):
		#open the web.whatsapp website
		self.driver.get('https://web.whatsapp.com/')
		print("Please scan QR Once")
		#wait until the user scans the QR code
		while True:
			try:
				searchBox = self.driver.find_element_by_xpath('//label[@class="_2MSJr"]//div[@class="_2S1VP copyable-text selectable-text"]')
				print('Scanning Successful')
				#if search box is available then the user has Successfully scanned the QR so break 
				break
			except Exception as e:
				pass
			#check if the search box is available, every 1 second
			time.sleep(1)

	def searchChat(self, name):
			#get the search box
			searchBox = self.driver.find_element_by_xpath('//label[@class="_2MSJr"]//div[@class="_2S1VP copyable-text selectable-text"]')
			#type in the required person's name
			searchBox.send_keys(name)
			#wait for 1 second to make sure everything renders properly
			time.sleep(1)

	def sendMessage(self, name):
		#look for the required chat name
		chat = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
		#click on the particular chat
		chat.click()
		#select the typing area/ chat box				
		chatBox = self.driver.find_element_by_xpath('//div[@class="_1Plpp"]')
		#type in the required message
		chatBox.send_keys(random.choice(messages))
		#wait for 1 second to make sure that the send button renders
		time.sleep(1)
		#search the send button
		sendButton = self.driver.find_element_by_xpath('//button[@class="_35EW6"]')
		#click the send button
		sendButton.click()

	def quit(self):
		self.driver.quit()

#make class object
bot = WhatsAppBot()
bot.login()

#lock variable will ensure that message is sent only once per alarm time(timeToSend) 
lock = 0
while True:
		try:
			#if the current time is in alarm time then send
			if(datetime.now().strftime("%H:%M %p") in timeToSend and lock==0):
				lock = 1
				for i in chat_name:
					bot.searchChat(i)
					bot.sendMessage(i)
					time.sleep(2)
			#if current time is not in alarm time then release the lock
			elif(datetime.now().strftime("%H:%M %p") not in timeToSend):
				lock=0
			#check every 25 seconds if current time matches alarm time
			time.sleep(25)
		except Exception as e:
			print("\n------ERROR------\n")
			print(e)

