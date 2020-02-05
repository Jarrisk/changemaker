import numpy as np
import pdb

###FUNCTION###
def MakeChange(input,challenge):   
    if challenge=='picky':
        MakeChange.mcm[1]=0
        if MakeChange.mcm[5]==0 and MakeChange.mcm[10]==0 and MakeChange.mcm[25]==0:
            return print('I hate pennies')
        if input%5!=0 and input%10!=0:
            return print('I hate pennies') 
    MakeChange.leftovers=MakeChange.total_money-input
    if MakeChange.leftovers<0:
        return print('Insufficient Funds')
    if input>MakeChange.total_money:
        print('Cant make change!')
        Quarters=print('Quarters','N/A')
        Dimes=print('Dimes','N/A')
        Nickles=print('Nickles','N/A')
        Pennies=print('Pennies','N/A')
        return None   
    i=[25,10,5]
    inp=np.array([input,0,0,0])
    #Quarters/Nickles/Dimes
    for j in range(3):  
        if (MakeChange.mcm[i[j]]*i[j])==inp[j]:
            inp[j+1]=0 
        if (MakeChange.mcm[i[j]]*i[j])<inp[j]:
            inp[j+1]=inp[j]-(MakeChange.mcm[i[j]]*i[j])
        if (MakeChange.mcm[i[j]]*i[j])>inp[j]:       
            remain=inp[j]%i[j]
            inp_remain=inp[j]-remain
            MakeChange.mcm[i[j]]=inp_remain/i[j]
            if remain==0:
                remain=inp[j]/i[j]
                MakeChange.mcm[i[j]]=remain       
            inp[j+1]=inp[j]-(MakeChange.mcm[i[j]]*i[j])
        if inp[j]<i[j]:
            MakeChange.mcm[i[j]]=0
            inp[j]=inp[j]    
    #Pennies
    MakeChange.mcm[1]=inp[j+1]
    #Totals
    if challenge=='picky':
        Sumofcoins=(MakeChange.mcm[25]*25)+(MakeChange.mcm[5]*5)+(MakeChange.mcm[10]*10)
    else:
        Sumofcoins=(MakeChange.mcm[25]*25)+(MakeChange.mcm[5]*5)+(MakeChange.mcm[10]*10)+(MakeChange.mcm[1])
    if Sumofcoins!=input and challenge=='picky':
        print('I hate pennies')
    else:
        Quarters=print('Quarters',int(MakeChange.mcm[25]))
        Dimes=print('Dimes',int(MakeChange.mcm[10]))
        Nickles=print('Nickles',int(MakeChange.mcm[5]))
    if challenge=='picky':
        Pennies=print('-------')
        MakeChange.mcm[1]=0
    else:
        Pennies=print('Pennies',int(MakeChange.mcm[1]))
        Line=print('-------')
    MakeChange.total_money=MakeChange.total_money-(Sumofcoins)
    MakeChange.mncm=({ 1: MakeChange.mcm[1], 5: MakeChange.mcm[5], 10: MakeChange.mcm[10], 25:MakeChange.mcm[25] })
    MakeChange.mcm[1]=MakeChange.fcm[1]-MakeChange.mncm[1]
    MakeChange.mcm[5]=MakeChange.fcm[5]-MakeChange.mncm[5]
    MakeChange.mcm[10]=MakeChange.fcm[10]-MakeChange.mncm[10]
    MakeChange.mcm[25]=MakeChange.fcm[25]-MakeChange.mncm[25]
    return 
##################
MakeChange.mcm=({ 1: 20, 5: 3, 10: 4, 25:3 })
MakeChange.mncm=({ 1: 0, 5: 0, 10: 0, 25:0 })
MakeChange.fcm=({ 1: 20, 5: 3, 10: 4, 25:3 })
MakeChange.leftovers=0
MakeChange.total_money=(MakeChange.mcm[25]*25)+(MakeChange.mcm[5]*5)+(MakeChange.mcm[10]*10)+(MakeChange.mcm[1]) 
MakeChange.leftovers=MakeChange.total_money
print("Starting Total=", MakeChange.leftovers)
a=int(input('Type in Change: '))
b=int(input('Type in Some More Change: '))
c=int(input('Type in Some More Change: '))
inp=np.array([a,b,c])
picky='picky'
easy='easy'
for i in range(3):
    print('-------')
    string='change for {} cents:'.format(inp[i])
    print(string)
    MakeChange(inp[i],easy)  
    print("Leftovers=", MakeChange.leftovers)