from collections.abc import Iterator, Iterable

class Soldier:
    def __init__(self, level):
        self.level = level

    def attack(self):
        return self.level * 1


class Jedi:
    def __init__(self, level):
        self.level = level

    def attack_with_saber(self):
        return self.level * 100


class StarWarsGame:
    def __init__(self, character):
        self.character = character

    def fight_enemy(self):
        print(f"You caused {self.character.attack()} of damage to the enemy")


class Adapter:
    def __init__(self, jedi):
        self.jedi = jedi

    def attack(self):
        return self.jedi.attack_with_saber()
    
#StarWarsGame(Soldier(5)).fight_enemy()
#StarWarsGame(Adapter(Jedi(20))).fight_enemy()

# =================================================================

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)
    

class IteratorDeck(Iterator):
    def __init__(self, cartas):
        self.cards = cartas
        self.card_pos = 0
    
    def __next__(self):
        try:
            card = self.cards[self.card_pos]
            self.card_pos += 1
            return card
        except IndexError:
            raise StopIteration()
        

class Baralho(Iterable):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)
    
    def __iter__(self):
        return IteratorDeck(self._cartas)
    
    def __str__(self) -> str:
        return f"{[carta for carta in self]}"
    
#baralho = Baralho()
#print(baralho)



    
