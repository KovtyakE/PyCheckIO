# The flocks of crows circled over the battlefield. Many brave warriors have fallen in this battle, many have continued
# to fight. "If this goes on, we’ll simply kill each other, and there will be no winners - we’ll all lose." - reflected
# Sir Ronald, watching a bleak picture in front of him. "I have to make an important decision. I know what it’ll cost,
# but now that’s the only thing that can save us all..."
# A long time ago, when he was often in search of trouble and adventure, he went to hunt a witch who had a huge bounty
# on her head. The bloody creature was able to save her life by persuading the knight to take a gift from her - a vial
# of vampire blood. This blood poured into the dying man’s mouth could bring him back to life in vampire form.
# Is it really the day when he has to use it?.. It seemed to be the only way to win this battle. Sir Ronald began to
# lean over the barely living bodies of his knights, who were lying beside him. To each of them he said:
# - "Drink. You’ll be given a new life..."

# So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic and add another
# type - the Vampire! Vampire should be the subclass of the Warrior class and have the additional vampirism parameter,
# which helps him to heal himself. When the Vampire hits the other unit, he restores his health by +50% of the
# dealt damage (enemy defense makes the dealt damage value lower).
# The basic parameters of the Vampire:
# health = 40
# attack = 4
# vampirism = 50%
# You should store vampirism attribute as an integer (50 for 50%). It will be needed to make this solution evolutes
# to fit one of the next challenges of this saga.


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0
        self.is_alive = True

    def check_is_alive(self):
        if self.health <= 0:
            self.is_alive = False
        return self.is_alive


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 60
        self.defense = 2


class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 1


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Army:
    def __init__(self):
        self.army = list()
        self.units = {
            'Knight': Knight,
            'Warrior': Warrior,
            'Defender': Defender,
            'Rookie': Rookie,
            'Vampire': Vampire,
        }

    def add_units(self, unit, count):
        for iteration in range(count):
            for key in self.units.keys():
                if unit.__name__ == key:
                    self.army.append(self.units[key]())


class Battle:
    def fight(self, army1, army2):
        while len(army1.army) != 0 and len(army2.army) != 0:
            if fight(unit_1=army1.army[0], unit_2=army2.army[0]):
                army2.army.remove(army2.army[0])
            if not army1.army[0].is_alive:
                army1.army.remove(army1.army[0])
            if len(army1.army) == 0:
                return False
            elif len(army2.army) == 0:
                return True


def fight(unit_1, unit_2):
    while unit_1.check_is_alive() and unit_2.check_is_alive():
        unit_2.health -= (unit_1.attack - unit_2.defense if unit_2.defense < unit_1.attack else 0)
        unit_1.health += int((unit_1.attack - unit_2.defense) * unit_1.vampirism if
                             unit_2.defense < unit_1.attack else 0)
        if unit_2.check_is_alive():
            unit_1.health -= (unit_2.attack - unit_1.defense if unit_1.defense < unit_2.attack else 0)
            unit_2.health += int((unit_2.attack - unit_1.defense) * unit_2.vampirism if
                                 unit_1.defense < unit_2.attack else 0)
    return unit_1.check_is_alive()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
