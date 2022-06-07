# In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we have only 2
# types of units - the Warriors and Knights. Let's add another one - the Defender.It should be the subclass of the
# Warrior class and have an additional defense parameter, which helps him to survive longer.When another unit hits
# the defender, he loses a certain amount of his health according to the next formula: enemy attack - *self-defense*( if
# enemy attack > self defense).Otherwise, the defender doesn't lose his health. The basic parameters of the Defender:
# health = 60
# attack = 3
# defense = 2
#
# Input: The warriors and armies.
# Output: The result of the battle(True or False).
#
# How it is used: For the computer games development.
#
# Note: From now on, the tests from "check" part will use another type of warrior: the rookie.Its code is
#
# class Rookie(Warrior):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.health = 50
#         self.attack = 1
#
# Precondition: 3 types of units


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
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


class Army:
    def __init__(self):
        self.army = list()
        self.units = {
            'Knight': Knight,
            'Warrior': Warrior,
            'Defender': Defender,
            'Rookie': Rookie,
        }

    def add_units(self, unit, count):
        for iteration in range(count):
            for key in self.units.keys():
                if unit.__name__ == key:
                    self.army.append(self.units[key]())


class Battle:
    def fight(self, army1, army2):
        while len(army1.army) != 0 and len(army2.army) != 0:
            print(army1.army, army2.army)
            for unit1 in army1.army:
                for unit2 in army2.army:
                    if fight(unit_1=unit1, unit_2=unit2):
                        army2.army.remove(unit2)
                        continue
                    else:
                        break
                if not unit1.is_alive:
                    army1.army.remove(unit1)
            if len(army1.army) == 0:
                print(0)
                return False
            elif len(army2.army) == 0:
                print(1)
                return True


def fight(unit_1, unit_2):
    while unit_1.check_is_alive() and unit_2.check_is_alive():
        unit_2.health -= (unit_1.attack - unit_2.defense if unit_2.defense < unit_1.attack else 0)
        if unit_2.check_is_alive():
            unit_1.health -= (unit_2.attack - unit_1.defense if unit_1.defense < unit_2.attack else 0)
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

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
