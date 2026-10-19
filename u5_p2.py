class Robot:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    def voice_line(self):
        print("Blipp Blopp!!")
        

class Battlebot(Robot):
    def __init__(self, name, energy, weapon):
        super().__init__(name, energy)
        self.weapon = weapon
    def voice_line(self):
        print("Boooom Slash!!!")
        
       
        


        
class Repairbot(Robot):
    def __init__(self, name, energy, repair_tool):
        super().__init__(name, energy)
        
        self.repair_tool = repair_tool
    def voice_line(self):
        print("Zapp Klang!!")


worrior = Battlebot(name = "Strid Robot", energy=10, weapon="katana")
healer = Repairbot(name="Lagnings Robot", energy=10, repair_tool="Mutterknack")
vanilla_bot = Robot(name="Skrott hög", energy=5)

# print(f"name: {worrior.name}\nplacement cost: {worrior.energy}\nheld weapon: {worrior.weapon}\n\n")
# print(f"name: {healer.name}\nplacement cost: {healer.energy}\nheld weapon: {healer.repair_tool}")
bots = {worrior, healer, vanilla_bot}
for bot in bots:
    bot.voice_line()