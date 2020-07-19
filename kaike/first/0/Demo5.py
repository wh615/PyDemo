import gifmaze as gm
from gifmaze.algorithms import random_dfs

surface = gm.GIFSurface(600, 400, bg_color=0)
surface.set_palette([ 0,0,0,255,255,255 ])
maze = gm.Maze(149, 99, mask=None).scale(4).translate((2, 2))

anim = gm.Animation(surface)
anim.pause(100)
anim.run(random_dfs,maze, speed=10, delay=5, trans_index=None, cmap={0: 0, 1: 1}, mcl=2, start=(0, 0))
anim.pause(300)
surface.save('d:\\random_dfs.gif')
surface.close()
