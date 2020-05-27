from selenium import webdriver
import time
from datetime import datetime
import random

#+-+-+-+-+-+-+-+-+-+-+-+-+- GLOBAL DECLARATIONS +-+-+-+-+-+-+-+-+-
chat_name = ['Trial','Trial2']
messages = ['Hello, Good Morning', 'I hope you have a good day', 'Good to be awake', 'Got up early today', 'How are you doing today?']
timeToSend = ['02:19 AM','02:21 AM']
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-++-+-+-+-

class WhatsAppBot():
	def __init__(self):
		self.driver = webdriver.Chrome()
	
	def login(self):
		self.driver.get('https://web.whatsapp.com/')
		print("Please scan QR Once")
		while True:
			try:
				chat = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(chat_name[0]))
				print('Scanning Successful')
				break
			except Exception as e:
				pass
			time.sleep(1)

	def searchChat(self, name):
			searchBox = self.driver.find_element_by_xpath('//label[@class="_2MSJr"]//div[@class="_2S1VP copyable-text selectable-text"]')
			searchBox.send_keys(name)
			time.sleep(1)

	def sendMessage(self, name):
		chat = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
		chat.click()				
		chatBox = self.driver.find_element_by_xpath('//div[@class="_1Plpp"]')
		chatBox.send_keys(random.choice(messages))
		time.sleep(1)
		sendButton = self.driver.find_element_by_xpath('//button[@class="_35EW6"]')
		sendButton.click()

	def quit(self):
		self.driver.quit()

bot = WhatsAppBot()
bot.login()

lock = 0
while True:
		try:
			if(datetime.now().strftime("%H:%M %p") in timeToSend and lock==0):
				lock = 1
				for i in chat_name:
					bot.searchChat(i)
					bot.sendMessage(i)
					time.sleep(2)
			elif(datetime.now().strftime("%H:%M %p") not in timeToSend):
				lock=0
			time.sleep(25)
		except Exception as e:
			print("\n------ERROR------\n")
			print(e)

