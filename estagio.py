#ESSE PROGRAMA RETORNA QUANTAS VOGAIS EXISTEM NA PALAVRA PARALELEPÍPEDO
vogais = 'aáãeéêiíîoòôõuúû'
def vogal(c):
    return c.lower() in 'aáãeéêiíîoòôõuúû'

palavra = 'paralelepípedo'
vogais = [letra for letra in palavra if vogal(letra)]
print(len(vogais))
