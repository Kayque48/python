import os

# criando uma lista vazia
mensagens = []

# adicionando nome ao usuário
nome = input('Seu nickname: ')

# criando uma repetição infinita
while True:
    
    # limpar o terminal a cada ciclo
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # confere se tem mensagens gravadas
    if len(mensagens) > 0:
        # exibe as mensagens gravadas
        for m in mensagens:
            print(m['nome'], '-', m['texto'])
            
    print('_______________________________________________________________________________________________________________')
    
    # obtendo texto
    texto = input('Mensagem: ')
    # encerra o loop
    if texto == '/end':
        break
    
    # adicionar mensagens na lista
    mensagens.append({'nome': nome, 'texto': texto})
