from matplotlib import pyplot as plt
import random
import os
from itertools import combinations
from mpl_toolkits.mplot3d import Axes3D

Ni=[]
Nu=[]
U=[]#all unions u
Ui=[]#all uniions ui

I=[]#all intersections u
Ii=[]#all intersectons ui

class Suplier():
    y_max = 1
    y_min = 0
  
    def triangular(x,a,b,c):
        return (round(max(min( (x-a)/(b-a), (c-x)/(c-b) ),0),3))
    
    def increase():
        
        A, B = [], []
        for i in range(8):
            x = random.randrange(5,50)

            a=random.randrange(0,5)
            b=random.randrange(5,45)
            c=random.randrange(45,51)
            A.append(((x, Suplier.triangular( x, a, b, c) )))
        for i in range(8):
            x = random.randint(5,50)

            a=random.randrange(0,5)
            b=random.randrange(5,45)
            c=random.randrange(45,51)
            B.append(( x, Suplier.triangular( x, a, b, c)))
        
            
        print('A fuzzy set: ', A)
        print("\n")
        
        print('B fuzzy set: ', B)
        print("\n") 
        return (A, B)#return s a tuple of two lists.
        
    
    def decrease():
        P, Q = [], []
        for i in range(8):
            x = random.randrange(5,50)
            a=random.randrange(0,5)
            b=random.randrange(5,45)
            c=random.randrange(45,51)
            P.append(  (x, round(1-Suplier.triangular( x, a, b, c),3) ))
        for i in range(8):
            x = random.randrange(5,50)
            a=random.randrange(0,5)
            b=random.randrange(5,45)
            c=random.randrange(45,51)
            Q.append(( x, round(1-Suplier.triangular( x, a, b, c),3)))
        
            
        print('P fuzzy set: ', P)
        print("\n")
        
        print('Q fuzzy set: ', Q)
        print("\n")
        return (P, Q)
     #genrating extension principle   
    def generate_type2(mat):
        ff=[]
        for i in mat:
            ff=ff+i
        el_map={}#stores x and u value.
        mu={}#(x,sup)
        for i in ff:
            if i[0] not in el_map:
                el_map[i[0]]=[]
                el_map[i[0]].append(i[1])
            if i[0] in el_map:#ingnore duplicate data in ff
                el_map[i[0]].append(i[1])#key is x and value is u
                        
        for key in el_map.keys():
            mu[key] = []
        
            for each in combinations([i for i in range(2)], 2):
                for i in  range(len(mat[each[0]])):
                    for j in range(len(mat[each[1]])):
                        if(key == (mat[each[0]][i][0]**2)+(mat[each[1]][j][0]**2)):
                            mu[key].append(min([mat[each[0]][i][1], mat[each[1]][j][1]]))
                
                                            

        ##superiour

        for i in mu.keys():
            if mu[i]==[]:#if no sup was produced above.
                mu[i]=max(el_map[i])
            else:
                mu[i] = max(mu[i])
            
        B = [(i, mu[i]) for i in mu.keys() ]#converting from dictionary to list.
        B.sort()
          
        print("Type 2:",B)
        print("\n")
        return B

        




class Operation():
    
    
    def intersection(l1,l2):
        
        lx=l1+l2
        f1 = [i[0] for i in lx]#storing x value.
        f1.sort()
        f1= list(set(f1))

        print("F1:",f1)
        print("\n")

        N =random.sample(f1 , 1)[0]#choosing a random value from the set f1

        print("The value of N is",N)
        
        ui=[]
        uui=[]
        vj=[]
        uvj=[]
        min_ui_vj=[]
        min_uui_uvj=[]
        
        for _ in range(N):
                ui.append(round(float(random.random()),2))
        print("The value of ui is:",ui)
        print("\n")
        for _ in range(N):
                uui.append(round(float(random.random()),2))
        print("The value of Uui:",uui)
        print("\n")
        
        for _ in range(N):
                vj.append(round(float(random.random()),2))
        print("The value of vj:",vj)
        print("\n")
        
        for _ in range(N):
                uvj.append(round(float(random.random()),2))
        print("The value of Uvj:",uvj)
        print("\n")
	
        for i in ui:
                for j in vj:
                        min_ui_vj.append(min(i,j))
                        
        for i in uui:
                for j in uvj:
                        min_uui_uvj.append(min(i,j)) 
        print("min_ui_vj",min_ui_vj)                       
        print("\n")
        
        print("min_uui_uvj",min_uui_uvj)
        print("\n")
        
        U_A_N=[]
        mx=-999
        muivj=list(set(min_ui_vj))
        print("muuivj:",muivj)
        
        for el in muivj:
            for i in range(len(min_ui_vj)):
                if el==min_ui_vj[i]:
                    mx=max(mx , min_uui_uvj[i])
            U_A_N.append((el,mx))
            mx=-999
        print("UA",N)
        print(U_A_N)
        for i in U_A_N:
            I.append(i[0])
            Ii.append(i[1])
            Ni.append(N)
        return f1
    
    def union(l1,l2):
        lx=l1+l2
        f1 = [i[0] for i in lx]
        f1.sort()
        f1= list(set(f1))

        print("f1",f1)
        print("\n")

        N =random.sample(f1,1)[0]
        print("The value of N is",N)
        print("\n")

        ui=[]
        uui=[]
        vj=[]
        uvj=[]
        max_ui_vj=[]
        min_uui_uvj=[]
        
        for _ in range(N):
                ui.append(round(float(random.random()),2))
        print("The value of ui from union is:",ui)
        print("\n")
        for _ in range(N):
                uui.append(round(float(random.random()),2))
        print("The value of Uui from union :",uui)
        print("\n")
        for _ in range(N):
                vj.append(round(float(random.random()),2))
        print("The value of vj from union :",vj)
        print("\n")
        for _ in range(N):
                uvj.append(round(float(random.random()),2))
        print("The value of Uvj from union :",uvj)
        print("\n")
        for i in ui:
                for j in vj:
                        max_ui_vj.append(max(i,j))
        
        print("\n")
        for i in uui:
                for j in uvj:
                        min_uui_uvj.append(min(i,j)) 
        print("max_ui_vj")                       
        print(max_ui_vj)   
        print("min_uui_uvj")
        print(min_uui_uvj)
        U_A_N=[]
        mx=-999
        muivj=list(set(max_ui_vj))
        print("muivj:",muivj)
        
        for el in muivj:
            for i in range(len(max_ui_vj)):
                if el==max_ui_vj[i]:
                    mx=max(mx , min_uui_uvj[i])
            U_A_N.append((el,mx))
            mx=-999
        print("UA",N)
        print(U_A_N)
        for i in U_A_N:
            U.append(i[0])
            Ui.append(i[1])
            Nu.append(N)
        print("\n")
        return f1


print("Genrating extension principle rule from increase")
print("\n")
ty2_1 = Suplier.increase()
type2v1 = Suplier.generate_type2(ty2_1)
print("Genrating extension principle rule from from decrease")
print("\n")
ty2_2 = Suplier.decrease()
type2v2 = Suplier.generate_type2(ty2_2)
input()
os.system('cls')

print("performing union opreation")
print("\n")
kk = Operation.union(type2v1 , type2v2)

print("\n\n")
print("performing intersection opreation")
print("\n")
kk = Operation.intersection(type2v1 , type2v2)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(Nu,U,Ui,marker='o')
ax.set_xlabel('N')
ax.set_ylabel('u')
ax.set_zlabel('ui')
plt.title('union')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Ni,I,Ii,marker='^')
ax.set_xlabel('N')
ax.set_ylabel('u')
ax.set_zlabel('ui')
plt.title('intersection')
plt.show()
