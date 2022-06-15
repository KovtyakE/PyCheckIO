# ... the battle lasted long enough and Sir Ronald have sent a messenger to the castle who had to deliver an order:
# "Open the weapons storehouse and bring everything to the battlefield." The last serious war has ended a long time ago,
# so the arsenal wasn’t too impressive, but one could find a few useful things, like better swords and shields,
# two-handed battle axes, and even the quite rare for these places, katana and wands.
# Perhaps, those weapons can turn the battle around...
# In this mission you should create a new class Weapon(health, attack, defense, vampirism, heal_power) which will equip
# your soldiers with weapons. Every weapon's object will have the parameters that will show how the soldier's
# characteristics change while he uses this weapon. Assume that if the soldier doesn't have some of the characteristics
# (for example, defense or vampirism), but the weapon have those, these parameters don't need to be added to the
# soldier.
#
# The parameters list:
# health - add to the current health and the maximum health of the soldier this modificator;
# attack - add to the soldier's attack this modificator;
# defense - add to the soldier's defense this modificator;
# vampirism - increase the soldier’s vampirism to this number (in %. So vampirism = 20 means +20%);
# heal_power - increase the amount of health which the healer restore for the allied unit.
#
# All parameters could be positive or negative, so when a negative modificator is being added to the soldier’s stats,
# they are decreasing, but none of them can be less than 0.
#
# Let’s look at this example: vampire (basic parameters: health = 40, attack = 4, vampirism = 50%) equip the
# Weapon(20, 5, 2, -60, -1). The vampire has the health and the attack, so they will change - health will grow up to
# 60 (40 + 20), attack will be 9 (4 + 5). The vampire doesn’t have defense or the heal_power, so these weapon
# modificators will be ignored. The weapon's vampirism modificator -60% will work as well. The standard vampirism
# value is only 50%, so we’ll get -10%. But, as we said before, the parameters can’t be less than 0, so the vampirism
# after all manipulations will be just 0%.
#
# Also you should create a few standard weapons classes, which should be the subclasses of the Weapon. Here’s their
# list:
# Sword - health +5, attack +2
# Shield - health +20, attack -1, defense +2
# GreatAxe - health -15, attack +5, defense -2, vampirism +10%
# Katana - health -20, attack +6, defense -5, vampirism +50%
# MagicWand - health +30, attack +3, heal_power +3
#
# And finally, you should add an equip_weapon(weapon_name) method to all of the soldiers classes. It should equip the
# chosen soldier with the chosen weapon.
# This method also should work for the units in the army. You should hold them in the list and use it like this:
# my_army.units[0].equip_weapon(Sword()) - equip the first soldier with the sword.
#
# Notes:
# While healing (both vampirism and health restored by the healer), the health can’t be greater than the maximum amount
# of health for this unit (with consideration of all of the weapon's modificators).
# If the heal from vampirism is float (for example 3.6, 1.1, 2.945), round it down in any case. So 3.6 = 3, 1.1 = 1,
# 2.945 = 2.
# Every soldier can be equipped with any number of weapons and get all their bonuses, but if he wears too much weapons
# with the negative health modificator and his health is lower or equal 0 - he is as good as dead, which is actually
# pretty dead in this case.


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

    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapon(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    ogre.health == 125
    lancelot.attack == 17
    richard.defense == 4
    eric.vampirism == 200
    freelancer.health == 15
    priest.heal_power == 5

    fight(ogre, eric) == False
    fight(priest, richard) == False
    fight(lancelot, freelancer) == True

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()

    battle.fight(my_army, enemy_army) == True
print("Coding complete? Let's try tests!")
