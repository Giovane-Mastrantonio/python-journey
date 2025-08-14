# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: use cores.

def titulo(texto, cor=42):
    """Exibe um título colorido com bordas."""
    tamanho = len( texto ) + 4
    print( f"\033[1;{cor}m{' ' * tamanho}\033[m" )
    print( f"\033[1;{cor}m  {texto}  \033[m" )
    print( f"\033[1;{cor}m{' ' * tamanho}\033[m" )


def linha_ondulada():
    """Exibe uma linha ondulada colorida."""
    print( "\033[1;30;42m" + "~" * 42 + "\033[m" )


def mensagem_help(comando):
    """Exibe mensagem antes do help com fundo azul."""
    linha_ondulada()
    print( f"\033[1;30;46m  Acessando o manual do comando '{comando}'...  \033[m" )
    linha_ondulada()


def obter_comando():
    """Obtém comando do usuário com fundo escuro."""
    return input( "\033[7;97mFunção ou Biblioteca > \033[m" ).strip()


def executar_help(comando):
    """Executa o help do comando informado."""
    if comando == '':
        help()
    else:
        help( comando )


def processar_comando(comando):
    """Processa o comando digitado pelo usuário."""
    if comando.upper() == 'FIM':
        return False

    mensagem_help( comando )
    executar_help( comando )
    print()
    return True


def main():
    """Sistema Interactive Help do Python."""
    linha_ondulada()
    print( "\033[1;30;42m  SISTEMA DE AJUDA PyHELP            \033[m" )
    linha_ondulada()

    while True:
        comando = obter_comando()

        if not processar_comando( comando ):
            linha_ondulada()
            print( "\033[1;30;42m  SISTEMA DE AJUDA PyHELP            \033[m" )
            linha_ondulada()
            break


if __name__ == "__main__":
    main()
