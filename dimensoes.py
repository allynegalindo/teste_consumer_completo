import pyautogui
from PIL import Image
from pytesseract import pytesseract

def atualizar_relatorio(resultado_teste):   
    with open('resultadosdostestes.txt', "a") as arquivo:
        arquivo.write(resultado_teste + "\n")
  
  # Função para verificar se o botão está presente na tela
def verificar_botao():
    # Localize a posição do botão na tela
    botao_posicao = pyautogui.locateCenterOnScreen('botaoaviso.png', confidence=0.9)
    
    # Se o botão for encontrado, retorne True, caso contrário, retorne False
    if botao_posicao is not None:
        return True
    else:
        return False 
    
caminho_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract 

#Teste 2.1 -> Abir / Fechar caixa

pyautogui.click(69,80, duration=0.5)       #abrir/fechar
pyautogui.click(262,401, duration=0.5)       #abrir caixa
pyautogui.click(1070,109, duration=1)       #adc entrada/saida
pyautogui.click(588,357, duration=0.5)      #clica em entrada
pyautogui.click(870,545, duration=0.5)       #clicar salvar  
pyautogui.sleep(1)

    #Se encontrar mensagem de erro na tela -> gerar teste passed

screenshot = pyautogui.screenshot(region=(0, 0, 1350, 580))     #Captura a região da tela
screenshot.save('teste2.1_msgalerta.png')

# Renomeie a variável que contém o nome do arquivo de imagem
nome_arquivo_imagem = "botaoaviso.jpg"

# Chame a função verificar_botao() para verificar se o botão está presente na tela
if verificar_botao():
    atualizar_relatorio('Test2.1_Msg_Erro -> PASSOU')  # Deve aparecer botão de alerta
else: 
    atualizar_relatorio('Test2.1_Sem_Msg_Erro-> FALHOU')

            