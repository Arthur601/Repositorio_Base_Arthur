import os
import flet as ft

pasta= ""
arquivo= ""
def main(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"
    
    # Função para criar pastas
    def criar_pasta(e):
        global pasta
        pasta = texto_recebido.value
        try:
            os.mkdir(pasta)
            informativo.value = f"Pasta criada: '{pasta}'"
        except FileExistsError as erro:
            informativo.value = f"Erro: {erro}"
        page.update()
    
    # Função para criar arquivos
    def criar_arquivo(e):
        global arquivo
        arquivo = texto_recebido.value
        if os.path.exists(f'{pasta}'):
            open(f'{pasta}\{arquivo}', "w").close()
            informativo.value = f"Arquivo criado: '{arquivo}'"
        else:
            open(f'{arquivo}', "w").close()
            informativo.value = f"Arquivo criado: '{arquivo}' na pasta '{pasta}'"

    def listar_arquivo(e):
        global listar
        listar = texto_recebido.value
        try:
           os.listdir()
           if os.path.exists(f"{pasta}\{arquivo}"):
               for listar in pasta:
                   informativo.value = f"'{arquivo}' encontrada em '{pasta}'"
           elif os.path.exists(renomear_arquivo):
               for listar in pasta:
                   informativo.value = f"'{renomear_arquivo}' encontrada em '{renomear_pasta}'"
           else:
                informativo.value = f"'{arquivo}' não encontrada"
        except FileNotFoundError as erro:
             informativo.value = f"Erro: {erro}"
        page.update()

    def excluir_arquivo(e):
        global apagar_arquivo
        apagar_arquivo = texto_recebido.value
        try:
            if os.path.exists(f"{pasta}\{arquivo}"):
                os.remove(f"{pasta}\{arquivo}")
                informativo.value = f"arquivo {arquivo} apagado"
            elif os.path.exists(arquivo):
                os.remove(arquivo)
                informativo.value = f"arquivo {arquivo} apagado"
            elif os.path.exists(f"{pasta}\{arquivo}"):
                os.remove(f"{renomear_pasta}\{renomear_arquivo}")
                informativo.value = f"arquivo {arquivo} apagado"
            else:
                informativo.value = f"O arquivo '{arquivo}' não existe"
        except OSError as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    def excluir_pasta(e):
        global excluir_pasta
        excluir_pasta = texto_recebido.value
        try:
            if os.path.exists(pasta):
                os.rmdir(pasta)
                informativo.value = f"Pasta '{pasta}' apagada"
            elif os.path.exists(renomear_pasta):
                os.rmdir(renomear_pasta)
                informativo.value = f"Pasta '{pasta}' apagada"
            else:
                informativo.value = f"A pasta '{pasta}' não existe"
        except OSError as erro:
            informativo.value = f"Erro: {erro}"
        page.update()
    def renomear_arquivo(e):
        global renomear_arquivo
        renomear = texto_recebido.value
        if arquivo == "":
            informativo.value = f"O arquivo '{arquivo}' não existe"
        elif os.path.exists(arquivo):
            os.rename(arquivo, renomear_arquivo)
            informativo.value = f"Arquivo '{arquivo}' renomeado para '{renomear}'"
        elif os.path.exists(f"{renomear_pasta}\{arquivo}"):
            os.rename(f"{renomear_pasta}\{arquivo}", f"{renomear_pasta}\{renomear}")
            informativo.value = f"Arquivo '{arquivo}' renomeado para '{renomear}'"
        else:
            os.rename(f"{pasta}\{arquivo}", f"{pasta}\{renomear}")
            informativo.value = f"Arquivo '{arquivo}' renomeado para '{renomear}'"
        page.update()
    def renomear_pasta(e):
        global renomear_pasta
        renomear2 = texto_recebido.value
        if pasta == "":
            informativo.value = f"A pasta '{pasta}' não existe"

        else:
            informativo.value = f"Pasta '{pasta}' renomeada para '{renomear2}'"
            os.rename(pasta, renomear2)
        page.update()

    # Campos e botões
    texto_recebido = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    botao_pasta = ft.ElevatedButton("Criar pasta", bgcolor="BLACK", color="CYAN", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("Criar arquivo", bgcolor="BLACK", color="CYAN", width=200, on_click=criar_arquivo)
    botao_listar_arquivo = ft.ElevatedButton("Listar arquivo", bgcolor="BLACK", color="WHITE", width=200, on_click=listar_arquivo)
    botao_excluir_arquivo = ft.ElevatedButton("Excluir arquivo", bgcolor="BLACK", color="RED", width=200, on_click=excluir_arquivo)
    botao_excluir_pasta = ft.ElevatedButton("Excluir pasta", bgcolor="BLACK", color="RED", width=200, on_click=excluir_pasta)
    botao_renomear_arquivo = ft.ElevatedButton("Renomear arquivo", bgcolor="BLACK", color="GREEN", width=200, on_click=renomear_arquivo)
    botao_renomear_pasta = ft.ElevatedButton("Renomear pasta", bgcolor="BLACK", color="GREEN", width=200, on_click=renomear_pasta)
    informativo = ft.Text("", size=20, color="white")

    # Layout
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta], alignment="center"),
        ft.Row([botao_arquivo], alignment="center"),
        ft.Row([botao_renomear_pasta], alignment="center"),
        ft.Row([botao_renomear_arquivo], alignment="center"),
        ft.Row([botao_listar_arquivo], alignment="center"),
        ft.Row([botao_excluir_arquivo], alignment="center"),
        ft.Row([botao_excluir_pasta], alignment="center"),
        ft.Row([informativo], alignment="center")
    )

ft.app(target=main)
