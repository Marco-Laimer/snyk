import sqlite3

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

# Solicitação de entrada do usuário
user_input = input("Digite o nome de usuário: ")

# Chamada da função de busca de usuário
search_user(user_input)