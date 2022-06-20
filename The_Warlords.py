# ... after all the efforts, sir Ronald couldn't win the battle. He finally realized that this isn’t just a small fight,
# but a full-fledged battle, and he needs to apply all his experience to effectively manage his army.
# It looks like this time the outcome of the battle will be decided once and for all.

# In this mission you should add a new class Warlord(), which should be the subclass of the Warrior class and have the
# next characteristics:
# health = 100
# attack = 4
# defense = 2

# Also, when the Warlord is included in any of the armies, that particular army gets the new move_units() method which
# allows to rearrange the units of that army for the better battle result. The rearrangement is done not only before
# the battle, but during the battle too, each time the allied units die. The rules for the rearrangement are as follow:
# If there are Lancers in the army, they should be placed in front of everyone else.
# If there is a Healer in the army, he should be placed right after the first soldier to heal him during the fight.
# If the number of Healers is > 1, all of them should be placed right behind the first Healer.
# If there are no more Lancers in the army, but there are other soldiers who can deal damage, they also should be
# placed in first position, and the Healer should stay in the 2nd row (if army still has Healers).
# Warlord should always stay way in the back to look over the battle and rearrange the soldiers when it's needed.
# Every army can have no more than 1 Warlord.
# If the army doesn’t have a Warlord, it can’t use the move_units() method.


class Warrior:
    def __init__(self):
        self.health, self.max_hp = 50, 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0
        self.attack_range = 1
        self.heal_power = 0
        self.is_alive = True
        # self.weapons = {
        #     'Sword': Sword,
        #     'Shield': Shield,
        #     'GreatAxe': GreatAxe,
        #     'Katana': Katana,
        #     'MagicWand': MagicWand,
        # }

    def check_is_alive(self):
        if self.health <= 0:
            self.is_alive = False
        return self.is_alive

    def equip_weapon(self, weapon_name):
        self.health += weapon_name.bonus_health if self.health > 0 else 0
        self.max_hp += weapon_name.bonus_health if self.max_hp > 0 else 0
        self.attack += weapon_name.bonus_attack if self.attack > 0 else 0
        self.defense += weapon_name.bonus_defense if self.defense > 0 else 0
        self.vampirism += weapon_name.bonus_vampirism if self.vampirism > 0 else 0
        self.heal_power += weapon_name.bonus_heal_power if self.heal_power > 0 else 0


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
        self.vampirism = 50


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
        self.heal_power = 2

    def heal(self, healing_target):
        healing_target.health += self.heal_power if healing_target.health <= healing_target.max_hp - self.heal_power \
            else healing_target.max_hp - healing_target.health


class Weapon:
    def __init__(self, bonus_health=0, bonus_attack=0, bonus_defense=0, bonus_vampirism=0, bonus_heal_power=0):
        self.bonus_health = bonus_health
        self.bonus_attack = bonus_attack
        self.bonus_defense = bonus_defense
        self.bonus_vampirism = bonus_vampirism
        self.bonus_heal_power = bonus_heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__(bonus_health=5, bonus_attack=2)


class Shield(Weapon):
    def __init__(self):
        super().__init__(bonus_health=20, bonus_attack=-1, bonus_defense=2)


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(bonus_health=-15, bonus_attack=5, bonus_defense=-2, bonus_vampirism=10)


class Katana(Weapon):
    def __init__(self):
        super().__init__(bonus_health=-20, bonus_attack=6, bonus_defense=-5, bonus_vampirism=50)


class MagicWand(Weapon):
    def __init__(self):
        super().__init__(bonus_health=30, bonus_attack=3, bonus_heal_power=3)


class Army:
    def __init__(self):
        self.units = list()
        self.unit_types = {
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
            for key in self.unit_types.keys():
                if unit.__name__ == key:
                    self.units.append(self.unit_types[key]())


class Battle:
    def fight(self, army1, army2):
        while len(army1.units) > 0 and len(army2.units) > 0:
            while len(army1.units) > 1 and len(army2.units) > 1:
                if fight(unit_1=army1.units[0],
                         unit_2=army2.units[0],
                         unit_behind_1=army1.units[1],
                         unit_behind_2=army2.units[1]):
                    army2.units.remove(army2.units[0])
                else:
                    army1.units.remove(army1.units[0])
            if fight(unit_1=army1.units[0],
                     unit_2=army2.units[0]):
                army2.units.remove(army2.units[0])
            else:
                army1.units.remove(army1.units[0])
        return len(army1.units) > 0

    def straight_fight(self, army1, army2):
        while len(army1.units) > 0 and len(army2.units) > 0:
            dead_units = list()
            for count in range(min(len(army1.units), len(army2.units))):
                fight(army1.units[count], army2.units[count])
                if army1.units[count].is_alive:
                    dead_units.append(army2.units[count])
                else:
                    dead_units.append(army1.units[count])
            for unit in dead_units:
                if unit in army1.units:
                    army1.units.remove(unit)
                elif unit in army2.units:
                    army2.units.remove(unit)
        return len(army1.units) > 0


def attack(attacking_unit, defending_unit, attack_multiplier=float(1)):
    attack1 = int(attacking_unit.attack * attack_multiplier)
    defending_unit.health -= (attack1 - defending_unit.defense if defending_unit.defense < attack1 else 0)
    vampirism = 0
    if attacking_unit.vampirism > 0:
        vampirism = int((attack1 - defending_unit.defense) * (attacking_unit.vampirism / 100) if
                        defending_unit.defense < attack1 else 0)
    attacking_unit.health += vampirism if attacking_unit.health <= attacking_unit.max_hp - vampirism else 0


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

    ronald = Warlord()
    heimdall = Knight()

    assert fight(heimdall, ronald) == False

    my_army = Army()
    my_army.add_units(Warlord, 1)
    my_army.add_units(Warrior, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 2)

    enemy_army = Army()
    enemy_army.add_units(Warlord, 3)
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 2)
    enemy_army.add_units(Knight, 2)

    my_army.move_units()
    enemy_army.move_units()

    assert type(my_army.units[0]) == Lancer
    assert type(my_army.units[1]) == Healer
    assert type(my_army.units[-1]) == Warlord

    assert type(enemy_army.units[0]) == Vampire
    assert type(enemy_army.units[-1]) == Warlord
    assert type(enemy_army.units[-2]) == Knight

    # 6, not 8, because only 1 Warlord per army could be
    assert len(enemy_army.units) == 6

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
print("Coding complete? Let's try tests!")