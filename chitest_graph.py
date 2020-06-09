import chitest
from tabulate import tabulate
import matplotlib.pyplot as plt
def fibonacci(no_terms): #same as from ass2.py
    benford=[ 30.1 , 17.6 , 12.5 , 9.7 , 7.8 , 6.7 , 5.8 , 5.1 , 4.6]
    fibonacci=[0]*9
    data=['']*9
    def count(fib):
        for i in fib:
            if i[0]=='1': fibonacci[0]=fibonacci[0]+1
            if i[0]=='2': fibonacci[1]=fibonacci[1]+1
            if i[0]=='3': fibonacci[2]=fibonacci[2]+1
            if i[0]=='4': fibonacci[3]=fibonacci[3]+1
            if i[0]=='5': fibonacci[4]=fibonacci[4]+1
            if i[0]=='6': fibonacci[5]=fibonacci[5]+1
            if i[0]=='7': fibonacci[6]=fibonacci[6]+1
            if i[0]=='8': fibonacci[7]=fibonacci[7]+1
            if i[0]=='9': fibonacci[8]=fibonacci[8]+1
        a=0
        for i in fibonacci:  #to calculate % and convert to string
            fibonacci[a]=float("{:.2f}".format((fibonacci[a]/len(fib)*100)))
            data[a]=[a+1,benford[a],fibonacci[a]]
            a=a+1
        
        
    #mainblock 
    a=1
    b=0
    add=0
    
    fib=[0]*no_terms
    for i in range(no_terms):
        fib[i]=str(a)
        add=a+b
        b=a
        a=add
    count(fib)
    return chitest.chitest(fibonacci,benford)
    

no_terms=int(input('enter number of terms'))
i=10
chitest1=[]
x_number=[]
fibonacci(10)
while i < no_terms:
    chitest1.append(fibonacci(i)) #add the values of chitest assosicated with different no. of terms
    i=i+10
    x_number.append(i)

# draws the plot
plt.xlabel('no of terms')
plt.ylabel('chitest value')
plt.title('chitest vs no of terms')
plt.plot(x_number,chitest1)
plt.show()