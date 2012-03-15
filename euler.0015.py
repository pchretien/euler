#Answer: 137846528820

'''
@author: Philippe Chretien

Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 2020 grid?
'''

def addRow(routes):
	newRoutes = []
	for i in range(0,len(routes)):
		newRoutes.append(1)
		if i > 0:
			newRoutes[i] = sum(routes[0:i+1])
	
	newVal = 2*sum(routes)
	for i in range(0,len(routes)):
		routes[i] = newRoutes[i]
	
	routes.append(newVal)
		
routes = [1]
for i in range(0,20):
	addRow(routes)
	print routes