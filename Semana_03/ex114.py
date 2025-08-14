# Crie um código em Python que teste se o site www.mastrantonio.com.br está
# acessível pelo computador usado.
# Ao executar o código deve aparecer a mensagem:
# Consegui acessar o site do Mastrantonio com sucesso!
import urllib
from time import sleep
from urllib import request, error

try:
    site = urllib.request.urlopen('http://www.mastrantonio.com.br')
except error.URLError:
    print( "Testando acesso ao site" )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print('\033[1;31mO site Mastrantonio não está acessível no momento\033[0m')
else:
    print( "Testando acesso ao site" )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print( '.', end='', flush=True )
    sleep( 1 )
    print('\033[1;32mConsegui acessar o site Mastrantonio\033[0m')

