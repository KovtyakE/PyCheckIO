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


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6
        self.attack_range = 2


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
        }

    def add_units(self, unit, count):
        for iteration in range(count):
            for key in self.units.keys():
                if unit.__name__ == key:
                    self.army.append(self.units[key]())


class Battle:
    def fight(self, army1, army2):
        while len(army1.army) != 0 and len(army2.army) != 0:
            unit_behind_1 = None
            unit_behind_2 = None
            if len(army2.army) > 1 and army1.army[0].attack_range == 2:
                unit_behind_2 = army2.army[1]
            if len(army1.army) > 1 and army2.army[0].attack_range == 2:
                unit_behind_1 = army1.army[1]
            if fight(unit_1=army1.army[0],
                     unit_2=army2.army[0],
                     unit_behind_1=unit_behind_1,
                     unit_behind_2=unit_behind_2):
                army2.army.remove(army2.army[0])
            else:
                army1.army.remove(army1.army[0])
            if len(army1.army) == 0:
                return False
            elif len(army2.army) == 0:
                return True


def attack(attacking_unit, defending_unit, attack_multiplier=float(1)):
    attack1 = int(attacking_unit.attack * attack_multiplier)
    defending_unit.health -= (attack1 - defending_unit.defense if defending_unit.defense < attack1 else 0)
    attacking_unit.health += int((attack1 - defending_unit.defense) * attacking_unit.vampirism if defending_unit.defense < attack1 else 0)


def fight(unit_1, unit_2, unit_behind_1=None, unit_behind_2=None):
    while unit_1.check_is_alive() and unit_2.check_is_alive():
        attack(attacking_unit=unit_1, defending_unit=unit_2, attack_multiplier=1)
        if unit_behind_2:
            attack(attacking_unit=unit_1, defending_unit=unit_behind_2, attack_multiplier=0.5)
        if unit_2.check_is_alive():
            attack(attacking_unit=unit_2, defending_unit=unit_1, attack_multiplier=1)
            if unit_behind_1:
                attack(attacking_unit=unit_2, defending_unit=unit_behind_1, attack_multiplier=0.5)
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
