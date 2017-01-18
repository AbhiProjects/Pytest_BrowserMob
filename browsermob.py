import browsermobproxy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

Location_Of_Browser_Mob_Proxy = 'browsermob-proxy-2.1.0-beta-5/bin/browsermob-proxy'
Location_Of_Chrome_Driver = ''
Test_Websiite = 'https://in.yahoo.com/?p=us'
WAIT_TIME = 5

def jsonWrite(FileName = 'Browsermob',Data = {}):
	'''
		Writes A JSON Object In Pretty Format In A Text File
		FileName : The File Name Of The Text File. Default Value = 'Browsermob'
		Data : The JSON Object To Be Written Into The Text File. Default Value = Empty Dictionary
		Returns : True If The Write Is Successful Else None
	'''
	try:
		f=open(FileName+'.txt','w')
		json.dump(Data,f,indent=4,sort_keys=True)
		f.close()
	except Exception, e:
		print 'JSON File Write Error'
		print 'Exception Occured:',e.__class__
		print 'Exception Message:', str(e)
	else:
		return True
	
def createWebDriver(Proxy,Location_Of_Chrome_Driver = None):
	'''
		Creates A Chrome Web Driver With Browser Mob Proxy
		Proxy : Browser Mob Proxy Object
		Location_Of_Chrome_Driver : Absolute Path Of The Selenium Chrome Browser. If Nothing Is Specified It Defaults To Current Working Directory
		Returns : Selenium Web Driver Object If The Web Driver Is Created Successfully Else None
	'''
	try:
		if Location_Of_Chrome_Driver == None:
			Location_Of_Chrome_Driver = os.getcwd() + '/chromedriver'
		
		Proxy_Options = webdriver.ChromeOptions()
		Proxy_Options.add_argument('--proxy-server={0}'.format(Proxy.proxy)) 
		Driver = webdriver.Chrome(Location_Of_Chrome_Driver,chrome_options = Proxy_Options) # Set Up Browser With Proxy Options 
		Driver.wait = WebDriverWait(Driver, WAIT_TIME)
	except Exception, e:
		print 'Create Web Driver Method'
		print 'Exception Occured:',e.__class__
		print 'Exception Message:', str(e)
	else:	
		return Driver

def closeWebDriver(Driver):
	'''
		Closes The Selenium Web Browser
		Driver : The Selenium Web Driver Object
	'''
	Driver.close()
	
def startProxyServer(Location_Of_Browser_Mob_Proxy = Location_Of_Browser_Mob_Proxy,Proxy_Server_Options = {}):
	'''
		Starts The Browser Mob Proxy Server
		Location_Of_Browser_Mob_Proxy : Absolute Path Of The Browser Mob Proxy Batch File
		Server_Options : Options For The Browser Mob Proxy Server Object
		Returns : Browser Mob Proxy Server Object If The Server Is Created Successfully Else None
	'''
	try:
		Server = browsermobproxy.Server(Location_Of_Browser_Mob_Proxy,Proxy_Server_Options)
		Server.start()
	except Exception, e:
		print 'Start Proxy Server Method'
		print 'Exception Occured:',e.__class__
		print 'Exception Message:', str(e)
	else:
		return Server
		
def closeProxyServer(Server):
	'''
		Closes Browser Mob Proxy Server
		Server : Browser Mob Proxy Server Object
	'''
	Server.stop()
	
def createProxy(Server):
	'''
		Creates A Proxy For The Client From The Browser Mob Proxy Server
		Server : Browser Mob Proxy Server Object
		Returns : Browser Mob Proxy Object If The Proxy Is Created Successfully Else None
	'''
	try:
		Proxy = Server.create_proxy()
	except Exception, e:
		print 'Create Proxy Method'
		print 'Exception Occured:',e.__class__
		print 'Exception Message:', str(e)
	else:
		return Proxy
	
def findWebElement(Driver,Type,Value):
	'''
		Find A Specific Web Driver Element By ID Or Tag Using A Specific Value
		Driver : The Selenium Web Driver Object
		Type : The Type Of Web Element Finder. The Type Can Either Be ID Or Tag
		Value : The Value Of The Tag
		Returns : The Web Element If Found Else None
	'''
	try:
		if Type == 'ID':
			Element = Driver.wait.until(EC.presence_of_element_located((By.ID, Value)))
		elif Type == 'Tag':
			Element = Driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, Value)))
		else:
			raise Exception('Type Passed Is Niether A ID Or A Tag Name')
	except Exception, e:
		print 'Find Web Element Method'
		print 'Type',Type
		print 'Exception Occured:',e.__class__
		print 'Exception Message:', str(e)
		return None
	else:	
		return Element

def main():
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy,{'legacy_mode':False}) 	# legcy_mode = True For Proxy With Legacy Implementation
	Proxy = createProxy(Server)												   		# legacy_mode = False For Proxy With Little Proxy Implementation
	Driver = createWebDriver(Proxy)
	Proxy.new_har(Test_Websiite) # Creates A New Network Data Gatherer Page
	
	Driver.get(Test_Websiite) # Opens The Test Website URL
	
	Web_Element_By_ID = findWebElement(Driver,'ID','UHSearchWeb')
	Web_Element_By_Tag = findWebElement(Driver,'Tag','title')
	
	if Web_Element_By_ID != None:
		print 'Text Content Of Search Button',Web_Element_By_ID.get_attribute('value')
		
	if 	Web_Element_By_Tag != None:
		print 'Text Content Of Title Tag',Web_Element_By_Tag.get_attribute('textContent')
	
	Network_Data = Proxy.har # Capatures The All Network Traffic Data
	
	if jsonWrite('Browsermob',Network_Data) == True: # Writes JSON Network Data To A Text File
		print 'Network Data Written To A Text File'
	
	closeProxyServer(Server)
	closeWebDriver(Driver)

# Invokes The Main Function	
if __name__=='__main__':
	main()	
