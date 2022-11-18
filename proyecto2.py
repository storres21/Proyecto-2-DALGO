"""
Nombre: Sofía Torres Ramírez.
 Código: 202014872

 Nombre: Juan Camilo Neira Campos
 Código: 201922746

 Nombre: Juan David Briceño Morales
 Código: 201812887
 """




from pkg_resources import compatible_platforms
import collections
import sys

def alfabeto_pandora(palabras):
    grafo= construir_grafo(palabras)
    try:
        return orden_topologico(grafo)
    except:
        return print("ERROR")
    

def construir_grafo(words):
    g = {c: [] for w in words for c in w}

    for i in range(1, len(words)):
        for c1, c2 in zip(words[i-1], words[i]):
            if c1 != c2:
                g[c1].append(c2)
                break

    for word in words:
        if len(word)>1:
            # for letter in range(len(word) - 1):
            #     lista = g.get(word[letter+1])
            #     print (lista)
            #     if word[letter] != word[letter + 1] and word[letter] not in lista:
            #         g[word[letter]].append(word[letter + 1])
            #         g[word[0]].append(word[letter+1])
            
            lista = g.get(word[1])
            #print (lista)
            if word[0] != word[1] and word[0] not in lista:
                g[word[0]].append(word[1])
            
    #print (g)
    return g

def find_first_letter(g):
    s = set()
    for l in g.values():
        for c in l:
            s.add(c)
    first_letter = [c for c in g if c not in s]
    if len(first_letter) != 1:
        raise Exception("no first letter %s" % first_letter)
    return first_letter[0]
    #return min(g.keys())

def explore(g, c, visited, result):
    if visited[c] == 1:
         raise Exception("ERROR")
    if visited[c] == 2:
        return
    visited[c] = 1
    for c2 in g[c]:
        explore(g, c2, visited, result)
    result.append(c)
    visited[c] = 2

def orden_topologico(g):
    visited = collections.defaultdict(lambda: 0)
    #visited = {}
    #visited = g
    result = []
    first_letter = find_first_letter(g)
    explore(g, first_letter, visited, result)
    result.reverse()
    return "".join(result)




# if __name__ == "__main__":
#     palabras =["ab", "ac", "cc", "cb"]
#     alfabeto_pandora(palabras)

#["ab", "ac", "cc", "cb"]
#["ab", "ah", "an", "mn", "mk"]
# ["xx", "xp", "pj", "jjj", "jjw"]
#["h", "hjh", "hjmh", "hm", "j", "jjm",  "m", "mh", "mmhj"]

#["arco", "barca", "cora", "ro"]
    

    
if __name__ == '__main__':
    numero_casos = int(sys.stdin.readline())
    for i in range(numero_casos):
        n_paginas, n_palabras = sys.stdin.readline().split()
        n_paginas = int(n_paginas)
        n_palabras = int(n_palabras)
        j=0
        palabras = []
        dict ={}
        for pagina in range(n_paginas):
            lista = (sys.stdin.readline().split())
            dict[int(lista[0])] = lista[1:]
        while j<n_paginas:
            cadena = dict[j]
            for palabra in cadena:
                palabras.append(palabra)
            j+=1
        print(alfabeto_pandora(palabras))

