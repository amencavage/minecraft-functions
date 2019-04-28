widths=[1,2,3]
heights=[5,10,15]
virts = ['up','down']

geomask_n=['n','North']
geomask_e=['e','East']
geomask_w=['w','West']
geomask_s=['s','South']
geomasks=[geomask_n,geomask_e,geomask_w,geomask_s]

def convert_coords(facing,coords_in):
	print 'input: ' + facing + ' ' + coords_in + '\n'
	f,v,l=coords_in.split('-')
	if len(v) == 2 and v.endswith('0'):
		y='~'
	else:
		if v.startswith('D'):
			y='~-' + v[1:]
		else:
			y='~' + v[1:]	
	if facing=='w':
		# WEST FACING (Pos Z, Neg X, Neg Z)
		if len(f) == 2 and f.endswith('0'):
			x='~'
		elif f.startswith('F'):
			x='~-' + f[1:]
		else:
			x='~' + f[1:]
		if len(l) == 2 and l.endswith('0'):
			z='~'
		elif l.startswith('R'):
			z='~-' + l[1:]
		else:
			z='~' + l[1:]
	elif facing=='e':
		# EAST FACING (Neg Z, Pos X, Pos Z)
		if len(f) == 2 and f.endswith('0'):
			x='~'
		elif f.startswith('B'):
			x='~-' + f[1:]
		else:
			x='~' + f[1:]
		if len(l) == 2 and l.endswith('0'):
			z='~'
		elif l.startswith('L'):
			z='~-' + l[1:]
		else:
			z='~' + l[1:]
	elif facing=='s':
		# SOUTH FACING (Pos X, Pos Z, Neg X)
		if len(f) == 2 and f.endswith('0'):
			z='~'
		elif f.startswith('B'):
			z='~-' + f[1:]
		else:
			z='~' + f[1:]
		if len(l) == 2 and l.endswith('0'):
			x='~'
		elif l.startswith('R'):
			x='~-' + l[1:]
		else:
			x='~' + l[1:]
	elif facing=='n':
		# NORTH FACING (Neg X, Neg Z, Pos X)
		if len(f) == 2 and f.endswith('0'):
			z='~'
		elif f.startswith('F'):
			z='~-' + f[1:]
		else:
			z='~' + f[1:]
		if len(l) == 2 and l.endswith('0'):
			x='~'
		elif l.startswith('L'):
			x='~-' + l[1:]
		else:
			x='~' + l[1:]
	coords = [x, y, z]
	return coords

def create_cmd_line(cmd,location1,location2,suffix,facing,virt):
	if cmd == 'fill':
		if virt == 'up':
			x1,y1,z1=convert_coords(facing,location1)
			x2,y2,z2=convert_coords(facing,location2)
		elif virt == 'down':
			x1,y1,z1=convert_coords(facing,location1.replace('D','U'))
			x2,y2,z2=convert_coords(facing,location2.replace('U','D'))
		startloc = x1 + ' ' + y1 + ' ' + z1
		endloc = x2 + ' ' + y2 + ' ' + z2
		cmdoutput = cmd + ' ' + startloc + ' ' + endloc + ' ' + suffix + '\n'
	elif cmd == 'setblock':
		if virt == 'up':
			x1,y1,z1=convert_coords(facing,location1)
		elif virt == 'down':
			x1,y1,z1=convert_coords(facing,location1.replace('D','U'))
		startloc = x1 + ' ' + y1 + ' ' + z1
		cmdoutput = cmd + ' ' + startloc + ' ' + suffix + '\n'
	return cmdoutput
	
def stairface(facing):
	if facing == 'n':
		sfoutput = '3'
	elif facing == 'e':
		sfoutput = '8'
	elif facing == 'w':
		sfoutput = '1'
	elif facing == 's':
		sfoutput = '2'
	return sfoutput

for virt in virts:
	for width in widths:
		for height in heights:
			for geomask in geomasks:
				filename = virt + '_' + str(width) + 'W_' + str(height) + 'H_' + geomask[0] + '.mcfunction'
				print filename
				file = open(filename,'w')
				print 'Create Obsidian Shell'
				cmd = 'fill'
				loc1 = 'F1-D2-L2'
				targloc2 = ['F' + str(height),'U' + str(height+4),'R' + str(width+1)]
				loc2 = '-'.join([str(x) for x in targloc2])
				suffix = 'minecraft:obsidian'
				file.write(create_cmd_line(cmd,loc1,loc2,suffix,geomask[0],virt))
				
				print 'Create Andesite Interior'
				cmd = 'fill'
				loc1 = 'F1-D1-L1'
				targloc2 = ['F' + str(height),'U' + str(height+3),'R' + str(width)]
				loc2 = '-'.join([str(x) for x in targloc2])
				suffix = 'minecraft:stone 6'
				file.write(create_cmd_line(cmd,loc1,loc2,suffix,geomask[0],virt))
				
				print 'Create stairs in the interior'
				for h in range(height):
					f = 'F' + str(h+1)
					v = 'U' + str(h)
					for w in range(width):
						h1 = 'R' + str(w)
						targloc = [f,v,h1]
						cmd = 'setblock'
						location = '-'.join([str(x) for x in targloc])
						suffix = 'minecraft:stone_brick_stairs ' + stairface(geomask[0])
						print 'create_cmd_line(' + cmd + ',' + location + ',' + location + ',' + suffix + ',' + geomask[0] + ',' + virt + ')'
						file.write(create_cmd_line(cmd,location,location,suffix,geomask[0],virt))
					# place glowstone every other level
					if h % 2 == 0:
						h1 = 'L1'
						v = 'U' + str(h+1)
						targloc = [f,v,h1]
						cmd = 'setblock'
						location = '-'.join([str(x) for x in targloc])
						suffix = 'minecraft:glowstone'
						print 'create_cmd_line(' + cmd + ',' + location + ',' + location + ',' + suffix + ',' + geomask[0] + ',' + virt + ')'
						file.write(create_cmd_line(cmd,location,location,suffix,geomask[0],virt))
						h1 = 'R' + str(width)
						targloc = [f,v,h1]
						cmd = 'setblock'
						location = '-'.join([str(x) for x in targloc])
						suffix = 'minecraft:glowstone'
						print 'create_cmd_line(' + cmd + ',' + location + ',' + location + ',' + suffix + ',' + geomask[0] + ',' + virt + ')'
						file.write(create_cmd_line(cmd,location,location,suffix,geomask[0],virt))
						
				
				print 'Create airspace in the interior'
				for h in range(height):
					cmd = 'fill'
					
					f = 'F' + str(h+1)
					v = 'U' + str(h+1)
					v2 = 'U' + str(h+4)
					h = 'R0'
					h2 = 'R' + str(w)
					
					targloc1 = [f,v,h]	
					targloc2 = [f,v2,h2]
					
					loc1 = '-'.join([str(x) for x in targloc1])
					loc2 = '-'.join([str(x) for x in targloc2])
					suffix = 'minecraft:air'
					file.write(create_cmd_line(cmd,loc1,loc2,suffix,geomask[0],virt))
					
				file.close()