class Diff1:
    depth = 0
    distance = 0
    aim = 0

    def up(self, units):
        self.aim -= units

    def down(self, units):
        self.aim += units

    def forward(self, units):
        self.distance += units
        self.depth += self.aim * units

    def __init__(self):
        with open("inputs/dec2_txt.txt") as data:
            for line in data.readlines():
                action, value = line.split(" ")
                value = int(value)
                if action == "up":
                    self.up(value)
                elif action == "down":
                    self.down(value)
                else:
                    self.forward(value)
        print(f"total depth: {self.depth}\ntotal distance: {self.distance}\n"
              f"aim = {self.aim}\nproduct = {self.depth * self.distance}")


Diff1()
