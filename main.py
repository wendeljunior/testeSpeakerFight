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
lento = 4 # 4 segundos
medio = 2 # 2 segundos
rapido = 1 # 1 segundo

def comecar():
	global driver
	driver = webdriver.Chrome(r"./chromedriver")
	driver.get("http://127.0.0.1:8000/")
	driver.execute_script(r"document.body.querySelectorAll('*[href=\"/events/\"]')[0].click();") #GET STARTED
	time.sleep(lento)

def signin():
	global driver
	driver.execute_script("document.getElementsByTagName('a')[1].click()")
	driver.execute_script("document.body.querySelectorAll('*[href=\"/accounts/login/\"]')[0].click();")
	time.sleep(rapido)

def signup():
	global driver
	driver.execute_script(r"document.body.querySelectorAll('*[href=\"/accounts/signup/\"]')[0].click();") #SIGN UP
	time.sleep(medio)

def tentaCriarNovoEvento():
	global driver
	driver.execute_script(r"document.body.querySelectorAll('*[href=\"/events/create/\"]')[0].click();") #NEW EVENT
	time.sleep(lento)


def criaConta(nome, email, senha):
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys(nome) #testador
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys(email) #123@mail.com
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys(senha) #123ABC
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys(senha)
	driver.execute_script("document.getElementsByTagName(\"button\")[0].click();")
	time.sleep(lento)


def tentaCriarContaSemUserName():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[0].click();")
	time.sleep(lento)

def tentaCriarContaSemEmail():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[0].click();")
	time.sleep(lento)

def tentaCriarContaSemSenha():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[0].click();")
	time.sleep(lento)

def tentaCriarContaSemConfirmSenha():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.execute_script("document.getElementsByTagName(\"button\")[0].click();")
	time.sleep(lento)

def tentaCriarContaSenhaMenor():
	driver.find_element_by_id("id_username").clear()
	driver.find_element_by_id("id_username").send_keys("testador")
	driver.find_element_by_id("id_email").clear()
	driver.find_element_by_id("id_email").send_keys("123@mail.com")
	driver.find_element_by_id("id_password1").clear()
	driver.find_element_by_id("id_password1").send_keys("123")
	driver.find_element_by_id("id_password2").clear()
	driver.find_element_by_id("id_password2").send_keys("123")
	driver.execute_script("document.getElementsByTagName(\"button\")[0].click();")
	time.sleep(lento)

def loginTestador():
	input_login = driver.find_element_by_id("id_login")
	input_login.clear()
	input_login.send_keys("testador")
	input_senha = driver.find_element_by_id("id_password")
	input_senha.clear()
	input_senha.send_keys("123ABC")
	driver.execute_script("document.getElementsByClassName('success')[0].click();")
	time.sleep(rapido)


def insereTituloEvento(titulo):
	driver.execute_script("document.getElementById('id_title').value = '%s';"%titulo)
	time.sleep(medio)

def insereDescricaoEvento(descricao):
	driver.execute_script("document.getElementById('mceu_25').value = '%s';"%descricao)
	time.sleep(medio)

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
	time.sleep(rapido)	
	driver.execute_script("document.getElementById('mceu_48-text').click()")
	time.sleep(rapido)	
	driver.execute_script("document.getElementById('mceu_49-text').click()")
	time.sleep(rapido)	
	driver.execute_script("document.getElementById('mceu_50-text').click()")
	time.sleep(rapido)	
	driver.execute_script("document.getElementById('mceu_51-text').click()")
	time.sleep(rapido)	
	driver.execute_script("document.getElementById('mceu_52-text').click()")
	time.sleep(rapido)	
	driver.execute_script("document.getElementById('mceu_53-text').click()")

def tamanhoFonte(): #Set font size
	driver.execute_script("document.getElementById('mceu_13-open').click()")
	driver.execute_script("document.getElementById(mceu_55-text).click()")
	time.sleep(rapido)
	driver.execute_script("document.getElementById(mceu_56-text).click()")
	time.sleep(rapido)
	driver.execute_script("document.getElementById(mceu_57-text).click()")
	time.sleep(rapido)
	driver.execute_script("document.getElementById(mceu_58-text).click()")
	time.sleep(rapido)
	driver.execute_script("document.getElementById(mceu_59-text).click()")
	time.sleep(rapido)
	driver.execute_script("document.getElementById(mceu_60-text).click()")
	time.sleep(rapido)
	driver.execute_script("document.getElementById(mceu_61-text).click()")

def clickPreVisualizar(): #clica no botao preview
	driver.execute_script("document.getElementsByTagName('button')[17].click()") #Preview
	time.sleep(lento)
	driver.find_element_by_class_name("mce-close").click() #Close Preview

def publish(check): #marca ou desmarca a opcao publish
	if check == True:
		driver.execute_script("document.getElementById('uniform-id_is_published').childNodes[0].className = 'checked';")
	else:
		driver.execute_script("document.getElementById('uniform-id_is_published').childNodes[0].className = '';")

def allowPublicVoting(check): #marca ou desmarca a opcao Allow Public Voting
	if check == True:
		driver.execute_script("document.getElementById('uniform-id_allow_public_voting').childNodes[0].className = 'checked';")
	else:
		driver.execute_script("document.getElementById('uniform-id_allow_public_voting').childNodes[0].className = '';")

def preencheData(mes, dia, ano, hora, minutos): #Faz todo o proceso para definir a data do evento
	driver.find_element_by_id("id_due_date_0").click() #clica em Due Date para poder setar data
	driver.find_element_by_id("id_due_date_0").send_keys(str(mes)+'/'+str(dia)+'/'+str(ano)+' '+str(hora)+':'+str(minutos))
	driver.find_element_by_id("id_due_date_0").send_keys(Keys.Enter)

def preencheLugares(qtLugares): #Define quantidade de lugares na plateia
	driver.find_element_by_id("id_slots").send_keys(qtLugares)

def anonymousVoting(check): #Marca a opcao de permitir voto anonimo
	if check == True:
		driver.execute_script("document.getElementById('uniform-id_anonymous_voting').childNodes[0].className = 'checked';")
	else:
		driver.execute_script("document.getElementById('uniform-id_anonymous_voting').childNodes[0].className = '';")

def confirmaCriacaoEvento(): #clica em submit para finalizar criacao de evento
	driver.find_element_by_css_selector(".btn-flat .success .text-upper")

def clickEvents(): #clica em 'Events' no menu lateral esquerdo
	driver.execute_script("document.getElementById('dashboard-menu').childNodes[1].getElementsByTagName('a')[0].click();")

def clickMyProposals(): #clica em 'My Proposals' no menu lateral esquerdo
	driver.execute_script("document.getElementById('dashboard-menu').childNodes[3].getElementsByTagName('a')[0].click();")

def clickMyEvents(): #clica em 'My Events' no menu lateral esquerdo
	driver.execute_script(" document.getElementById('dashboard-menu').childNodes[5].getElementsByTagName('a')[0].click();")

def href():
	driver.find_element_by_href()


'''
#Teste Cricao de conta
comecar()
signin()
signup()
criaConta('testador', 'testador@mail.com', '123ABC')
tentaCriarContaSemUserName()
tentaCriarContaSemEmail()
tentaCriarContaSemSenha()
tentaCriarContaSemConfirmSenha()
tentaCriarContaSenhaMenor()
'''


#Teste criacao de eventos
comecar()
signin()
loginTestador()
tentaCriarNovoEvento()
insereTituloEvento("Aprovação na Disciplina de Teste de Software")
insereDescricaoEvento("Neste maravilhoso encontro, vamos comemorar a aprovação dos alunos que sobreviveram a mais uma disciplina de mais um semestre no glorioso Bacharelado em Tecnologia da Informação.")
