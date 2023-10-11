from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver


driver = iniciar_driver()

# Navegar até o site
driver.get('https://www.kabum.com.br/computadores/monitores')

# Rolar até o fim da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")

# Encontrar os titulos
titulos = driver.find_elements(By.XPATH, "//div[@class='sc-93fa31de-15 dCsZrx']//h2")
# for titulo in Titulos:
#     print(titulo.text)
# Econtrar os preços
precos = driver.find_elements(By.XPATH, "//div//span[@class='sc-6889e656-2 bYcXfg priceCard']")
# for preco in precos:
#     print(preco.text)
# Encontrar o Link
links = driver.find_elements(By.XPATH, "//div[@class='sc-93fa31de-7 gopyRO productCard']//a")
# for link in links:
#     print(link.text)
# Guardar em um arquivo CSV
for titulo, preco, link in zip(titulos, precos, links):
        with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
            link_processado = link.get_attribute('href')
            arquivo.write(
                f'{titulo.text};{preco.text};{link_processado}{os.linesep}')
# Repetir em todas as páginas 