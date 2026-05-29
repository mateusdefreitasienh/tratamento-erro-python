# Tratamento de erros
# try, except, else, finally

# Erro de divisão

# teste = True

# try:
#     a = 10
#     b = 0
#     print (a / b)
# except ZeroDivisionError:
#     if teste:
#         raise # Exibe em que linha está o erro
#     print("Não é possível dividir por zero!")

# erro de index
# try:
#     lista = [1, 2, 3]
#     print(lista[5])
# except IndexError:
#     print("Índice fora do intervalo")

# Tratamento de erro completo

while True:
    try:
        num = int(input("Digite um numero: "))
        print(f"Você digitou: {num}")
        break
    except ValueError:
        print("Valor inválido")
    else:
        print(f"Você digitou: {num}")
    finally:
        print("Fim do bloco try/catch")