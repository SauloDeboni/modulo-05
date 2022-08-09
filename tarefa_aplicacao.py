from tarefa_funcao import multiplo

# Aplicação solicita ao usuário um número natural

while True:
    natural = input("Digite um número inteiro ou \"sair\" para encerrar: ")

    if natural == "sair":
        break
    elif natural.isdigit() == False:
        print("Tente novamente! Apenas números são aceitos.")
        print()
    elif int(natural) < 0:
        print("Tente novamente! Apenas número positivos são aceitos.")
        print()
    else:
        print(multiplo(natural))
        print()

print("Você saiu da aplicação.")
print()
