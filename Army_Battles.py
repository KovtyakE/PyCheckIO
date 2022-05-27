# In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But
# let's move to something that feels a little more epic - the armies! In this mission your task is to add new classes
# and functions to the existing ones. The new class should be the Army and have the method add_units() - for adding
# the chosen amount of units to the army. The first unit added will be the first to go to fight, the second will be
# the second, ...
# Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
# The battles occur according to the following principles:
# at first, there is a duel between the first warrior of the first army and the first warrior of the second army.
# As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the
# surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the
# armies die. In this case, the fight() function should return True , if the first army won, or False , if the second
# one was stronger.
# Note that army 1 have the advantage to start every fight!


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

    def check_is_alive(self):
        if self.health <= 0:
            self.is_alive = False
        return self.is_alive


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:
    def __init__(self):
        self.army = list()

    def add_units(self, unit, count):
        for iteration in range(count):
            if unit.__name__ == 'Knight':
                self.army.append(Knight())
            elif unit.__name__ == 'Warrior':
                self.army.append(Warrior())


class Battle:
    def fight(self, army1, army2):
        while len(army1.army) != 0 and len(army2.army) != 0:
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
                return False
            elif len(army2.army) == 0:
                return True


def fight(unit_1, unit_2):
    while unit_1.check_is_alive() and unit_2.check_is_alive():
        unit_2.health -= unit_1.attack
        if unit_2.check_is_alive():
            unit_1.health -= unit_2.attack
    return unit_1.check_is_alive()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")