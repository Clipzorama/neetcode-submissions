import random

class Character:

    def __init__(self, name, health, max_health, attack_power, defense, level=1, attack_penalty=0):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense = defense
        self.level = level

        # gonna use this for attacking method
        self.attack_penalty = 0


    def can_attack(self, target):
        if not self.is_alive():
            print(f"{self.name} is dead and cannot attack!")
            return False

        if not target.is_alive():
            print(f"{target.name} is already dead!")
            return False

        return True

    # this is a lot more effective when calculating the damage for the round. so much better
    def attack(self, target):

        if not self.can_attack(target):
            return
        
        effective_attack = max(0, self.attack_power - self.attack_penalty)
        
        damage = max(0, effective_attack - target.defense)

        target.health = max(0, target.health - damage)

        print(f"{self.name} just attacked {target.name} for {damage} damage!")




        self.attack_penalty = 0

    def heal(self, amount):

        if not self.is_alive():
            print(f"{self.name} is dead and cannot heal themselves!")
            return

        if self.health + amount > self.max_health:
            self.health = self.max_health
            print(f"{self.name} has been healed back to full health: {self.max_health} / {self.max_health} HP.")

        else:
            self.health += amount
            print(f"{self.name} has been healed: {self.health} / {self.max_health} HP.")

    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} is alive with {self.health} / {self.max_health} HP.")
            return True
        else:
            print(f"{self.name} is DEAD!")
            return False

        
    def display_stats(self):
        print(f"The following stats are for {self.name}")
        print("\n")
        print(f"Health: {self.health}")
        print(f"Max Health: {self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Defense: {self.defense}")
        print(f"Current Level: {self.level}")




# Warrior Child Class
class Warrior(Character):
    def __init__(self, name, health, max_health, attack_power, defense, level=1, attack_penalty=0):
        super().__init__(name, health, max_health, attack_power, defense, level, attack_penalty)

    def shield_bash(self, target):

        if not self.can_attack(target):
            return

        effective_attack = max(0, self.attack_power - self.attack_penalty)        
        damage = max(0, effective_attack - target.defense)
        target.health = max(0, target.health - damage)
        target.attack_penalty = 5
        self.attack_penalty = 0

        print(f"{self.name} just did a shield bash on {target.name} and reduced their attack by {target.attack_penalty} for the next round.")





# Mage Child Class
class Mage(Character):
    def __init__(self, name, health, max_health, attack_power, defense, mana, max_mana, level=1, attack_penalty=0):
        super().__init__(name, health, max_health, attack_power, defense, level, attack_penalty)
        self.mana = mana
        self.max_mana = max_mana

    # Its the same as the other ones but the only difference is that i am adding mana inside of their stats as well
    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}")
        print(f"Max Mana: {self.max_mana}")


    def cast_spell(self, target):

        if not self.can_attack(target):
            return

        if self.mana > 10:

            effective_attack = max(0, self.attack_power - self.attack_penalty)
            damage = max(0, effective_attack - target.defense)

            target.health = max(0, target.health - damage)
            self.mana -= 10

            self.attack_penalty = 0

            print(f"{self.name} the mage casted a spell and attacked {target.name}")


            print(f"{self.name} Mana: {self.mana}")

        else:
            print(f"{self.name} the mage cannot perform this attack!")
            return



class Assassin(Character):

    def __init__(self, name, health, max_health, attack_power, defense, level=1, attack_penalty=0):
        super().__init__(name, health, max_health, attack_power, defense, level, attack_penalty)

    def critical_strike(self, target):

        if not self.can_attack(target):
            return

        effective_attack = max(0, self.attack_power - self.attack_penalty)

        damage = max(0, effective_attack - target.defense)

        if random.randint(1, 100) <= 30:
            print("CRITICAL HIT")
            damage *= 3
            target.health = max(0, target.health - damage)

        else:
            target.health = max(0, target.health - damage)

        self.attack_penalty = 0

        print(f"{self.name} the assassin, attacked {target.name} for {damage} damage.")

       

    




        


            



    



