import pyautogui
from PIL import Image
from pytesseract import pytesseract
import time


def atualizar_relatorio(resultado_teste):
    with open('resultadosdostestes.txt', "a") as arquivo:
        arquivo.write(resultado_teste + "\n")

def verificar_botao():
    # Localize a posição do botão na tela
    botao_posicao = pyautogui.locateCenterOnScreen('botaoaviso.png', confidence=0.5)
    if botao_posicao is not None:
        return True
    else:
        return False

def executar_testes():
    
    caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = caminho_tesseract
    
    # Teste 01 -> Validação de Login e Senha / Senha Incorreta
    pyautogui.doubleClick(557, 342, duration=1) 
    pyautogui.sleep(7)
    pyautogui.click(705, 307, duration=0.5)
    pyautogui.click(590, 351, duration=0.5)
    pyautogui.click(538, 370, duration=0.5)
    pyautogui.write('Casevabe3711')
    pyautogui.click(736, 469, duration=0.5)  
    pyautogui.sleep(0.25)
    pyautogui.screenshot('teste01_msgerro.png')
    pyautogui.click(683, 415, duration=0.5) 
    screenshot = pyautogui.screenshot(region=(0, 0, 1366, 768))
    screenshot.save('teste01_Msg_de_Erro.png')
    texto = pytesseract.image_to_string(Image.open('teste01_Msg_de_Erro.png'))
    
    nome_arquivo_imagem = "botaoavisologin.png"
if verificar_botao():
        atualizar_relatorio('Test01_Msg_Erro -> PASSOU')
else: 
        atualizar_relatorio('Test01_Sem_Msg_Erro -> FALHOU')
        
        if __name__ == "__main__":
            while True:
                executar_testes()


    #Teste1.1 -> Validação de Login e Senha / Senha Correta / caminho feliz
    #Automação - Escolher ADMIN - Digitar Senha - Clicar no botão entrar - Logou no sistema -> 'Teste passou'
    
    #MÉTODO BDD
    
    #Given usuário clique em 'admin'
    #And Digite senha correta
    #When clicar em 'entrar'
    #Then Logará no sistema corretamente

pyautogui.click(705,307, duration=0.5)
pyautogui.click(590,351,duration=0.5)
pyautogui.click(538,370,duration=0.5)
pyautogui.write('Casevabe3721')
pyautogui.click(736,469, duration=0.5)  # Entrar e logar no sist
pyautogui.sleep(1)

screenshot = pyautogui.screenshot(region=(0, 0, 1366, 768))
screenshot.save ('teste1.1_Acesso_ao_Sistema.png')
texto = pytesseract.image_to_string(Image.open('teste1.1_Acesso_ao_Sistema.png'))

logar_sistema = "CONSUMER"
if logar_sistema in texto:
            atualizar_relatorio('Test01_Logar_no_Sistema -> PASSOU') #logar no sist
else: 
            atualizar_relatorio('Test01_Msg_Erro-> FALHOU') #se nao logar
            pyautogui.click(690,418, duration=0.5)
            pyautogui.click(1131,96, duration=0.5)
            
            if __name__ == "__main__":
                while True:
                    executar_testes()
            
#Teste 02 -> Fechamento de Caixa caminho feliz
    #Automação -  Clicar em abrir/fechar caixa - abrir caixa - digitar valor - clicar em salvar -se adicionar valor -> Teste Passed
    
        # Método BDD 

        #Given: que faça abertura de caixa;
        #And: digite valor
        #When: clicar em salvar;
        #Then: abre-se caixa corretamente.

pyautogui.sleep(1)
pyautogui.click(69,80, duration=0.5)       #abrir/fechar
pyautogui.click(262,401, duration=0.5)       #abrir caixa
pyautogui.sleep(1)
pyautogui.click(1070,109, duration=1)       #adc entrada/saida
pyautogui.click(588,357, duration=0.5)      #clica em entrada
pyautogui.click(587,406, duration=0.5)         #clique valor
pyautogui.write('3')                             #digita valor
pyautogui.click(870,545, duration=0.5)       #clicar salvar  

pyautogui.sleep(1) 

screenshot = pyautogui.screenshot(region=(1144, 588, 300, 250))
screenshot.save ('teste2_msgsuc.png')
texto = pytesseract.image_to_string(Image.open('teste2_msgsuc.png'))

mensagem_sucesso = "Adicionar Entrada"
if mensagem_sucesso in texto:
            atualizar_relatorio('Test02_Msg_Sucesso -> PASSOU')  #msg operaçao realizada c suc 
else: 
            atualizar_relatorio('Test02_Sem_Msg_Sucesso -> FALHOU')  #msg operaçao realizada c suc
            
 #Teste 2.1 -> Abir / Fechar caixa
     # Automação - Clicar em abrir/fechar caixa - abrir caixa - tentar fechar caixa sem registrar um valor -  Reconhecer mensagem de erro -> 'Teste Passed'

        # Método BDD 

        #Given: clicar em abrir/fechar caixa;
        #And: clicar adc entrada/saida;
        #When: salvar sem digitar valor;
        #Then: gera-se uma mensagem de erro.
                  
pyautogui.click(1070,109, duration=1)       #adc entrada/saida
pyautogui.click(588,357, duration=0.5)      #clica em entrada
pyautogui.click(870,545, duration=0.5)       #clicar salvar  
pyautogui.sleep(1)

    #Se encontrar mensagem de erro na tela -> gerar teste passed
    #Quando houver muita info e ícone com cor  

screenshot = pyautogui.screenshot(region=(0, 0, 1350, 580))     #Captura a região da tela
screenshot.save('teste2.1_msgalerta.png')
pyautogui.sleep(1)
pyautogui.click(684,416, duration=0.5)       #clicar confirmar 
pyautogui.click(752,545, duration=0.5)         #clicar em voltar
pyautogui.click(1206,67, duration=0.5)          #clicar em x

nome_arquivo_imagem = "botaoaviso.png"      #nome do arquivo de imagem
if verificar_botao():   # Chame a função verificar_botao() p/ verificar se o botão está na tela 
    atualizar_relatorio('Test2.1_Msg_Erro -> PASSOU')  # Deve aparecer botão de alerta
else: 
    atualizar_relatorio('Test2.1_Sem_Msg_Erro-> FALHOU') #Não deve aparecer botão de alerta
            
pyautogui.click(690,419)                        #clicar em confirmar 
pyautogui.click(760,542)                        #clicar em voltar
pyautogui.click(1208,67)                        #clico p fechar

    #Teste 03 -> Validar o click em mesa e fazer pedido
    #Automação - Clicar em mesa - fazer pedido - digitar um pedido - clicar em salvar pedido 
    
        # Método BDD 

        #Given: que clique em Mesas/Comandas;
        #And: Selecione a mesa desejada
        #When: quando 'Buscar produto escrito';
        #Then: então gera-se um pedido.

pyautogui.click(273,85, duration=0.5)       #coordenada de mesas/comandas
pyautogui.click(208,282, duration=0.5)       #mesa1
pyautogui.click(547,130, duration=0.5)       #clicar na janela buscar   
pyautogui.write('cocada')                       #escreverproduto
pyautogui.click(644,362, duration=0.5)       #clicar em adicionar
pyautogui.sleep(1)
        
        #Se encontrar a palavra adicionada na tela -> gerar teste passed 

screenshot = pyautogui.screenshot(region=(0,0, 1366,768))
screenshot.save ('pedidofeito.png')
texto = pytesseract.image_to_string(Image.open('pedidofeito.png'))

pedido_efetivado = "Itens do Pedido"
if pedido_efetivado in texto:
            atualizar_relatorio('Test03_Pedido_Adc -> PASSOU')  #deve mostrar iten adc
else: 
            atualizar_relatorio('Test03_NGerou_Pedido -> FALHOU')  #se n mostrar iten adc
            
#Teste 04 -> Cadastro de Produtos - Massa de Dados 
    #Automação - Clicar em produtos - novo - digitar características - salvar -> 'Teste Passou'  
    
        # Método BDD 

        #Given: que clique em novo produto;
        #And: adicione os dados relacionados;
        #When: quando clicar em salvar;
        #Then: então adiciona-se novo produto ao sistema.

#Teste 4.1 -> Cadastro de Produtos Iguais / Mensagem de Erro + continuação de looping 
    #Automação - Salvar produtos iguais - aparecer msg 'produto já cadastrado' - reconhecer mensagem - clicar em confirmar - fechar a tela - retornar looping -> TESTE PASSOU 
    
pyautogui.click(112,31,duration=1)      #Clicando no botao produtos
pyautogui.click(49,78,duration=1)     #Clicandos em Produtos
pyautogui.click(1293,165,duration=1)  #Clicando em Novo
        
with open('produtosparacadastrar.txt','r') as arquivo:
    for linha in arquivo:  
        nome = linha.split(',')[0]
        custo = linha.split(',')[1]
        final = linha.split(',')[2]
        pyautogui.click(1293,165,duration=1)  #Clicando em Novo
        pyautogui.click(339.142, duration=1)
        # 1 clicar em Nome e escrever o nome do produto
        pyautogui.write(nome)
        # 2 clicar em categoria e escolher 'refeições'
        pyautogui.click(339,177, duration=1)    #clica em categoria
        pyautogui.click(341,258, duration=1)    #clica em refeições
        # 3 clicar em preço de custo e adc valor
        pyautogui.click(339,203, duration=1)    #clica em preço de custo     
        pyautogui.write(custo)   
        # 4 clicar em preço de venda e adicionar valor
        pyautogui.click(556,202, duration=1)    #clica cód. do sistema
        pyautogui.write(final)  
        # 5 Clicar em Salvar
        pyautogui.click(1060,622, duration=1)   #Clica em Salvar 
        pyautogui.sleep(1)
        # 6 Verificar se o produto foi salvo
        screenshot = pyautogui.screenshot(region=(1144, 588, 300, 250))
        screenshot.save ('teste4_novo_produto_cad.png')
        texto = pytesseract.image_to_string(Image.open('teste4_novo_produto_cad.png'))

        mensagem_sucesso = "Novo Produto"
        if mensagem_sucesso in texto:
            atualizar_relatorio('Test04_Cad_Produto -> PASSOU')
        else: 
            atualizar_relatorio('Test04_Cad_Produto -> FALHOU')
            pyautogui.click(690,418, duration=0.5)
            pyautogui.click(1131,96, duration=0.5)
            
            # Outros testes aqui...
    
if __name__ == "__main__":
    while True:
        executar_testes()
        time.sleep(180)  # Aguardar 60 segundos antes de executar os testes novamente