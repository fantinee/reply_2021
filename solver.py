from copy import copy
import numpy as np

class Solver:
  def __init__(self, grid):
    self.grid = grid
    self.buildings = grid.buildings
    self.antennas = grid.antennas

  def gen_random_solution(self):
    def _valid_pos(grid, i, j):
      if not grid.cells[j][i][1]:
        return True
      else:
        False
    import numpy as np

    antennas = copy(self.antennas)
    grid =  copy(self.grid)
    while antennas:
      for i, ant_i in enumerate(antennas):
        ant = antennas[ant_i]
        i, j = np.random.randint(0, grid.w), np.random.randint(0, grid.h)
        if _valid_pos(grid, i, j):
          grid.cells[j][i][1] = ant._id
          ant.pos = (i, j)
          del antennas[ant_i]
          print('Assigning ant {} to pos {}'.format(ant._id, (i, j)))
          break
    
    return grid

  def evaluate_solution(self, grid):
    def _get_cell_coverage(grid, ant):
      Range = ant.Range
      for x in range(ant.pos[0] - Range, ant.pos[0] + Range + 1):
        amp = Range - abs(ant.pos[0] - x)
        print(x, amp)
        if x >= 0 and x <= grid.w - 1:
          for y in range(ant.pos[1] - amp, ant.pos[1] + amp + 1):
            print(y)
            if y >= 0 and y <= grid.h - 1:
              yield (x, y)
    
    def _get_score(grid, ant, x ,y):
      score = 0
      building = None

      if grid.cells[y][x][0]:
        building = grid.buildings[grid.cells[y][x][0]]
        score += building.speed * ant.Speed
        dist = abs(x - ant.pos[0]) + abs(y - ant.pos[1])
        score -= building.latency * dist

      return score, building        

    antennas = copy(grid.antennas)
    coverage = {b._id: 0 for b in grid.buildings}
    
    for ant_id in antennas:
      ant = antennas[ant_id]
      print('\tParsing ant {} - pos {} - range {}'.format(ant_id, ant.pos, ant.Range))
      if ant.pos[0]:
        for covered_x, covered_y in _get_cell_coverage(grid, ant):
          print('\t\tEvaluation pos {}'.format((covered_x, covered_y)))
          score, building = _get_score(grid, ant, covered_x, covered_y)
          print('\t\t\tScore', score)
          if building:
            if score > coverage[building._id]:
              coverage[building._id] = score
    
    return sum(coverage.values())
        

   
    
