class EventsPage(object):
	def __init__(self, erros = None):
		self.erros = erros
# -1: Codigo TimeOut, -2: Codigo NoSuchElement
	def sigIn(driver):		
		try:
			driver.execute_script("document.getElementsByTagName('a')[1].click()") #click signIn
			driver.execute_script("document.body.querySelectorAll('*[href=\"/accounts/login/\"]')[0].click();") #click Using Email or password
		except TimeoutException as e:
			self.erros.append(e)
			return -1

		except NoSuchElementException as e:
			self.erros.append(e)
			return -2
		
	def newEvent(driver):
		try:
			driver.execute_script(r"document.body.querySelectorAll('*[href=\"/events/create/\"]')[0].click();") #NEW EVENT
		except TimeoutException as e:
			self.erros.append(e)
			return -1

		except NoSuchElementException as e:
			self.erros.append(e)
			return -2

	def votaEventoTeste(driver):
		driver.get(driver.current_url + "teste/")