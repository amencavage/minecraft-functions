for length in [5,10,20,50,100,200]:
	for width in [2,3,4]:
		for height in [3]:
			# EAST FACING (Neg Z, Pos X, Pos Z)
			filename = 'hallway_E_' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L.mcfunction'
			file = open(filename,'w')
			file.write('fill ~1 ~-2 ~-2 ~' + str(length+1) + ' ~' + str(height+1) + ' ~' + str(width+1) + ' minecraft:obsidian 0 hollow\n')
			file.write('fill ~1 ~-1 ~-1 ~' + str(length) + ' ~' + str(height) + ' ~' + str(width) + ' minecraft:stone 6 hollow\n')
			# LEFT SIDE GLOWSTONE
			file.write('fill ~2 ~1 ~-1 ~' + str(length) + ' ~1 ~-1 minecraft:glowstone\n')
			# RIGHT SIDE GLOWSTONE
			file.write('fill ~2 ~1 ~' + str(width) + ' ~' + str(length-1) + ' ~1 ~' + str(width) + ' minecraft:glowstone\n')
			file.write('tellraw @p ["",{"text":"Hallway facing East ' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L created","color":"gold","bold":true}]\n')
			file.close()
			
			# WEST FACING (Pos Z, Neg X, Neg Z)
			filename = 'hallway_W_' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L.mcfunction'
			file = open(filename,'w')
			file.write('fill ~-1 ~-2 ~2 ~-' + str(length+1) + ' ~' + str(height+1) + ' ~-' + str(width+1) + ' minecraft:obsidian 0 hollow\n')
			file.write('fill ~-1 ~-1 ~1 ~-' + str(length) + ' ~' + str(height) + ' ~-' + str(width) + ' minecraft:stone 6 hollow\n')
			# LEFT SIDE GLOWSTONE
			file.write('fill ~-2 ~1 ~1 ~-' + str(length) + ' ~1 ~1 minecraft:glowstone\n')
			# RIGHT SIDE GLOWSTONE
			file.write('fill ~-2 ~1 ~-' + str(width) + ' ~-' + str(length-1) + ' ~1 ~-' + str(width) + ' minecraft:glowstone\n')
			file.write('tellraw @p ["",{"text":"Hallway facing West ' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L created","color":"gold","bold":true}]\n')
			file.close()
			
			# NORTH FACING (Neg X, Neg Z, Pos X)
			filename = 'hallway_N_' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L.mcfunction'
			file = open(filename,'w')
			file.write('fill ~-2 ~-2 ~-1 ~' + str(width+1) + ' ~' + str(height+1) + ' ~-' + str(length+1) + ' minecraft:obsidian 0 hollow\n')
			file.write('fill ~-1 ~-1 ~-1 ~' + str(width) + ' ~' + str(height) + ' ~-' + str(length) + ' minecraft:stone 6 hollow\n')
			# LEFT SIDE GLOWSTONE
			file.write('fill ~-1 ~1 ~-2 ~-1 ~1 ~-' + str(length-1) + ' minecraft:glowstone\n')
			# RIGHT SIDE GLOWSTONE
			file.write('fill ~' + str(width) + ' ~1 ~-2 ~' + str(width) + ' ~1 ~-' + str(length-1) + ' minecraft:glowstone\n')
			file.write('tellraw @p ["",{"text":"Hallway facing North ' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L created","color":"gold","bold":true}]\n')
			file.close()
			
			# SOUTH FACING (Pos X, Pos Z, Neg X)
			filename = 'hallway_S_' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L.mcfunction'
			file = open(filename,'w')
			file.write('fill ~2 ~-2 ~1 ~-' + str(width+1) + ' ~' + str(height+1) + ' ~' + str(length+1) + ' minecraft:obsidian 0 hollow\n')
			file.write('fill ~1 ~-1 ~1 ~-' + str(width) + ' ~' + str(height) + ' ~' + str(length) + ' minecraft:stone 6 hollow\n')
			# LEFT SIDE GLOWSTONE
			file.write('fill ~1 ~1 ~2 ~1 ~1 ~' + str(length-1) + ' minecraft:glowstone\n')
			# RIGHT SIDE GLOWSTONE
			file.write('fill ~-' + str(width) + ' ~1 ~2 ~-' + str(width) + ' ~1 ~' + str(length-1) + ' minecraft:glowstone\n')
			file.write('tellraw @p ["",{"text":"Hallway facing South ' + str(height) + 'Hx' + str(width) + 'Wx' + str(length) + 'L created","color":"gold","bold":true}]\n')
			file.close()