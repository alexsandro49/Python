#Verifica a conexão com um site, trantando os possíveis erros.

import urllib
import urllib.request

link = 'http://pudim.com.br'
try:
    site = urllib.request.urlopen(link)
except urllib.error.URLError:
    print(f'\033[31mO site {link[7:]} não está acessível no momento!\033[m')
else:
    print(f'\033[32mSite {link[7:]} foi acessado com sucesso!\033[m')
