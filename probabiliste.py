from random import randint,uniform


nb_tours=5
n1,n2=5,5 #Taille matrice
pop = 1000 #population par case 
p = 0.1 #P(I->R)

deb_inf=[(n1//2,n2//2,pop//2)] #coordonnées premiers infectés


proba_guerison=0.1
proba_infection=0.50
proba_deplacement=0.5



M = [[[pop,0,0] for i in range(n2)] for i in range(n1)]

for i in deb_inf:
    M[i[0]][i[1]]=[pop-i[2],i[2],0]

print(M)

def position(x,y,n1,n2):
    L=[(0,1),(1,0),(-1,0),(0,-1)]    
    if x==0:
        L.remove((-1,0))
    if y==0:
        L.remove((0,-1))
    if x==n1-1:
        L.remove((1,0))
    if y==n2-1:
        L.remove((0,1)) 
    k=randint(0,len(L)-1)
    dx,dy=L[k]
    return(x+dx,y+dy)
    

    
def deplacement(M,proba_deplacement):
    n=len(M)
    N=M[:]
    for i in range (n):
        for j in range (n):
            for k in range (3):
                for l in range (N[i][j][k]):
                    p=uniform(0,1)
                    if p<proba_deplacement:
                        x,y=position(i,j,n,n)
                        M[i][j][k]-= 1
                        M[x][y][k]+= 1

def infection(M,proba_infection):
    for i in range (len(M)):
        for j in range (len(M[0])):
            if M[i][j][1]+M[i][j][0]+M[i][j][2]!=0:
                coef=M[i][j][1]/(M[i][j][1]+M[i][j][0]+M[i][j][2])
                for l in range (M[i][j][0]):
                    k=uniform(0,1)
                    if k<coef*proba_infection:
                        M[i][j][0]-=1
                        M[i][j][1]+=1

def coef(M,x,y):
    s=M[x][y][1]
    c=1
    l=[1,-1]
    for i in l:
        if x+i in range(n1):
            s+=M[x+i][y][1]
            c+=1
    for i in l:
        if y+i in range(n2):
            s+=M[x][y+i][1]
            c+=1
    return s/(c*pop)
    
print(coef(M,n2//2,n1//2-1))

def infection_bis(M,proba_infection):
    for i in range (len(M)):
        for j in range (len(M[0])):
            for l in range (M[i][j][0]):
                k=uniform(0,1)
                c=coef(M,i,j)
                if k<c*proba_infection:
                    M[i][j][0]-=1
                    M[i][j][1]+=1


def guerison(M,proba_guerison):
    for i in range (len(M)):
        for j in range (len(M[0])):
            for l in range (M[i][j][1]):
                k=uniform(0,1)
                if k<proba_guerison:
                    M[i][j][1]-=1
                    M[i][j][2]+=1



def main(M):
    N=M[:]
    for i in range(nb_tours):
        infection(M,proba_infection)
        guerison(M,proba_guerison)
        deplacement(M,proba_deplacement)
        print(nb(M))

def main_bis(M):            
    N=M[:]
    for i in range(nb_tours):
        infection_bis(N,proba_infection)
        guerison(N,proba_guerison)
        print("Itération:",i,nb(N))
    
def nb(M):
    S,I,R=0,0,0
    for i in range (len(M)):
        for j in range (len(M)):            
            S,I,R= S+M[i][j][0],I+M[i][j][1],R+M[i][j][2]
    return(S,I,R)

main_bis(M)

print(M)

