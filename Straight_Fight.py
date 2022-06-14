# ...despite all of the tactical measures that have been undertaken, neither side still hasn’t had a victory.
# Therefore, the two army commanders decided to change tactics and immediately arrange a battle where all survived
# soldiers of one armie will be fighting all of the survivors of the other.
# A new unit type won’t be added in this mission, but instead we’ll add a new tactic - straight_fight(army_1, army_2).
# It should be the method of the Battle class and it should work as follows:
# at the beginning there will be a few duels between each pair of soldiers from both armies (the first unit against
# the first, the second against the second and so on). After that all dead soldiers will be removed and the process
# repeats until all soldiers of one of the armies will be dead. Armies might not have the same number of soldiers.
# If a warrior doesn’t have an opponent from the enemy army - we’ll automatically assume that he’s won a duel (for
# example - 9th and 10th units from the first army, if the second has only 8 soldiers).


class Warrior:
    def __init__(self):
        self.health, self.max_hp = 50, 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0
        self.attack_range = 1
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
        self.health, self.max_hp = 60, 60
        self.defense = 2


class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.health, self.max_hp = 50, 50
        self.attack = 1


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health, self.max_hp = 40, 40
        self.attack = 4
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.attack_range = 2


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health, self.max_hp = 60, 60
        self.attack = 0
        self.heal_value = 2

    def heal(self, healing_target):
        healing_target.health += self.heal_value if healing_target.health <= healing_target.max_hp - self.heal_value \
            else healing_target.max_hp - healing_target.health


class Army:
    def __init__(self):
        self.army = list()
        self.units = {
            'Knight': Knight,
            'Warrior': Warrior,
            'Defender': Defender,
            'Rookie': Rookie,
            'Vampire': Vampire,
            'Lancer': Lancer,
            'Healer': Healer,
        }

    def add_units(self, unit, count):
        for iteration in range(count):
            for key in self.units.keys():
                if unit.__name__ == key:
                    self.army.append(self.units[key]())


class Battle:
    def fight(self, army1, army2):
        while len(army1.army) > 0 and len(army2.army) > 0:
            while len(army1.army) > 1 and len(army2.army) > 1:
                if fight(unit_1=army1.army[0],
                         unit_2=army2.army[0],
                         unit_behind_1=army1.army[1],
                         unit_behind_2=army2.army[1]):
                    army2.army.remove(army2.army[0])
                else:
                    army1.army.remove(army1.army[0])
            if fight(unit_1=army1.army[0],
                     unit_2=army2.army[0]):
                army2.army.remove(army2.army[0])
            else:
                army1.army.remove(army1.army[0])
        return len(army1.army) > 0

    def straight_fight(self, army1, army2):
        while len(army1.army) > 0 and len(army2.army) > 0:
            dead_units = list()
            for count in range(min(len(army1.army), len(army2.army))):
                fight(army1.army[count], army2.army[count])
                if army1.army[count].is_alive:
                    dead_units.append(army2.army[count])
                else:
                    dead_units.append(army1.army[count])
            for unit in dead_units:
                if unit in army1.army:
                    army1.army.remove(unit)
                elif unit in army2.army:
                    army2.army.remove(unit)
        return len(army1.army) > 0


def attack(attacking_unit, defending_unit, attack_multiplier=float(1)):
    attack1 = int(attacking_unit.attack * attack_multiplier)
    defending_unit.health -= (attack1 - defending_unit.defense if defending_unit.defense < attack1 else 0)
    attacking_unit.health += int((attack1 - defending_unit.defense) * attacking_unit.vampirism if
                                 defending_unit.defense < attack1 else 0)


def fight(unit_1, unit_2, unit_behind_1=None, unit_behind_2=None):
    while unit_1.check_is_alive() and unit_2.check_is_alive():
        attack(attacking_unit=unit_1, defending_unit=unit_2, attack_multiplier=1)
        if unit_behind_2 and isinstance(unit_1, Lancer):
            attack(attacking_unit=unit_1, defending_unit=unit_behind_2, attack_multiplier=0.5)
        if isinstance(unit_behind_1, Healer):
            unit_behind_1.heal(unit_1)
        if unit_2.check_is_alive():
            attack(attacking_unit=unit_2, defending_unit=unit_1, attack_multiplier=1)
            if unit_behind_1 and isinstance(unit_2, Lancer):
                attack(attacking_unit=unit_2, defending_unit=unit_behind_1, attack_multiplier=0.5)
            if isinstance(unit_behind_2, Healer):
                unit_behind_2.heal(unit_2)
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
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

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
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    army_5 = Army()
    army_5.add_units(Warrior, 10)

    army_6 = Army()
    army_6.add_units(Warrior, 6)
    army_6.add_units(Lancer, 5)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    assert battle.straight_fight(army_5, army_6) == False
print("Coding complete? Let's try tests!")
