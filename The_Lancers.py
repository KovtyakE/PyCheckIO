# ... the vampires fought fiercely. Judging by the course of the battle, Sir Ronald made the right decision, although
# not very ethically ambiguous.
# Suddenly, new soldiers joined the Umbert’s ranks - has he really got an ace up his sleeve? Lancers presented the
# fresh forces, which made Sir Ronald’s position increasingly difficult, lancers could attack two soldiers at once
# with their long spears. Something needed to be done with that…
# It seems that the Warrior, Knight, Defender and Vampire are not enough to win the battle. Let's add one more
# powerful unit type - the Lancer.
# Lancer should be the subclass of the Warrior class and should attack in a specific way - when he hits the other
# unit, he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly assaulted one (enemy
# defense makes the deal damage value lower - consider this).
# The basic parameters of the Lancer:
# health = 50
# attack = 6


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


if __name__ == "__main__":
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
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
