import sqlite3
import subprocess

def search_user(username):
    # Simulação de consulta SQL insegura
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    
    # Conexão com o banco de dados SQLite (exemplo)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Execução da consulta
    cursor.execute(query)

    # Obtenção dos resultados
    results = cursor.fetchall()

    # Exibição dos resultados
    print(results)

def execute_command(command):
    subprocess.run(command, shell=True)

# Solicitação de entrada do usuário
user_input_sql = input("Digite o nome de usuário para a consulta SQL: ")
user_input_command = input("Digite o comando a ser executado: ")

# Chamada da função de busca de usuário
search_user(user_input_sql)

# Execução do comando (vulnerabilidade)
execute_command(user_input_command)
