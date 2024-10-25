""" Наследование """

class Game:
  def __init__(self, game_name, game_year, company, graphics):
    self.game_name = game_name
    self.game_year = game_year
    self.graphics = graphics
    self.company = company
    
  def info(self):
    print(f'Game - {self.game_name}, year - {self.game_year}, company - {self.company}, graphics - {self.graphics}, multiplayer - {self.multiplayer}')
    
game = Game('MobileLegends', "2017", "Tencent", "Ultra HD")

    
class Roblox(Game):
  def __init__(self, game_name, game_year, company, graphics, multiplayer):
    # super().__init__(game_name, game_year, company, graphics)
    Game.__init__(self, game_name, game_year, company, graphics)
    self.multiplayer = multiplayer
    
  # def info(self):
  #   print(f'Game - {self.game_name}, year - {self.game_year}, company - {self.company}, graphics - {self.graphics}, multiplayer - {self.multiplayer}')
  
roblox = Roblox('Roblox', '2002', 'Roblox studio', 'Full HD', 'Yes')
roblox.info()
game.info()
