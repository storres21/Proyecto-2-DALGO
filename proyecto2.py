# {a: [b, c]} means a is before b and c



import collections


def build_graph(words):
    g = {c: [] for w in words for c in w}
    for word in words:
        if len(word)>1:
            # for letter in range(len(word) - 1):
            #     lista = g.get(word[letter+1])
            #     print (lista)
            #     if word[letter] != word[letter + 1] and word[letter] not in lista:
            #         g[word[letter]].append(word[letter + 1])
            #         g[word[0]].append(word[letter+1])
            
            lista = g.get(word[1])
            print (lista)
            if word[0] != word[1] and word[0] not in lista:
                g[word[0]].append(word[1])
            
            
    for i in range(1, len(words)):
        for c1, c2 in zip(words[i-1], words[i]):
            if c1 != c2:
                g[c1].append(c2)
                break
    print (g)
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

def topo_sort(g):
    visited = collections.defaultdict(lambda: 0)
    result = []
    first_letter = find_first_letter(g)
    explore(g, first_letter, visited, result)
    result.reverse()
    return "".join(result)

def sort_alphabet(words):
    return topo_sort(build_graph(words))


if __name__ == "__main__":
    words =["ab", "ac", "cc", "cb"]
    print(sort_alphabet(words))

#["ab", "ah", "an", "mn", "mk"]
# ["xx", "xp", "pj", "jjj", "jjw"]
#["h", "hjh", "hjmh", "m", "mh", "mmhj","hm", "j", "jjm"]
    