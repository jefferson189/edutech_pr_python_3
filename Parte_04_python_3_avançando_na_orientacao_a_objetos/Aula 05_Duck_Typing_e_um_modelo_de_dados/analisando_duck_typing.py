class Listinha:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)

meu_objeto = Listinha([1, 2, 4])

contador = 0
for item in meu_objeto:
    contador += 1

if len(meu_objeto) == contador:
    print('São iguais!')
else:
    print('Não são iguais!')