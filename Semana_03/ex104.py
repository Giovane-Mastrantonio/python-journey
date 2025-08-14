# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função
# input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Exemplo: n=leiaInt('Digite um número').
def leiaInt(mensagem):
    """Lê um número inteiro com validação."""
    while True:
        entrada = input(mensagem)
        if entrada.lstrip('-').isdigit():
            return int(entrada)
        print("ERRO! Digite um número inteiro válido.")


def main():
    """Demonstração da função leiaInt()."""
    n = leiaInt("Digite um número: ")
    print(f"Você acabou de digitar o número {n}")


if __name__ == "__main__":
    main()