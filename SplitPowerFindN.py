def SplitPowerFindN(p,maxn):
    for i in range(2, maxn):
        n = 0
        for j in range(0, len(str(i))):
            jp = int(str(i)[j]) ** p
            #print(i,j,str(i)[j],jp)
            n += jp

        #print(n)
        if i == n:
            print("FOUND", i)
            return True

for nn in range(2,100):
    print("nn=",nn)
    SplitPowerFindN(nn,100000)