# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
import time

driver = None

def comecar():
	global driver
	driver = webdriver.Chrome(r"./chromedriver")
	driver.get("http://127.0.0.1:8000/")
	driver.execute_script(r"document.body.querySelectorAll('*[href=\"/events/\"]')[0].click();") #GET STARTED
	time.sleep(2)

def signin():
	driver.execute_script("document.getElementsByTagName('a')[1].click()")
	driver.execute_script("document.body.querySelectorAll('*[href=\"/accounts/login/\"]')[0].click();")

def signup():
	driver.execute_script(r"document.body.querySelectorAll('*[href=\"/accounts/signup/?next=%2Fevents%2Fcreate%2F\"]')[0].click();") #SIGN UP
	time.sleep(2)

def tentaCriarNovoEvento():
	driver.execute_script(r"document.body.querySelectorAll('*[href=\"/events/create/\"]')[0].click();") #NEW EVENT
	time.sleep(2)


def criaConta():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123ABC")
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123ABC")
	driver.execute_script("document.getElementsByTagName(\"button\")[1].click();")
	time.sleep(3)


def tentaCriarContaSemUserName():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[1].click();")
	time.sleep(3)

def tentaCriarContaSemEmail():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[1].click();")
	time.sleep(3)

def tentaCriarContaSemSenha():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[1].click();")
	time.sleep(3)

def tentaCriarContaSemConfirmSenha():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.execute_script("document.getElementsByTagName(\"button\")[1].click();")
	time.sleep(3)

def tentaCriarContaSenhaMenor():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[1].click();")
	time.sleep(3)

def loginTestador():
	input_login = driver.find_element_by_id("id_login")
	input_login.clear()
	input_login.send_keys("testador")
	input_senha = driver.find_element_by_id("id_password")
	input_senha.clear()
	input_senha.send_keys("123ABC")
	driver.execute_script("document.getElementsByClassName('success')[0].click()")


def insereTituloEvento(title):
	driver.find_element_by_id("id_title").send_keys(title)

def insereDescricaoEvento(descricao):
	driver.find_element_by_id("mceu_25").send_keys(descricao)

def clickNegrito():
	driver.execute_script("document.getElementsByTagName('button')[1].click();")

def clickItalic():
	driver.execute_script("document.getElementsByTagName('button')[2].click()")

def clickSublinhado():
	driver.execute_script("document.getElementsByTagName('button')[3].click()")

def configColor():
	driver.find_element_by_class_name("mce-open") #Abre paleta de cores
	driver.find_element_by_id('mceu_30-16').click() #Escolhe vermelho
	driver.execute_script("document.getElementsByTagName('button')[4].click()") #Clica para acionar cor

def alinhaEsquerda():
	driver.execute_script("document.getElementsByTagName('button')[6].click()")

def alinhaCentro():
	driver.execute_script("document.getElementsByTagName('button')[7].click()")

def alinhaDireita():
	driver.execute_script("document.getElementsByTagName('button')[8].click()")

def desfazTexto():
	driver.execute_script("document.getElementsByTagName('button')[11].click()")

def refazTexto():
	driver.execute_script("document.getElementsByTagName('button')[12].click()")

def limparFormatacao():
	driver.execute_script("document.getElementsByTagName('button')[13].click()")

def titulacao(): #Headings
	driver.execute_script("document.getElementsByTagName('button')[14].click()")
	driver.execute_script("document.getElementById('mceu_47-text').click()")
	time.sleep(2)	
	driver.execute_script("document.getElementById('mceu_48-text').click()")
	time.sleep(2)	
	driver.execute_script("document.getElementById('mceu_49-text').click()")
	time.sleep(2)	
	driver.execute_script("document.getElementById('mceu_50-text').click()")
	time.sleep(2)	
	driver.execute_script("document.getElementById('mceu_51-text').click()")
	time.sleep(2)	
	driver.execute_script("document.getElementById('mceu_52-text').click()")
	time.sleep(2)	
	driver.execute_script("document.getElementById('mceu_53-text').click()")

def tamanhoFonte(): #Set font size
	driver.execute_script("document.getElementById('mceu_13-open').click()")
	driver.execute_script("document.getElementById(mceu_55-text).click()")
	time.sleep(2)
	driver.execute_script("document.getElementById(mceu_56-text).click()")
	time.sleep(2)
	driver.execute_script("document.getElementById(mceu_57-text).click()")
	time.sleep(2)
	driver.execute_script("document.getElementById(mceu_58-text).click()")
	time.sleep(2)
	driver.execute_script("document.getElementById(mceu_59-text).click()")
	time.sleep(2)
	driver.execute_script("document.getElementById(mceu_60-text).click()")
	time.sleep(2)
	driver.execute_script("document.getElementById(mceu_61-text).click()")

def clickPreVisualizar(): #clica no botao preview
	driver.execute_script("document.getElementsByTagName('button')[17].click()") #Preview
	time.sleep(4)
	driver.find_element_by_class_name("mce-close").click() #Close Preview

def publish(check): #marca ou desmarca a opcao publish
	if check == True:
		driver.execute_script("document.getElementById('uniform-id_is_published').childNodes[0].className = 'checked';")
	else:
		driver.execute_script("document.getElementById('uniform-id_is_published').childNodes[0].className = '';")


def allowPublicVting(check): #marca ou desmarca a opcao Allow Public Voting
	if check == True:
		driver.execute_script("document.getElementById('uniform-id_allow_public_voting').childNodes[0].className = 'checked';")
	else:
		driver.execute_script("document.getElementById('uniform-id_allow_public_voting').childNodes[0].className = '';")

def configData(): #Faz todo o proceso para definir a data do evento
	driver.find_element_by_id("id_due_date_0").click() #clica em Due Date para poder setar data
	



comecar()
signin()
loginTestador()
'''
tentaCriarNovoEvento()
tentaCriarNovoEvento()
tentaCriarContaSemUserName()
tentaCriarContaSemEmail()
tentaCriarContaSemSenha()
tentaCriarContaSemConfirmSenha()
tentaCriarContaSenhaMenor()
criaConta()
driver.close()
'''