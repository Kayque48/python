print("Bem vindo a programa para calcular IMC\n vamos começar!")
peso = float(input("Primeiro, insira o seu peso:"))
altura = float(input("Agora a sua altura:"))

IMC = peso/(altura*altura)

print("\n")
print("Sua informações:")
print("peso = "+ str(peso) +"\n altura = "+ str(altura) + "\nIMC = "+str(IMC))

if IMC < 18.5:
    print("magreza")
elif IMC < 24.9:
    print("saudavel")
elif IMC < 25.9:
    print("sobrepeso")
elif IMC < 34.9:
    print("Obesidade I")
elif IMC < 39.9:
    print("Obesidade II")
elif IMC > 40:
    print("Obesidade III")