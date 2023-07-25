import sys
# Ele recebe o arquivo como argumento depois do python3
if len(sys.argv) > 1:
	path = sys.argv[1]
else:
# Caso não receba o argumento usa esse como padrão
	path = 'unweighted_events.lhe'
new = 'newunweighted_events.lhe'

# Aqui serve pra encontrar o inicio dos eventos no .lhe, caso seja relevante, e inicializar a lista com as linhas 
with open(path, 'r+') as f:
	linhas = f.readlines()
	inicio = linhas.index('<event>\n')	

# Aqui serve pra inserir os dados
pzini = 6800		# pz inicial dos protons
eini = 6800		# energia inicial dos protons

with open(new, 'w') as new:
	i = 0
	while True:
		if linhas[i] == '<event>\n':
			j = 0
			while linhas[i+j] != '<mgrwt>\n':
				if linhas[i+j].split()[0] == '22':
					pzf = eval(linhas[i+j].split()[8])
					sign = (pzf/abs(pzf))
					pzp = pzini*sign - pzf
					ef = eval(linhas[i+j].split()[9])
					ep = eini - ef
					if sign > 0: linhas.insert(linhas.index('<mgrwt>\n', i), f'     2212  1    0    0    0    0 +{0:.10e} +{0:.10e} +{pzp:.10e} {ep:.10e} 0.9382720882E+00 {0:.4e} {1:.4e}\n')
					else: linhas.insert(linhas.index('<mgrwt>\n', i),f'     2212  1    0    0    0    0 -{0:.10e} -{0:.10e} {pzp:.10e} {ep:.10e} 0.9382720882E+00 {0:.4e} -{1:.4e}\n')
				j += 1
		i += 1
		if i == len(linhas): break
	for line in linhas:
		new.write(line)
		
