class Phone:
    def phonecolor(self, color):
        self.color = color
    def phonecost(self, cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def makecall(self):
        print("Make call with phone")

    def playgame(self):
        print("Play game with phone")
    
p1 =Phone()
p1.phonecolor("The Phone is:" + "Blue")
p1.phonecost("The Phone cost is:" + str(10000))
print(p1.show_color())
print(p1.show_cost())
p1.makecall()
p1.playgame()
