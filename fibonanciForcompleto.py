ent = input()
p = list(ent)

'''for i in range(len(p)):
    for j in range(len(p)+1):
        substring =  p[i:j]
        if len(substring) == 0:
            pass
        else:
            print(substring)

for j in range(len(p)):
    print(p[j:j+1])#len-4
    if j == 3 or j ==4:
        pass
    else:
        print(p[j:j+2])#len-3
    if j == 2 or j == 3 or j == 4:
        pass
    else:
        print(p[j:j+3])#len-2
    if j == 3 or j == 4 or j ==2 or j == 1:
        pass
    else:
        print(p[j:j+4])#len-1
    if j == 4:
        pass
    else:
        print(p[j:])#len-0'''

def f(cont):
    print(p[cont:cont+1])
    if cont == 3 or cont == 4:
        pass
    else:
        print(p[cont:cont+2])
    if cont == 2 or cont == 3 or cont == 4:
        pass
    else:
        print(p[cont:cont+3])
    if cont == 3 or cont == 4 or cont ==2 or cont == 1:
        pass
    else:
        print(p[cont:cont+4])
    if cont == 4:
        pass
    else:
        print(p[cont:cont+5])
    if cont < 4:
        f(cont+1)
    
f(0)


    


            


        
