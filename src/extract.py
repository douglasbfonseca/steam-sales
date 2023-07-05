
def extract_data():
    with open ('data/html-pagina.txt', 'r', encoding='utf-8') as arquivo:
        source = arquivo.read()
    return source