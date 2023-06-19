# Coloca aqui o path pro arquivo
path = 'unweighted_events.lhe'
new = 'newunweighted_events.lhe'

# Aqui serve pra encontrar o inicio dos eventos no .lhe, caso seja relevante, e inicializar a lista com as linhas 
with open(path, 'r+') as f:
	linhas = f.readlines()
	inicio = linhas.index('<event>\n')	

# Aqui serve pra inserir os dados
teste = True
with open(new, 'w') as new:
	i = 0
	while True:
		if linhas[i] == '<event>\n':
			pzf1 = eval(linhas[i+2].split()[8])
			ef1 = eval(linhas[i+2].split()[9])
			pzf2 = eval(linhas[i+3].split()[8])
			ef2 = eval(linhas[i+3].split()[9])
			pzp1 = 6500 - pzf1
			pzp2 = -6500 - pzf2
			linhas.insert(i+6, f'       2212        1    0    0    0    0 0.0000E+00 0.0000E+00  {pzp1:.10e}  $en  0.938272046E+00 0.0000E+00 9.\n')
			linhas.insert(i+7, f'       2212        1    0    0    0    0 0.0000E+00 0.0000E+00  {pzp2:.10e}  $en  0.938272046E+00 0.0000E+00 9.\n')
		i += 1
		if i == len(linhas): break
	for line in linhas:
		new.write(line)
