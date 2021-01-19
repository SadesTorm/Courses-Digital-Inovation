from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import csv



#menu de entrada 
print('Bem Vindo ao Robot-WP')
option_in = input('Escolha uma opção abaixo:\n 1 - Enviar somente texto \n 2 - Enviar somente Imagem \n 3 - Enviar imagem em seguida um texto \n 4 - Enviar imagem com comentario \n->')


#iniciando navegação no Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
#pesquisando link no qual desejo navegar
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#definindo os contatos para destino da mensagem 

arquivo_sms =  open('sms.txt', 'r') 
sms = arquivo_sms.read()

arquivo_img =  open('img.txt', 'r') 
img = arquivo_img.read()

print(sms)

#lista de contatos
contatos = []

#abrindo arquivo com os contatos e add na lista
with open('contacts.csv', 'r', encoding="utf8") as entrada:
    ler = csv.reader(entrada)
    next(ler)
    for linha in ler:
    
       contatos.append(linha[0])  


#imprimindo lista
#print(contatos)



#função para buscar contato 
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#função para o envio da menssagem de texto
def enviar_sms(op,sms):

    campo_text = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_text[op].click()
    time.sleep(2)
    campo_text[op].send_keys(sms)
    campo_text[op].send_keys(Keys.ENTER)
   
#função para envio de imagem
def enviar_img():
    
    button_clip('anexar img',img)

    button_enviar_img = driver.find_element_by_xpath('//span[@data-testid="send"]')
    button_enviar_img.click()
    time.sleep(2)

#função para envio de imagem com comentario
def enviar_img_sms(sms):

    button_clip('anexar img',img)

    campo_text = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_text[0].click()
    time.sleep(3)
    campo_text[0].send_keys(sms)
    time.sleep(3)

    button_enviar_img = driver.find_element_by_xpath('//span[@data-testid="send"]')
    button_enviar_img.click()
    time.sleep(3)
   

#função  botao clip (anexar)
def button_clip(option,fille):

    if option == 'anexar img':
        button_anexar = driver.find_element_by_xpath('//span[@data-testid="clip"]')
        button_anexar.click()
        button_img = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        button_img.send_keys(fille)
        time.sleep(2) 


for contato in contatos:

    buscar_contato(contato)
    if int(option_in) ==1:        
        enviar_sms(1,sms)

    elif int(option_in) ==2:
        enviar_img()

    elif int(option_in) ==3:   
        enviar_img()
        enviar_sms(1,sms)

    elif int(option_in) ==4:
        enviar_img_sms(sms)
    else:
        continue