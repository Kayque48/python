def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def mutiplicar(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

while True:
    num1 = float(input("Insira o primeiro valor da operação: "))
    num2 = float(input("Insira o segundo valor da operação: "))
    
    op = input("Digite a operação desejada:")
    
    if op == "soma":
        resultado = somar(num1, num2)
        print(num1, "+", num2, "=", resultado)
        
    elif op == "subtrair":
        resultado = subtrair(num1, num2)
        print(num1, "+", num2, "=", resultado)
        
    elif op == "mutiplicar":
        resultado = mutiplicar(num1, num2)
        print(num1, "+", num2, "=", resultado)
    
    elif op == "dividir":
        resultado = divisao(num1, num2)
        print(num1, "+", num2, "=", resultado)
    
    elif op == "end":
        break