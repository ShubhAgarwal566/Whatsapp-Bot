from selenium import webdriver
import time

#+-+-+-+-+-+-+-+-+-+-+-+-+- GLOBAL DECLARATIONS +-+-+-+-+-+-+-+-+-
chat_name = ['Trial', 'Trial2']
message = 'Hi i am shubh'
count = 0
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
				print(e)
			time.sleep(1)
		chat.click()

	def sendMessage(self, name):
		global count
		chat = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
		chat.click()				
		chatBox = self.driver.find_element_by_xpath('//div[@class="_1Plpp"]')
		chatBox.send_keys(message+str(count))
		count+=1
		time.sleep(.5)
		sendButton = self.driver.find_element_by_xpath('//button[@class="_35EW6"]')
		sendButton.click()

	def quit(self):
		self.driver.quit()


bot = WhatsAppBot()
bot.login()

while True:
		try:
			for i in chat_name:
				bot.sendMessage(i)
				time.sleep(2)
		except Exception as e:
			print("\n------ERROR------\n")
			print(e)
