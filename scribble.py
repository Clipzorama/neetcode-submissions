class Character:

    def __init__(self, name, health, max_health, attack_power, defense, level=1):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense = defense
        self.level = level

        # gonna use this for attacking method
        self.attack_penalty = 0


    # this is a lot more effective when calculating the damage for the round. so much better
    def attack(self, target):
        effective_attack = max(0, self.attack_power - self.attack_penalty)
        
        damage = max(0, effective_attack - target.defense)

        target.health = max(0, target.health - damage)

        print(f"{self.name} just attacked {target.name} for {damage} damage!")

        self.attack_penalty = 0

    def heal(self, amount):
        if self.health + amount > self.max_health:
            self.health = self.max_health
            print(f"{self.name} has been healed back to full health: {self.max_health} / {self.max_health} HP.")

        else:
            self.health += amount
            print(f"{self.name} has been healed: {self.health} / {self.max_health} HP.")

    def is_alive(self):
        return True if self.health > 0 else False

    def display_stats(self):
        print(f"The following stats are for {self.name}")
        print("\n")
        print(f"Health: {self.health}")
        print(f"Max Health: {self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Defense: {self.defense}")
        print(f"Current Level: {self.level}")




class Warrior(Character):
    def __init__(self, name, health, max_health, attack_power, defense, level=1):
        super().__init__(name, health, max_health, attack_power, defense, level)

    def shield_bash(self, target):

        effective_attack = max(0, self.attack_power - self.attack_penalty)        
        damage = max(0, effective_attack - target.defense)
        target.health = max(0, target.health - damage)
        target.attack_penalty = 5
        print(f"{self.name} just did a shield bash on {target.name} and reduced their attack by {target.attack_penalty} for the next round")


class Mage(Character):
    def __init__(self, name, health, max_health, attack_power, defense, mana, max_mana level=1):
        super().__init__(name, health, max_health, attack_power, defense, level=1)
        self.mana = mana
        self.max_mana = max_mana

    # Its the same as the other ones but the only difference is that i am adding mana inside of their stats as well
    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}")
        print(f"Max Mana: {self.max_mana}")


    def cast_spell(self, target):

        self.mana += 10

        target.mana = max(0, target.mana - 10)

        if self.mana > self.max_mana:
            self.mana = self.max_mana

        print(f"{self.name} just casted a spell on {target.name} taking away 10 mana.")
        print("\n")
        print(f"{self.name} Total Mana: {self.mana}")
        print(f"{target.name} Total Mana: {target.mana}")

            



            



    



