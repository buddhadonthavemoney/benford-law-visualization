from tabulate import tabulate
try:
	import graph
	import chitest
	benford=[ 30.1 , 17.6 , 12.5 , 9.7 , 7.8 , 6.7 , 5.8 , 5.1 , 4.6]
	title=['digit','benford (%)', 'fib (%)']
	fibonacci=[0]*9
	data=['']*9
	def count(fib):
		"""function to count the percentage of numbers starting with different digits"""
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
			fibonacci[a]=float("{:.2f}".format((fibonacci[a]/len(fib)*100)))  #reduces the number of decimal point values
			data[a]=[a+1,benford[a],fibonacci[a]] #store in multidimensional dimensional array to display in table
			a=a+1
		
		
	#mainblock 
	a=1
	b=0
	add=0
	no_terms=2000
	fib=[0]*no_terms
	for i in range(no_terms):
		fib[i]=str(a)
		add=a+b
		b=a
		a=add
	count(fib)
	print(tabulate(data,headers=title,tablefmt="fancy_grid"))
	print('the value of chi test is ',chitest.chitest(fibonacci,benford))
	graph.plotfunc(8,benford,fibonacci,'fibonacci')
except Exception:
	print('file doesn\'t exist')

