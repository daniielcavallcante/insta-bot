from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import random

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/p/B_lBfLzHn0Q/")
driver.maximize_window()
sleep(2)
#Entrar
element = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button")
element.click()
sleep(2)
#Usuario
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
element.send_keys('daniielcavallcante')
sleep(1)
#Senha
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
element.send_keys('guaraton1')
sleep(1)
#Submeter
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button")
element.click()
sleep(2)

#Le o arquivo com os usuarios
arquivo = open('accounts.txt', 'r')
arquivo = arquivo.readlines()


wait = WebDriverWait(driver, 10)
comentarios = 0

for i in arquivo:
    #delay
    espera = random.randint(5, 15)

    #Clica para comentar e digita o comentario
    element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea")
    element.click()
    ActionChains(driver).send_keys(i).perform()

    #delay
    espera1 = random.randint(2, 5)
    sleep(espera1)

    #Envia o comentario
    element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button")
    ActionChains(driver).move_to_element(element).click(element).perform()

    print('Comentarios bem sucedidos: ', comentarios)
    #delay
    espera2 = random.randint(1, 4)
    sleep(espera2)
    comentarios+=1
    if comentarios >= 30:
        break
    #recarrega a pagina
    print('Espera atual: ', espera)
    sleep(espera)
    driver.refresh()



'''
###Automatizaaao para novas contas
#Regras de participaaao
driver.get("https://www.instagram.com/fgg_andre/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B_lBfLzHn0Q/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button/svg")
element.click()
driver.get("https://www.instagram.com/alan_leocadio/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/bobtechoficial/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/canalemanalise/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/jucyber/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/jtg.eletronics/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/luan.ltech/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()


#Outras contas
#Guipedro
driver.get("https://www.instagram.com/guiiipedro1/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__dDQKjVlw/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__c69mjVOJ/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()

#Heitoor
driver.get("https://www.instagram.com/heitoorzin/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__cH4sja9U/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__b-B_DxGD/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__b15ujHAZ/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()

#Luca
driver.get("https://www.instagram.com/lucamartins26/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__clLSA8CV/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__ciVZg8DJ/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()


#Henrique
driver.get("https://www.instagram.com/henriquepascoal8/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()

#Brenda
driver.get("https://www.instagram.com/brendamoraaaiis/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__aHlRhNO-/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__Z7lbhs9m/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__ZoJKBAHg/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()


#Luuh
driver.get("https://www.instagram.com/luuhmoraiss1/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__ex4Tp1Yn/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__ep68J7dy/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()


#Karla
driver.get("https://www.instagram.com/brendamoraaaiis/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__kIm0gNjA/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__j_8LAWcU/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()
driver.get("https://www.instagram.com/p/B__j3EtAhQh/")
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")
element.click()


'''
