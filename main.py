import numpy as np

from solver import Solver

class Building:
  def __init__(self, id, x, y, latency, speed):
    self._id = id
    self.x = x
    self.y = y
    self.latency = latency
    self.speed = speed

class Antenna:
  def __init__(self, id, Range, Speed):
    self._id = id
    self.pos = (None, None)
    self.Range = Range
    self.Speed = Speed

class Grid:
  def __init__(self, data_file):
    self.input_file = read_input(data_file)
    self.w = int((self.input_file[0]).split()[0])
    self.h = int((self.input_file[0]).split()[1])
    self.cells = [[[None, None] for i in range(self.w)] for j in range(self.h)]
    self.n = int((self.input_file[1]).split()[0]) # number of buildings
    self.m = int((self.input_file[1]).split()[1])
    self.r = int((self.input_file[1]).split()[2])
    self.buildings = {}
    self.antennas = {}
    #self.buildings_hash = {}  # Position to object
    self._grid_populate()
    self._read_antennas()

  def _grid_populate(self):
    
    pass

  def _add_buildings(self):
    id_num = 0
    for i in range (self.n):
      b_line = [int(i) for i in self.input_file[i+2].split()]
      b = Building(id_num, *b_line)
      self.buildings[id_num] = b
      self.cells[b.x][b.y][0] = id_num
      id_num+=1

  def _read_antennas(self):
    id_num = 0
    for i in range (self.m):
      a = [int(i) for i in self.input_file[i+self.n+2].split()]
      self.antennas[id_num] = Antenna(id_num, *a)
      id_num+=1

def read_input(file):
    with open(file,"r") as f:
        return  (f.read().splitlines())

def main():
  print ("REPLY CHALLENGE")
  # generate grid 
  print('Loading data...')
  grid =  Grid("data_scenarios_a_example.in")
  print('Data loaded.')
  solver = Solver(grid)
  print('Generating solution...')
  grid = solver.gen_random_solution()
  print('Solution generated')
  print('Evaluating solution...')
  evaluation = solver.evaluate_solution(grid)
  print('Evaluation:', evaluation)
  print('END')

main()