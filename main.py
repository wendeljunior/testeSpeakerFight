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