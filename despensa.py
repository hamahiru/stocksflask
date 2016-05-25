despensa = {'Ura':'5', 'SinLactosa':'3'}

def despensa_lista():
    return despensa

def update(prod,kop):
    despensa[prod] = kop
    return despensa

def update_lista(prod,kop):
    despensa[prod] = kop
    return despensa
