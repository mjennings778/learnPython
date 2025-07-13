class Enemy():
    def __init__(self, released, members, combat_level, size, 
                xp_bonus, max_hit, aggressive, poisonous, attack_style, attack_speed):
        self.released = released
        self.members = members
        self.combat_level = combat_level
        self.size = size
        self.xp_bonus = xp_bonus
        self.max_hit = max_hit
        self.aggressive = aggressive
        self.poisonous = poisonous
        self.attack_style = attack_style
        self.attack_speed = attack_speed

    def special(self):
        self.dmg = int(self.max_hit) * 0.3
        print(f"Damage is now {self.dmg} ")


Zulrah = Enemy(
    "8 January 2015",
    "Yes",
    "725",
    "5x5",
    "+0%",
    "41",
    "Yes",
    "Yes (venom)",
    "Ranged",
    "3 ticks"
)

print(vars(Zulrah))