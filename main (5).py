#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket")
    #Define the deeived class Batsman
class Batsman (player):
  def play(self):
    print("The batsman is bating ")
    #define the derived class  bowler
class Bowler(player):
  def play(self):
    print("the bowler is bowling")        
batsman=Batsman()
bowler=Bowler()
Player=player()

Player.play()
batsman.play()
bowler.play()

  



