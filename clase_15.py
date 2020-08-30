"""
Hacer una clase Player o Jugador que va a tener una lista de items.

Atributos del Player:
    - health (valor entre 0 y 100)
    - money
    - items (una lista con los items)

Metodos del Player:
    - sell(item) -> Busca el item dentro del player y lo vende (llama a item.sell()) 
    - throw(item) -> Busca el item dentro del player y lo tira
    - use(item) -> Busca el item dentro del player y lo usa
    - add_item(item) -> Agrega a la lista de items un item nuevo.

Si se trata de usar/vender/tirar un item que no se puede, debera lanzar una exception

 Hacer una clase abstracta Item, y crear las implementaciones para los siguientes tipos de items:
 - Sword               ($100)
 - Armor               ($150)
 - Shield               ($80)
 - Boots                ($50)
 - Ring                 ($10)
 - Helmet               ($50)
 - Granades              ($5)
 - Quest                   --
 - PotionMedium (20)    ($10)
 - PotionLarge (50)     ($25)

 Atributos del item:
    - price
    - quantity
    - description

Metodos del Item:
    - sell(player) -> Recibe un objeto jugador, le saca ese item, y le suma el dinero de lo que vale el item
    - throw(player) -> Recibe el objeto jugador y le saca ese item sin darle dinero
    - use(player) -> Solo para pociones, le sube la vida al jugador segun el tipo de pocion que sea.
 
RESTRICCIONES:
    - Quest items no se pueden vender ni tirar
    - Espadas/Armaduras/Escudo/Botas/Cascos no pueden ser cantidad > 1
"""

################## ERRORS ######################
class CannotUseError(Exception):
    pass

class CannotSellError(Exception):
    pass

class CannotThrowError(Exception):
    pass

################################################


################## PLAYER ######################
class Player():
    def __init__(self):
        self.health = 100
        self.items = []
        self.money = 0

    def sell(self, item): #Recibe un objeto jugador, le saca ese item, y le suma el dinero de lo que vale el item
        item.sell(self)        

    def throw(self): #Recibe el objeto jugador y le saca ese item sin darle dinero
        pass

    def use(self, item): #Solo para pociones, le sube la vida al jugador segun el tipo de pocion que sea
        item.use(self)

    def add_item(self, item): #Agrega a la lista de items un item nuevo
        self.items.append(item)


    """ metodos que cree por mi cuenta"""
    def recive_damage(self, damage_score):
        self.health -= damage_score
    
    def restore_health(self, restore_score):
        self.health += restore_score
        if self.health > 100:
            self.health = 100

    def is_alive(self):
        return self.health > 0

    def add_money(self, money):
        self.money += money

###############################################




################### ITEMS #####################

class Item():
    def __init__(self):
        self.price = None
        self.quantity = None
        self.description = None
        self.power = None
    
    def sell(self, player): #Recibe un objeto jugador, le saca ese item, y le suma el dinero de lo que vale el item
        player.items.remove(self)
        player.add_money(self.price)
        

    def throw(self, player): #Recibe el objeto jugador y le saca ese item sin darle dinero
        player.items.remove(self)

    def use(self, player): #Solo para pociones, le sube la vida al jugador segun el tipo de pocion que sea
        player.restore_health(self.power)
        self.quantity -= 1


class Sword(Item):
    def __init__(self):
        self.description = 'A Sword, it´s like a huge knife'
        self.quantity = 1
        self.price = 100
        self.power = 50
    
    def use(self, player):
        print('Take this MotherFucker! (you have attacked yourself?!?!?!)')
        player.recive_damage(self.power)
        print('Health = {}'.format(player.health))
        if not player.is_alive():
            print('Game Over')
            exit()


class Armor(Item):
    def __init__(self):
        self.description = 'A Regular armor, to be "regular" safe'
        self.quantity = 1
        self.price = 150

    def use(self, player):
        raise CannotUseError    

class Shield(Item):
    def __init__(self):
        self.description = 'Shield happens'
        self.quantity = 1
        self.price = 80
    
    def use(self, player):
        print('This method will attack your opponent with the shield (your opponent may laugh at you)')


class Boots(Item):
    def __init__(self):
        self.description = 'Breaks down your straight-normative concepts'
        self.quantity = 1
        self.price = 50
    
    def use(self, player):
        raise CannotUseError

class Ring(Item):
    def __init__(self):
        self.description = 'Each day more asshole'
        self.quantity = 1
        self.price = 10

    def use(self, player):
        raise CannotUseError

class Helmet(Item):
    def __init__(self):
        self.description = 'Head protection'
        self.quantity = 1
        self.price = 5

    def use(self, player):
        raise CannotUseError

class Granade(Item):
    def __init__(self):
        self.description = 'Reduces opponent´s health'
        self.quantity = 5
        self.price = 50

    def use(self):
        print('This method will make an explotion on opponent´s area')

class Quest(Item):
    def __init__(self):
        self.description = 'An Item to solve a quest'
        self.quantity = 1
        self.price = 0

    def sell(self, player):
        raise CannotSellError

    def use(self, player):
        raise CannotUseError

    def throw(self, player):
        raise CannotThrowError


class PotionMedium(Item):
    def __init__(self):
        self.description = 'Restores a few health points'
        self.quantity = 1
        self.price = 10
        self.power = 20

    def sell(self, player):
        if self.quantity == 1:
            player.items.remove(self)
        else:
            self.quantity -=1



class PotionLarge(Item):
    def __init__(self):
        self.description = 'Restores many(?) health points'
        self.quantity = 1
        self.price = 25
        self.power = 50

    def sell(self, player):
        if self.quantity == 1:
            player.items.remove(self)
        else:
            self.quantity -=1



def test_player_cannot_use_armor():
    player = Player()
    armor = Armor()
    player.add_item(armor)
    try:
        player.use(armor)
        assert False, "Shouldn't be able to use equipment"
    except CannotUseError:
        print("Test passed")


def test_player_cannot_sell_quest_item():
    player = Player()
    quest_item = Quest()
    player.add_item(quest_item)
    try:
        player.sell(quest_item)
        assert False, "Shouldn't be able to sell quest item"
    except CannotSellError:
        print("Test passed")


def test_sell_item():
    player = Player()
    sword = Sword()
    player.add_item(sword)
    assert len(player.items) == 1
    previous_money = player.money
    player.sell(sword)
    assert len(player.items) == 0
    assert player.money == previous_money + 100, player.money
    print("Test passed")


def test_use_potion():
    player = Player()
    player.health = 20
    potion = PotionMedium()
    potion.quantity = 10
    player.add_item(potion)
    assert len(player.items) == 1
    player.use(potion)
    assert player.health == 40
    assert len(player.items) == 1
    assert potion.quantity == 9
    print("Test passed")


test_sell_item()
test_use_potion()
test_player_cannot_use_armor()
test_player_cannot_sell_quest_item()