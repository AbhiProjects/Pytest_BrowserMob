from browsermob import *
import pytest

Location_Of_Browser_Mob_Proxy = 'browsermob-proxy-2.1.0-beta-5/bin/browsermob-proxy'
Location_Of_Chrome_Driver = ''
Test_Websiite = 'https://in.yahoo.com/?p=us'
WAIT_TIME = 5

def test_startProxyServer_With_Little_Proxy_Support():
	'''
		Start Proxy Server With Little Proxy Support Unit Test Method
		Asserts The Type Of Server Object
	'''
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy)
	checkData = browsermobproxy.Server(Location_Of_Browser_Mob_Proxy)
	checkData.start()
	
	closeProxyServer(Server)
	closeProxyServer(checkData)
	
	assert type(Server) == type(checkData)
	
def test_startProxyServer_With_Legacy_Support():
	'''
		Start Proxy Server Unit With Legacy Support Test Method
		Asserts The Type Of Server Object
	'''
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy,{'legacy_mode':True})
	checkData = browsermobproxy.Server(Location_Of_Browser_Mob_Proxy,{'legacy_mode':True})
	checkData.start()
	
	closeProxyServer(Server)
	closeProxyServer(checkData)
	
	assert type(Server) == type(checkData)
	
def test_createProxy():
	'''
		Create Proxy Unit Test Method
		Asserts The Type Of Proxy Client Object
	'''
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy)
	Proxy = createProxy(Server)
	
	checkServer = browsermobproxy.Server(Location_Of_Browser_Mob_Proxy)
	checkServer.start()
	checkProxy = checkServer.create_proxy()
	
	closeProxyServer(Server)
	closeProxyServer(checkServer)
	
	assert type(Proxy) == type(checkProxy)

def test_createWebDriver():
	'''
		Create Web Driver Unit Test Method
		Asserts The Type Of Selenium Web Driver Object
	'''
	global Location_Of_Chrome_Driver
	
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy)
	Proxy = createProxy(Server)
	
	if Location_Of_Chrome_Driver == '':
		Location_Of_Chrome_Driver = os.getcwd() + '/chromedriver'
	
	Proxy_Options = webdriver.ChromeOptions()
	Proxy_Options.add_argument('--proxy-server={0}'.format(Proxy.proxy))
	Driver = createWebDriver(Proxy)
	checkDriver = webdriver.Chrome(Location_Of_Chrome_Driver,chrome_options = Proxy_Options)
	
	closeWebDriver(Driver)
	closeWebDriver(checkDriver)
	
	assert type(Driver) == type(checkDriver)
	
def test_WebElement_By_ID_With_Little_Proxy_Support():
	'''
		Checks The Web Element By ID With Little Proxy Support Unit Test Method
		ID = 'UHSearchWeb'
		Value = 'Search Web'
		Asserts The String Value Of The Selenium Web Element Object
	'''
	Test_Failure = False
	
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy)
	Proxy = createProxy(Server)
	Driver = createWebDriver(Proxy)
	Proxy.new_har(Test_Websiite)
	
	Driver.get(Test_Websiite)
	
	Web_Element_By_ID = findWebElement(Driver,'ID','UHSearchWeb')
	
	if Web_Element_By_ID != None:
		checkData = Web_Element_By_ID.get_attribute('value')
	else:
		Test_Failure = True
			
	Network_Data = Proxy.har
	if jsonWrite('Test_Browsermob_By_ID',Network_Data) == True:
		print 'Network Data Written To A Text File'
	else:
		Test_Failure = True
	
	closeProxyServer(Server)
	closeWebDriver(Driver)
	
	if Test_Failure == True:
		assert 0
	
	assert checkData == 'Search Web'
	
def test_WebElement_By_ID_With_Legacy_Support():
	'''
		Checks The Web Element By ID Unit With Legacy Support Test Method
		ID = 'UHSearchWeb'
		Value = 'Search Web'
		Asserts The String Value Of The Selenium Web Element Object
	'''
	Test_Failure = False
	
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy,{'legacy_mode':True})
	Proxy = createProxy(Server)
	Driver = createWebDriver(Proxy)
	Proxy.new_har(Test_Websiite)
	
	Driver.get(Test_Websiite)
	
	Web_Element_By_ID = findWebElement(Driver,'ID','UHSearchWeb')
	
	if Web_Element_By_ID != None:
		checkData = Web_Element_By_ID.get_attribute('value')
	else:
		Test_Failure = True
			
	Network_Data = Proxy.har
	if jsonWrite('Test_Browsermob_By_ID',Network_Data) == True:
		print 'Network Data Written To A Text File'
	else:
		Test_Failure = True
	
	closeProxyServer(Server)
	closeWebDriver(Driver)
	
	if Test_Failure == True:
		assert 0
	
	assert checkData == 'Search Web'
	
def test_WebElement_By_Tag_With_Little_Proxy_Support():
	'''
		Checks The Web Element By Tag With Little Proxy Support Unit Test Method
		Tag = 'Title'
		Value = 'Yahoo'
		Asserts The String Value Of The Selenium Web Element Object
	'''
	Test_Failure = False
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy)
	Proxy = createProxy(Server)
	Driver = createWebDriver(Proxy)
	Proxy.new_har(Test_Websiite)
	
	Driver.get(Test_Websiite)
	
	Web_Element_By_Tag = findWebElement(Driver,'Tag','title')
	
	if Web_Element_By_Tag != None:
		checkData = Web_Element_By_Tag.get_attribute('textContent')
	else:
		Test_Failure = True
			
	Network_Data = Proxy.har
	if jsonWrite('Test_Browsermob_By_Tag',Network_Data) == True:
		print 'Network Data Written To A Text File'
	else:
		Test_Failure = True
	
	closeProxyServer(Server)
	closeWebDriver(Driver)
	
	if Test_Failure == True:
		assert 0
		
	assert checkData == 'Yahoo'
	
def test_WebElement_By_Tag_With_Legacy_Support():
	'''
		Checks The Web Element By Tag With Legacy Support Unit Test Method
		Tag = 'Title'
		Value = 'Yahoo'
		Asserts The String Value Of The Selenium Web Element Object
	'''
	Test_Failure = False
	Server = startProxyServer(Location_Of_Browser_Mob_Proxy,{'legacy_mode':True})
	Proxy = createProxy(Server)
	Driver = createWebDriver(Proxy)
	Proxy.new_har(Test_Websiite)
	
	Driver.get(Test_Websiite)
	
	Web_Element_By_Tag = findWebElement(Driver,'Tag','title')
	
	if Web_Element_By_Tag != None:
		checkData = Web_Element_By_Tag.get_attribute('textContent')
	else:
		Test_Failure = True
			
	Network_Data = Proxy.har
	if jsonWrite('Test_Browsermob_By_Tag',Network_Data) == True:
		print 'Network Data Written To A Text File'
	else:
		Test_Failure = True
	
	closeProxyServer(Server)
	closeWebDriver(Driver)
	
	if Test_Failure == True:
		assert 0
		
	assert checkData == 'Yahoo'
