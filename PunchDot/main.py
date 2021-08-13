from selenium import webdriver
import time
import schedule
import json
import os.path


def pega_dados():
    print("Será solicitado apenas na primeira vez do uso do software.")
    time.sleep(5)
    user = input("Digite seu usuario do portal RH:")
    password = input("Digite seu senha do portal RH:")
    my_data = {'user': user, 'password': password}
    with open('data.json', 'w') as t:
        json.dump(my_data, t)


def data_user():

    if not(os.path.exists('data.json')):
        pega_dados()

    else:

        with open('data.json', 'r') as f:
            inputtt = json.load(f)

            user = inputtt['user']
            password = inputtt['password']

    return user, password

def install_library():
    os.system('pip install -r requirements.txt')


def bate_ponto():
    install_library()
    user, password = data_user()

    chrome = webdriver.Chrome(executable_path=r'chromedriver.exe')
    chrome.get("https://apdata.com.br/everis/")
    time.sleep(3)
    chrome.find_element_by_xpath('//*[@id="button-1020-btnEl"]').click()
    # digitar o usuário
    chrome.find_element_by_xpath('// *[ @ id = "ext-135"]').click()
    chrome.find_element_by_xpath('// *[ @ id = "ext-135"]').send_keys(user)
    # digitar a senha
    chrome.find_element_by_xpath('// *[ @ id = "ext-137"]').click()
    chrome.find_element_by_xpath('// *[ @ id = "ext-137"]').send_keys(password)
    # confirmar
    chrome.find_element_by_xpath('//*[@id="ext-139"]').click()
    time.sleep(5)
    chrome.close()

    return 0


def run():

    schedule.every().day.at("08:00").do(bate_ponto)
    schedule.every().day.at("12:00").do(bate_ponto)
    schedule.every().day.at("13:00").do(bate_ponto)
    schedule.every().day.at("17:00").do(bate_ponto)

    while 1:
        schedule.run_pending()
        time.sleep(2)
    return 0


if __name__ == '__main__':
    bate_ponto()

