class Character:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def take_damage(self,damage):
        self.health -= damage



class Player(Character):

    def __init__(self, name, health,level): 
        super().__init__(name,health)
        self.level = level

    def level_up(self,level_up):
        self.level += level_up

class Enemy(Character):

    def __init__(self, name, health,enemy_type):
        super().__init__(name, health)
        self.enemy_type =enemy_type

# Testing the classes

player = Player("John", 100, 1)
enemy = Enemy("Goblin", 50, "Melee")

player.take_damage(20)
print(f"{player.name} took 20 damage. Health: {player.health}")

enemy.take_damage(10)
print(f"{enemy.name} took 10 damage. Health: {enemy.health}")

player.level_up(1)
print(f"{player.name} leveled up! New level: {player.level}")

   