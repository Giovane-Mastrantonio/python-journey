# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.

from ex107 import moeda
# Solicitando o preço ao usuário (como mostrado na imagem)
preco = float(input("Digite o preço: R$ "))
# Chamando a função resumo() que exibirá as informações formatadas
moeda.resumo(preco)