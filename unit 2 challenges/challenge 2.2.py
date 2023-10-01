class player:
  
  def play(self):
    print("player is playing cricket")

class batsman(player):
  def play(self):
    print("batsman is batting")

class bowler(player):
  def play(self):
    print("bowler is bowling")

bm=batsman()
bw=bowler()

bm.play()
bw.play()