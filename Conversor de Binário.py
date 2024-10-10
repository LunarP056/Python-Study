print("Conversor de Decimal para Binário\n")
valor = input("Digite o número que você deseja converter para decimal:\n")
tamanho = len(str(valor)) #Arquiva o número de algarismos
int(tamanho) 
resultado = 0

for i in range(tamanho):
    index = tamanho - (i+1) #Indica a posição 
    digito = valor[index]
    resultado += (int(digito) * (2**i))

print("O valor em decimal é: " + (str)(resultado))