# Conway-Game-Python
The mathematician Conway imagined a game, called game of life, which considered cells that are susceptible to reproduce, disappear, or survive when they obey certain rules. 
These cells are represented by elements on a grid of squares, where a grid has an arbitrary
size. Thus, each cell (except those on the boundaries of the grid) is surrounded by eight squares
that contain other cells. The rules are stated as follows:

## 1. Survival: Each cell that has two or three adjacent cells survives until the next generation.
## 2. Death: Each cell that has at least four adjacent cells disappears (or dies) by 
overpopulation. Also, each cell that has at most one adjacent cell dies by isolation.
## 3. Birth: Each empty square (i.e., dead cell) that is adjacent to exactly three cells gives birth
to a new cell for the next generation.

It is worth noting that all births and deaths occur at the same time during a generation.
