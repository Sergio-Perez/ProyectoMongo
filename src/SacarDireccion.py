import requests
from bs4 import BeautifulSoup

def numpags(pagina):
    if pagina == 1:
        r = list(range(0,1))
    elif pagina > 1:
        r = list(range(0,pagina*10,10))
    else:
        r = [-1]
    return r

def ExtractDireccion(donde, elque, paginas):
    
    r = numpags(paginas)
    nombres=[]
    adress=[]
    
    if len(r) >= 3 or r[0] == -1:
        print("Exceso de páginas, máximo 3 páginas (nos pueden banear) o número de páginas inválido")
    else:
        
        for e in r:
            
            url =f"https://www.yelp.es/search?find_desc={elque}&find_loc={donde}&start={e}"
            data = requests.get(url)
            soup = BeautifulSoup(data.text)
            
            sacandoNombre = [e.text.split("\xa0") for e in soup.find_all('h4')]
            
            nombre = list(map(lambda s: s[1],sacandoNombre))
           
            nombres += nombre
            
            direccion = [e.text for e in soup.find_all('address')]
            
            adress += direccion
            
    return list(zip( nombres,adress))