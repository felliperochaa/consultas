import time
from usuarios import registrar_usuario, autenticar_usuario
from consultas import marcar_consulta, cancelar_consulta, listar_consultas
from datetime import datetime

def menu_principal():
    while True:
        print("Bem-vindo ao Sistema de Agendamento de Consultas!")
        print("1. Registrar usuário")
        print("2. Login")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            email = input("Digite o e-mail: ")
            cpf = input("Digite o CPF: ")
            senha = input("Digite a senha: ")
            if registrar_usuario(email, cpf, senha):
                print("Usuário registrado com sucesso!")
            else:
                print("Erro: Já existe um usuário com esse e-mail ou CPF.")
        
        elif opcao == '2':
            email_ou_cpf = input("Digite o e-mail ou CPF: ")
            senha = input("Digite a senha: ")
            usuario = autenticar_usuario(email_ou_cpf, senha)
            
            if usuario:
                print("Login realizado com sucesso!")
                menu_usuario(usuario)
            else:
                print("E-mail/CPF ou senha incorretos.")
        
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario(usuario):
    while True:
        print("\n--- Menu de Consultas ---")
        print("1. Marcar consulta")
        print("2. Ver consultas agendadas")
        print("3. Cancelar consulta")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            data_consulta = input("Digite a data da consulta (dd/mm/yyyy): ")
            horario = input("Digite o horário da consulta (HH:MM): ")
            try:
                data = datetime.strptime(data_consulta, '%d/%m/%Y').date()
                consulta = marcar_consulta(usuario, data, horario)
                if consulta:
                    print(f"Consulta marcada para {data_consulta} às {horario}.")
                else:
                    print("Você já tem uma consulta nessa data e horário.")
            except ValueError:
                print("Data ou horário inválidos. Tente novamente.")
        
        elif opcao == '2':
            consultas = listar_consultas(usuario)
            if consultas:
                print("Consultas agendadas:")
                for i, consulta in enumerate(consultas, start=1):
                    print(f"{i}. {consulta['data']} às {consulta['horario']}")
            else:
                print("Você não tem consultas agendadas.")
        
        elif opcao == '3':
            consultas = listar_consultas(usuario)
            if not consultas:
                print("Você não tem consultas para cancelar.")
                continue
            for i, consulta in enumerate(consultas, start=1):
                print(f"{i}. {consulta['data']} às {consulta['horario']}")
            try:
                indice = int(input("Digite o número da consulta que deseja cancelar: "))
                if 1 <= indice <= len(consultas):
                    confirmacao = input(f"Tem certeza que deseja cancelar a consulta {indice}? (s/n): ").lower()
                    if confirmacao == 's':
                        if cancelar_consulta(usuario, indice - 1):
                            print("Consulta cancelada com sucesso.")
                        else:
                            print("Erro ao cancelar a consulta.")
                    else:
                        print("Cancelamento abortado.")
                else:
                    print("Número de consulta inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
        
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()