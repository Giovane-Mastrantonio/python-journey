# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
# a possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leia Float() com a mesma funcionalidade.

def leiaInt(mensagem):
    """
    Lê um número inteiro com validação completa.
    Trata casos de entrada inválida sem usar try/except.
    Se o usuário não digitar nada, retorna None.
    """
    while True:
        entrada = input( mensagem ).strip()

        # Verifica se a entrada está vazia (usuário não quer digitar)
        if not entrada:
            print( "Usuário preferiu não digitar esse número." )
            return None

        # Verifica se é apenas o sinal negativo
        if entrada == '-':
            print( "ERRO! Digite um número inteiro válido." )
            continue

        # Verifica se contém apenas dígitos (e opcionalmente sinal negativo no início)
        valido = True
        for i, char in enumerate( entrada ):
            if char == '-':
                if i != 0:  # Sinal negativo só pode estar no início
                    valido = False
                    break
            elif not char.isdigit():
                valido = False
                break

        if valido:
            # Converte manualmente para int
            numero = 0
            negativo = entrada.startswith( '-' )
            entrada_limpa = entrada.lstrip( '-' )

            for digit in entrada_limpa:
                numero = numero * 10 + int( digit )

            if negativo:
                numero = -numero

            return numero
        else:
            print( "ERRO! Digite um número inteiro válido." )


def leiaFloat(mensagem):
    """
    Lê um número real (float) com validação completa.
    Aceita vírgula ou ponto como separador decimal.
    Trata casos de entrada inválida sem usar try/except.
    Se o usuário não digitar nada, retorna None.
    """
    while True:
        entrada = input( mensagem ).strip()

        # Verifica se a entrada está vazia (usuário não quer digitar)
        if not entrada:
            print( "Usuário preferiu não digitar esse número." )
            return None

        # Substitui vírgula por ponto (padrão brasileiro)
        entrada = entrada.replace( ',', '.' )

        # Verifica casos especiais inválidos
        if entrada in ['-', '.', '-.']:
            print( "ERRO! Digite um número real válido." )
            continue

        # Verifica se contém apenas caracteres válidos
        valido = True
        pontos = 0

        for i, char in enumerate( entrada ):
            if char == '.':
                pontos += 1
                if pontos > 1:  # Mais de um ponto decimal
                    valido = False
                    break
            elif char == '-':
                if i != 0:  # Sinal negativo só pode estar no início
                    valido = False
                    break
            elif not char.isdigit():
                valido = False
                break

        if not valido:
            print( "ERRO! Digite um número real válido." )
            continue

        # Separa parte inteira e decimal
        if '.' in entrada:
            inteira, decimal = entrada.split( '.' )
        else:
            inteira, decimal = entrada, '0'

        # Ajusta partes vazias
        if inteira == '' or inteira == '-':
            inteira = '0' if inteira == '' else '-0'
        if decimal == '':
            decimal = '0'

        # Verifica se as partes são válidas
        if not (inteira.lstrip( '-' ).isdigit() and decimal.isdigit()):
            print( "ERRO! Digite um número real válido." )
            continue

        # Converte manualmente para float
        numero = 0.0
        negativo = inteira.startswith( '-' )
        inteira_limpa = inteira.lstrip( '-' )

        # Converte parte inteira
        for digit in inteira_limpa:
            numero = numero * 10 + int( digit )

        # Converte parte decimal
        if decimal != '0':
            decimal_valor = 0.0
            for digit in decimal:
                decimal_valor = decimal_valor * 10 + int( digit )
            numero += decimal_valor / (10 ** len( decimal ))

        if negativo:
            numero = -numero

        return numero


def main():
    """Demonstração das funções leiaInt() e leiaFloat()."""
    print( "=== TESTE DAS FUNÇÕES DE LEITURA ===\n" )

    # Testando leiaInt()
    print( "📊 Testando leiaInt():" )
    n = leiaInt( "Digite um Inteiro: " )

    # Se o usuário não digitou o inteiro, para a execução
    if n is None:
        # Ainda tenta ler o real para mostrar a mensagem
        f = leiaFloat( "Digite um Real: " )
        if f is None:
            print( f"O valor inteiro digitado foi {0 if n is None else n} e o real foi {0 if f is None else f}" )
        return

    # Testando leiaFloat()
    print( "📊 Testando leiaFloat():" )
    f = leiaFloat( "Digite um Real: " )

    # Se o usuário não digitou o real, para a execução
    if f is None:
        print( f"O valor inteiro digitado foi {n} e o real foi {0 if f is None else f}" )
        return

    # Se chegou até aqui, ambos foram digitados
    print( f"O valor inteiro digitado foi {n} e o real foi {f}" )

if __name__ == "__main__":
    main()