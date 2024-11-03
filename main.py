# Função para verificar se um número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Testar a função para números de 1 a 100
for n in range(1, 101):
    if eh_primo(n):
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")
