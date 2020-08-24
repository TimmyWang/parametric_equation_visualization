import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




class Visual:

	def __init__(self, fun_x, fun_y, fun_z=None):
		self.fun_x = fun_x
		self.fun_y = fun_y
		self.fun_z = fun_z

	def plot(self, range_p1, range_p2, range_p3=None, alpha=0.8,figsize=(12,7)):
		if range_p3 is not None:
			x,y,z = [],[],[]
			for p1 in range_p1:
				for p2 in range_p2:
					for p3 in range_p3:
						x.append(self.fun_x(p1,p2,p3))
						y.append(self.fun_y(p1,p2,p3))
						z.append(self.fun_z(p1,p2,p3))
			
			fig = plt.figure(figsize=figsize)
			ax = Axes3D(fig)			
			ax.scatter(x,y,z,alpha=alpha)

		else:
			x,y = [],[]
			for p1 in range_p1:
				for p2 in range_p2:
					x.append(self.fun_x(p1,p2))
					y.append(self.fun_y(p1,p2))
			plt.figure(figsize=figsize)
			plt.scatter(x,y,alpha=alpha)



