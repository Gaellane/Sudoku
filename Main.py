import Sudoku
def isNum(nb)->bool:
    test='0123456789'
    for i in test:
        if i==nb:
            return True
    return False
def lecture(nom):
    with open(nom, 'r') as fichier:
        lines=fichier.readlines()
    nb=[]
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if isNum(lines[y][x]):
                temp=int(lines[y][x])
                nb.append({'nb':temp,'x':x,'y':y})
    return nb

nom=input("nom du fichier : ")
test=Sudoku.Sudoku(lecture(nom))
test.finish()