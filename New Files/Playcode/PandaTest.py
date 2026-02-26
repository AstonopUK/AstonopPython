#TestPanda3DProject
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import random

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
       
       # Load a 3D model
        self.model = self.loader.loadModel("models/panda")
        self.model.reparentTo(self.render)
        self.model.setScale(0.5)
        self.model.setPos(10, 0, 0)
       
        # Load a cube model
        self.cube = self.loader.loadModel("models/box")
        self.cube.reparentTo(self.render)
        self.cube.setPos(Point3(0, 10, 0))
       
        # Add a directional light
        self.light = DirectionalLight("myLight")
        self.light_node = self.render.attachNewNode(self.light)
        self.light_node.setPos(0, 0, 10)
        self.render.setLight(self.light_node)

        # Rotate the cube over time
        self.taskMgr.add(self.spin_cube, "spinCubeTask")
   
    def spin_cube(self, task):
        angles = [task.time * random.randint(-10,10), task.time * random.randint(-10,10), task.time * random.randint(-10,10)]
        self.cube.setHpr(angles[0], angles[1], angles[2])
        return task.cont

app = MyApp()
app.run()