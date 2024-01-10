# passo a passo do projeto

# passo 1 - Entrar no sistema da empresa
    # #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# aperta uma tecla -> pyautogui.press
# aperta -> pyautogui.hotkey
# scroll (rolar) -> pyautogui.scroll
pyautogui.PAUSE = 0.5
# aperta a tecla do windows (command + barra de espaço)
pyautogui.press("win")
# digita o nome do programa (Edge)
pyautogui.write("edge")
pyautogui.click(x=875, y=52)
# aperta enter
#pyautogui.press("enter")

# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# aperta enter
pyautogui.press("enter")

# espera - 5 - segundo
time.sleep(3)
    
# passo 2 - fazer login
pyautogui.click(x=813, y=300)
# digitar o email
pyautogui.write("robsonnascimento20@gmail.com")
# passa para o campo de senha
pyautogui.press("tab")
# digitar a senha
pyautogui.write("Hellena20")
# botao
pyautogui.click(x=1027, y=430)
time.sleep(2)


# passo 3 - Importa a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    # passo 4 - Cadastrar um produto
    pyautogui.click(x=825, y=218)


    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.press("tab")
    # codigo
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
# passo 5 - Repetir isso até a base de dados