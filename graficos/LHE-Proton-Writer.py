import sys
'''
    Dependendo da origem do gerador de eventos eles tem espaçamento e precisão diferentes
'''
# Ele recebe o arquivo como argumento depois do python3
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    # Caso não receba o argumento usa esse como padrão
    path = 'unweighted_events.lhe'
new = 'new'+path

# Aqui serve pra encontrar o inicio dos eventos no .lhe, caso seja relevante, e inicializar a lista com as linhas 
with open(path, 'r+') as f:
    linhas = f.readlines()
    #print(linhas)
    inicio = linhas.index(' <event>\n')	

# Aqui serve pra inserir os dados
pzini = 7000		# pz inicial dos protons
eini = 7000		# energia inicial dos protons

# Massa de repouso do proton: 0.9382720882E+00


with open(new, 'w') as new:
    i = 0
    while True:
        if linhas[i] == ' <event>\n':
            j = 0
            while linhas[i+j] != ' </event>\n':
                if linhas[i+j].split()[0] == '22':
                    pzf = eval(linhas[i+j].split()[8])
                    sign = (pzf/abs(pzf))
                    pzp = pzini*sign - pzf
                    ef = eval(linhas[i+j].split()[9])
                    ep = eini - ef
                    if sign > 0: linhas.insert(i+j+1, ' '*13+f'2212{" "*8}1    0    0    0    0  {0:.9e}  {0:.9e}  {pzp:.9e}  {ep:.9e}  0.938272088E+00 0. 1.\n')
                    else: linhas.insert(i+j+1, ' '*13+f'2212{" "*8}1    0    0    0    0 -{0:.9e} -{0:.9e} {pzp:.9e}  {ep:.9e}  0.938272088E+00 0. -1.\n')
                j += 1
        i += 1
        if i == len(linhas): break
    for line in linhas:
        new.write(line)

