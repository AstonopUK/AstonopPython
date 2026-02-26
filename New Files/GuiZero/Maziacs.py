from guizero import *

app = App()

maps = []
gridSize = 8

for z in range(gridSize):
    maps.append([])

for x in range(gridSize):
    for y in range(gridSize):
        maps[x].append(Box(app))
        maps[x][y].bg="#ceba99"