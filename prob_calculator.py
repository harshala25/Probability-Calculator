import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents =[]
    print(kwargs)
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    print(self.contents)

  def draw(self,num):
    all_removed = []
    if(num > len(self.contents)):
      return self.contents
    for i in range(num):
      removed=self.contents.pop(int(random.random() * len(self.contents)))
      all_removed.append(removed)
    return all_removed
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  cnt=0
  for i in range(num_experiments):
    exp_copy=copy.deepcopy(expected_balls)
    hat_copy=copy.deepcopy(hat)
    colors_gotten =hat_copy.draw(num_balls_drawn)

    for color in colors_gotten:
      if(color in exp_copy):
        exp_copy[color]-=1
    
    if(all(x <=0 for x in exp_copy.values())):
      cnt+=1
  
  return cnt/num_experiments
        

