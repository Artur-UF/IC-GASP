# Coloca aqui o path pro arquivo
path = 'unweighted_events.lhe'

# Aqui serve pra encontrar o inicio dos eventos no .lhe, caso seja relevante, e inicializar a lista com as linhas 
with open(path, 'r+') as f:
	linhas = f.readlines()
	inicio = linhas.index('<event>\n')	

# Aqui serve pra inserir os dados
with open(path, 'w') as new:
	i = 0
	while True:
		if linhas[i] == '<event>\n':
			linhas.insert(i+6, 'Aqui vai os dados dos protons-------------------<<<<<<<<<<<\n')
		i += 1
		if i == len(linhas): break
	for line in linhas:
		new.write(line)
