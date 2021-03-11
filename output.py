def write_solution(grid, number_antennas):

  file = open("output.txt", "w") 
  file.write(str(number_antennas))
  file.write("\n")

  row_n = -1
  for row in grid.cells:
    row_n += 1
    column_n = 0
    for antenna in row:
      file.write(str(antenna) + str(' ') + str(column_n) + str(' ') + str(row_n))
      file.write("\n")
      column_n += 1


