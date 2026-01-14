  
# Exemplo de automação de tarefas com python

import pyautogui
import time

# pyautogui.click -> clicar
# pyautogui.write -> escrever
# pyautogui.press -> pressionar tecla
# pyautogui.hotkey -> pressionar combinação de teclas (hotkey)
# pyautogui.scroll -> rolar a tela

pyautogui.PAUSE = 0.5  # tempo de espera entre as ações
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' #variável para o link do sistema da empresa 

# passo 1: entrar no sistema da empresa
# abrir o navegador
pyautogui.press('win') # abrir o menu iniciar
pyautogui.write('chrome') # escrever o nome do navegador
pyautogui.press('enter') # pressionar enter para abrir o navegador
pyautogui.write(link) # escrever o link do sistema
pyautogui.press('enter') # pressionar enter para entrar no link
pyautogui.sleep(3)  # esperar 3 segundos para a página carregar

# passo 2: fazer login
pyautogui.click(x=903, y=609)  # clicar no campo de usuário
pyautogui.write('seuEmailAqui') # escrever o usuário
pyautogui.press('tab')  # ir para o próximo campo
pyautogui.write('suaSenhaAqui')  # escrever a senha
pyautogui.press('tab') # ir para o botão de login
pyautogui.press('enter')  # pressionar o botão de login 
pyautogui.sleep(3)  # esperar 3 segundos para a página carregar

# passo 3: abrir a base de dados (importar o arquivo)
import pandas

tabela = pandas.read_csv('Produtos.csv')  # ler a tabela de produtos

for linha in tabela.index:  # para cada linha na tabela
  # passo 4: cadasdtrar 1 produto
  # codigo
  pyautogui.click(x=945, y=444) # clicar no campo de produtos
  codigo = str(tabela.loc[linha, 'codigo'])  # pegar o código do produto da tabela
  pyautogui.write(codigo) # escrever o código do produto
  pyautogui.press('tab') # ir para o próximo campo
  # marca
  marca = str(tabela.loc[linha, 'marca'])  # pegar a marca do produto da tabela
  pyautogui.write(marca) # escrever a marca do produto
  pyautogui.press('tab') # ir para o próximo campo
  # tipo
  tipo = str(tabela.loc[linha, 'tipo'])  # pegar o tipo do produto da tabela
  pyautogui.write(tipo) # escrever o tipo do produto
  pyautogui.press('tab') # ir para o próximo campo
  # categoria
  categoria = str(tabela.loc[linha, 'categoria'])  # pegar a categoria do produto da tabela
  pyautogui.write(categoria) # escrever a categoria do produto
  pyautogui.press('tab') # ir para o próximo campo
  # preco_unitario
  preco_unitario = str(tabela.loc[linha, 'preco_unitario'])  # pegar o preço unitário do produto da tabela
  pyautogui.write(preco_unitario) # escrever o preço unitario do produto
  pyautogui.press('tab') # ir para o próximo campo
  # custo
  custo = str(tabela.loc[linha, 'custo'])  # pegar o custo do produto da tabela
  pyautogui.write(custo) # escrever o custo do produto
  pyautogui.press('tab') # ir para o próximo campo
  # obs
  obs = str(tabela.loc[linha, 'obs'])  # pegar a observação do produto da tabela
  if obs != 'nan':
    pyautogui.write(obs) # escrever uma observação
  pyautogui.press('tab') # ir para o próximo campo (enviar)
  pyautogui.press('enter') # pressionar o botão de enviar (cadastrar o produto)

  pyautogui.scroll(5000)  # voltar para o inicio da pagina

# passo 5: repetir o passo 4 até acabar a lista de produtos
