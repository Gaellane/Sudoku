class Sudoku:
    def __init__(self,nb):
        self.ligne=[]
        self.base=[]
        self.etape=[0,0]
        self.initLigne()
        for i in nb:
            tab=[i['x'],i['y']]
            self.base.append(tab)
            self.ligne[i['y']][i['x']]=i['nb']
    def initLigne(self):
        for i in range(9):
            liste=[0 for j in range(9)]
            self.ligne.append(liste)
        
    def verifLigne(self,numLigne:int)->bool:
        for i in range(8):
            for j in range(i+1,9):
                if(self.ligne[numLigne][i]!=0 and self.ligne[numLigne][i]==self.ligne[numLigne][j]):
                    return False
        return True
    def verifColonne(self,numCol:int)->bool:
        for i in range(8):
            for j in range(i+1,9):
                if(self.ligne[i][numCol]!=0 and self.ligne[i][numCol]==self.ligne[j][numCol]):
                    return False
        return True
    def verifSemCarre(self,numColCarre:int,numLiCarre:int)->bool:
        x,y=numColCarre*3,numLiCarre*3
        toVerif=[0,0,0]
        for i in range(x,x+3):
            for j in range(y,y+3):
                toVerif=self.ligne[i][j]
                for I in range(x,x+3):
                    for J in range(y,y+3):
                        if(self.ligne[i][j]!=0 and I!=i and J!=j and self.ligne[i][j]==self.ligne[I][J]):
                            return False
        return True
    def verif(self,numLigne:int,numcol:int)->bool :
        return (self.verifLigne(numLigne) and self.verifColonne(numcol) and self.verifSemCarre(numLigne//3,numcol//3)) 
    def verifInBase(self,liste) ->bool:
        for i in (self.base):
            if i==liste:
                return True
        return False
    def show(self)->None:
        for i in range(9):
            string=""
            for j in range(9):
                if self.ligne[i][j]==0:
                    string+='_ '
                else:
                    string+=str(self.ligne[i][j])+" "
            print(string)    
    def changeEtape(self,avance:bool)->None:
        if avance:
            self.etape[0]+=1
            if self.etape[0]==9:
                self.etape[1]+=1
                self.etape[0]=0
        else :
            self.etape[0]-=1
            if self.etape[0]<0:
                self.etape[1]-=1
                self.etape[0]=8
                if self.etape[1]<0:
                    self.etape[1]=0
                    self.etape[0]=0 
    def change(self,ligne:int,colomne:int):
        self.ligne[ligne][colomne]+=1
        self.ligne[ligne][colomne]%=10
    def nulifier(self,ligne:int,colomne:int):
        self.ligne[ligne][colomne]=0
    def NotFinished(self)->bool:
        for i in range(9):
            for j in range(9):
                if self.ligne[i][j]==0:
                    return True
        return False
    def seachEtape(self,etat:bool)->bool:
        while self.verifInBase(self.etape):
            self.changeEtape(etat)
    def finish(self):
        print("Etat de debut : ")
        self.show()
        etat=True
        while(self.NotFinished()):

            self.seachEtape(etat)
            self.change(self.etape[1],self.etape[0])
            
            if(self.etape[1]==9):
                break
            while not self.verif(self.etape[1],self.etape[0]) :
                self.change(self.etape[1],self.etape[0])
                # print("ajgfkahsfhkjashfjkhjksf")
                if self.ligne[self.etape[1]][self.etape[0]]==0:
                    etat=False
                    break
            if self.ligne[self.etape[1]][self.etape[0]]!=0:
                etat=True
            if not self.NotFinished():
                break
            if etat:
                self.changeEtape(etat)
            else :
                self.nulifier(self.etape[1],self.etape[0])
                self.changeEtape(etat)
        print("resultat : ")
        self.show()
