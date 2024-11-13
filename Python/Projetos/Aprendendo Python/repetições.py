notas = []

for x in range(3):
    codigo_aluno = int(input("RM: "))
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
print(notas)

soma_notas = 0
contador_notas = 0

for i in notas:
    codigo_aluno = i[0]
    nota = i[1]
    print(" O RM ", codigo_aluno, "tirou a notas: ", nota)
    soma_notas += nota
    contador_notas += 1

media = soma_notas/contador_notas
print("A media total é: ", media)