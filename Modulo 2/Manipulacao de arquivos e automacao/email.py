import pyautogui as gui
import flet as ft

def main(page: ft.Page):
    page.title = "enviar email"
    page.theme_mode = "dark"
    
    # Função para criar pastas
    def enviar_email(e):
            email = texto_recebido.value
            mensagem = mensagem_recebida.value
            gui.press('win')
            gui.sleep(1)
            gui.write('Outlook')
            gui.moveTo(713,500, duration=0.5)
            gui.click()
            gui.sleep(2)
            gui.click()
            gui.hotkey('ctrl', 'n')
            gui.sleep(2)
            gui.write(email)
            gui.press('tab', presses=2)
            gui.write(mensagem)
            gui.hotkey('ctrl', 'enter')
            gui.moveTo(1072,564, duration=0.5)
            gui.click()
            informativo.value = "Email enviado com sucesso!"



    # Campos e botões
    texto_recebido = ft.TextField(label="email", width=300)
    mensagem_recebida = ft.TextField(label="mensagem", width=300, height=100)
    botao = ft.ElevatedButton("Enviar", bgcolor="CYAN", color="WHITE", width=200, on_click=enviar_email)
    informativo = ft.Text("", size=20, color="GREEN")
