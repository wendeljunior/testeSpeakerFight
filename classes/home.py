class Home(object):
	def __init__(self, erros = []):
		self.erros = erros
	# -1: Codigo TimeOut, -2: Codigo NoSuchElement
	def getStarted(driver):
		try:
			driver.execute_script(r"document.body.querySelectorAll('*[href=\"/events/\"]')[0].click();") #Clicando em GET STARTED
			time.sleep(2)
		except TimeoutException as e:
			self.erros.append(e)
			return -1

		except NoSuchElementException as e:
			self.erros.append(e)
			return -2

	def tellMeAbout(driver):
		driver.execute_script(r"document.body.querySelectorAll('*[href=\"/about/\"]')[0].click();") #Clicando em Tell me about speakerfight
		time.sleep(2)
		except TimeoutException as e:
			self.erros.append(e)
			return -1

		except NoSuchElementException as e:
			self.erros.append(e)
			return -2

	def joinTheFighters(driver):
		driver.execute_script(r"document.body.querySelectorAll('*[href=\"/events/\"]')[0].click();") #Clicando em Join the fighters
		time.sleep(2)
		except TimeoutException as e:
			self.erros.append(e)
			return -1

		except NoSuchElementException as e:
			self.erros.append(e)
			return -2