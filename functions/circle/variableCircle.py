from math import *
	
for radius in range(2,101):
	filename = 'hori_rad_' + str(radius) + '.mcfunction'
	file = open(filename,'w')
	for x in range(-radius,radius+1):
		for y in range(-radius,radius+1):
			if ceil(hypot(x,y)) == radius:
				file.write('clone ~ ~-1 ~ ~ ~-1 ~ ~' + str(x) + ' ~ ~' + str(y) + '\n')
	file.write('tellraw @p ["",{"text":"Horizontal circle of radius '+str(radius)+' made","color":"gold","bold":true}]\n')
	
	file.close()
	
for radius in range(2,101):
	filename = 'vert_rad_' + str(radius) + '.mcfunction'
	file = open(filename,'w')
	for x in range(-radius,radius+1):
		for y in range(-radius,radius+1):
			if ceil(hypot(x,y)) == radius:
				file.write('clone ~ ~-1 ~ ~ ~-1 ~ ~ ~' + str(x) + ' ~' + str(y) + '\n')
	file.write('tellraw @p ["",{"text":"Vertical circle of radius '+str(radius)+' made","color":"gold","bold":true}]\n')
	
	file.close()	
	
for radius in range(2,31):
	filename = 'sphere_rad_' + str(radius) + '.mcfunction'
	file = open(filename,'w')
	for x in range(-radius,radius):
		for y in range(-radius,radius):
			for z in range(-radius,radius):
				if ceil(hypot(x,y)) == radius and ceil(hypot(x,z)) == radius:
					file.write('clone ~ ~-1 ~ ~ ~-1 ~ ~' + str(x) + ' ~' + str(y) + ' ~' + str(z) + '\n')
	for y in range(-radius,radius):
		for x in range(-radius,radius):
			for z in range(-radius,radius):
				if ceil(hypot(x,y)) == radius and ceil(hypot(y,z)) == radius:
					file.write('clone ~ ~-1 ~ ~ ~-1 ~ ~' + str(x) + ' ~' + str(y) + ' ~' + str(z) + '\n')
	#for z in range(-radius,radius):
		#for x in range(-radius,radius):
			#for y in range(-radius,radius):
				#if ceil(hypot(x,z)) == radius and ceil(hypot(y,z)) == radius:
					#file.write('clone ~ ~-1 ~ ~ ~-1 ~ ~' + str(x) + ' ~' + str(y) + ' ~' + str(z) + '\n')
	file.write('tellraw @p ["",{"text":"Sphere of radius '+str(radius)+' made","color":"gold","bold":true}]\n')
	
	file.close()	