pokemon = ["pikachu", "raichu", "charmander","charizard"]

def elements(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    elements(list,idx+1)

elements(pokemon)