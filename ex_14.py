n = int(input('Dati numarul de coloane si randuri:\n'))
if 2 <= n <= 10:
    matrice = []
    for i in range(n):
        list = []
        for j in range(n):
            list.append(int(input(f'Dati element pe pozitia {i}:{j}: ')))
        matrice.append(list)
    for linie in matrice:
        print(linie)
    sus_prin = []
    jos_prin = []
    sus_sec = []
    jos_sec = []
    diag_sec = []
    diag_prin = [matrice[i][i] for i in range(len(matrice))]
    print(f'Suma elementelor din diagonala principala este {sum(diag_prin)}')
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i + j == len(matrice) - 1:
                diag_sec.append(matrice[i][j])
            if i < j:
                sus_prin.append(matrice[i][j])
                jos_prin.append(matrice[j][i])
            if i + j < len(matrice) - 1:
                sus_sec.append(matrice[i][j])
            if i + j > len(matrice) - 1:
                jos_sec.append(matrice[i][j])
    print(f'Suma elementelor din diagonala secundara este {sum(diag_sec)}')
    print(f'Suma elementelor din partea de sus a diagonalei principale este: {sum(sus_prin)}')
    print(f'Suma elementelor din partea de jos a diagonalei principale este: {sum(jos_prin)}')
    print(f'Suma elementelor din partea de sus a diagonalei secundare este: {sum(sus_sec)}')
    print(f'Suma elementelor din partea de jos a diagonalei secundare este: {sum(jos_sec)}')
else:
    print('Dati un numar ed linii si coloane intre 2 si 10')