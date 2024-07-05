import os
import csv

# Inicializa o array de remédios
array_remedios = []

# Nome do arquivo CSV
csv_file = 'remedios.csv'

def ler_remedios_do_arquivo():
    global array_remedios
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            array_remedios = list(reader)

def salvar_remedios_no_arquivo():
    global array_remedios
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['nome', 'valor', 'ativo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(array_remedios)

def menu():
    print("""
    ███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░██╗░░░░░░█████╗░░█████╗░░█████╗░
    ██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗
    █████╗░░███████║██████╔╝██╔████╔██║███████║██║░░░░░██║░░██║██║░░╚═╝███████║
    ██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░░░░██║░░██║██║░░██╗██╔══██║
    ██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║██║░░██║███████╗╚█████╔╝╚█████╔╝██║░░██║
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝""")

    print("1. Cadastrar remédio")
    print("2. Listar remédios")
    print("3. Alterar estado do remédio")
    print("4. Sair")

def exibir_opcoes():
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            cadastrar_remedio()
        elif escolha == 2:
            listar_remedios()
        elif escolha == 3:
            alterar_estado_remedio()
        elif escolha == 4:
            print("Sair")
            print("""
        ████████████████████████████████████████████████████████████████████████
        █▄─█─▄█─▄▄─█▄─▄███─▄─▄─█▄─▄▄─███─▄▄▄▄█▄─▄▄─█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█░█
        ██▄▀▄██─██─██─██▀███─████─▄█▀███▄▄▄▄─██─▄█▀██─█▄█─███─▄▄▄██─▄─▄██─▄█▀█▄█
        ▀▀▀▄▀▀▀▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀""")
            salvar_remedios_no_arquivo()
        else:
            print("Opção Inválida")
    except ValueError:
        print("Opção Inválida, Tente Outra")

def cadastrar_remedio():
    os.system('cls')
    print("-- ℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕒𝕣 𝕣𝕖𝕞𝕖́𝕕𝕚𝕠 --")
    nome_remedio = input("Digite o nome do remédio: ")
    valor_remedio = float(input("Digite o valor do remédio: "))
    remedio = {'nome': nome_remedio, 'valor': valor_remedio, 'ativo': True}
    array_remedios.append(remedio)
    print(f"O remédio {nome_remedio} foi adicionado com sucesso!\n")
    salvar_remedios_no_arquivo()
    voltar_menu()

def listar_remedios():
    os.system('cls')
    print("-- 𝕃𝕚𝕤𝕥𝕒𝕣 𝕣𝕖𝕞𝕖́𝕕𝕚𝕠𝕤 --")
    for i, remedio in enumerate(array_remedios, 1):
        status = "Ativo" if remedio['ativo'] == "True" else "Inativo"
        print(f'{i} - Nome: {remedio["nome"]}, Valor: {remedio["valor"]}, Status: {status}')
    print("\n")
    voltar_menu()

def alterar_estado_remedio():
    try:
        escolha = int(input("Escolha o número do remédio para alterar o estado: "))
        if 1 <= escolha <= len(array_remedios):
            remedio = array_remedios[escolha - 1]
            remedio['ativo'] = "False" if remedio['ativo'] == "True" else "True"
            print(f"O estado do remédio {remedio['nome']} foi alterado para {'Ativo' if remedio['ativo'] else 'Inativo'}.\n")
            salvar_remedios_no_arquivo()
        else:
            print("Número do remédio inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
    voltar_menu()

def voltar_menu():
    escolha = input("Deseja voltar para o Menu? (y/n) ")
    if escolha.lower() == "y":
        main()
    else:
        print("Saiu!")
        print("""
        ████████████████████████████████████████████████████████████████████████
        █▄─█─▄█─▄▄─█▄─▄███─▄─▄─█▄─▄▄─███─▄▄▄▄█▄─▄▄─█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█░█
        ██▄▀▄██─██─██─██▀███─████─▄█▀███▄▄▄▄─██─▄█▀██─█▄█─███─▄▄▄██─▄─▄██─▄█▀█▄█
        ▀▀▀▄▀▀▀▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀""")
        salvar_remedios_no_arquivo()

def main():
    ler_remedios_do_arquivo()
    os.system('cls')
    menu()
    exibir_opcoes()

if __name__ == '__main__':
    main()
