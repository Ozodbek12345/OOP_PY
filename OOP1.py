import random
class Warrior:
    Name = None
    Health = 100
    def set_name(self):
        print("Введите имя героя")
        self.Name = input()
    def start_the_battle(self):
        while Player_1.Health > 0 and Player_2.Health > 0:
            turn = random.randint(1, 2)
            if turn == 1:
                Player_2.Health -= 20
                print(Player_1.Name, "attacked")
                print(Player_2.Name, "health =", Player_2.Health)
            else:
                Player_1.Health -= 20
                print(Player_2.Name, "attacked")
                print(Player_1.Name, "health =", Player_1.Health)
        if Player_1.Health == 0:
            print(Player_2.Name, "win!")
        else:
            print(Player_1.Name, 'win!')
Player_1 = Warrior()
Player_2 = Warrior()
Player_1.set_name()
Player_2.set_name()
Player_1.start_the_battle()
