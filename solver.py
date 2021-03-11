from copy import copy
import numpy as np

class Solver:
  def __init__(self, grid):
    self.grid = grid
    self.buildings = grid.buildings
    self.antennas = grid.antennas

  def gen_random_solution(self):
    def _valid_pos(grid, i, j):
      if not grid.cells[i][j][1]:
        return True
      else:
        False
    import numpy as np

    antennas = copy(self.antennas)
    grid =  copy(self.grid)
    while antennas:
      for i, ant_i in enumerate(antennas):
        ant = antennas[ant_i]
        i, j = np.random.randint(grid.w), np.random.randint(grid.h)
        if _valid_pos(grid, i, j):
          grid.cells[i][j][1] = ant._id
          del antennas[ant_i]
          print('Assigning ant {} to pos {}'.format(ant._id, (i, j)))
          break
    
    return grid


   
    
