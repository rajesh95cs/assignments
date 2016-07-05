
def nesteggfixed(salary,save,growthrate,years,fund):
    if(years==0):
       fund.append(salary*save*0.01)
       return fund
    else:
        fund=nesteggfixed(salary,save,growthrate,years-1,fund)
        fund.append(fund[-1]*(1+0.01*growthrate)+(salary*save*0.01))
        return fund

salary=10000
save=10
growthrate=15
years=5
fund=list()
temp=0.00
fund=nesteggfixed(salary,save,growthrate,years,fund)
print(fund)


"""def nesteggfixed(salary,save,growthrate,retirefund):
    fund=salary*save*0.01
    for i in range(0,len(growthrate)):
        fund=fund*(1+0.01*growthrate[i])+salary*save*0.01
        retirefund.append(fund)
    print(retirefund)

salary=10000
save=10
growthrate=[3,4,5,0,3]
retirefund=list()
nesteggfixed(salary,save,growthrate,retirefund)"""
