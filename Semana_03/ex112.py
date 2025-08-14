# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado
# dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a
# função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadesCeV import dado
from utilidadesCeV.moeda import resumo

# Exemplo de uso
if __name__ == "__main__":
    preco = dado.leiaDinheiro( "Digite o preço: R$ " )
    resumo(preco)