# Tratamento de erros
# try, except, else, finally

teste = True

try:
    a = 10
    b = 0
    print (a / b)
except ZeroDivisionError:
    if teste:
        raise # Exibe em que linha está o erro
    print("Não é possível dividir por zero!")