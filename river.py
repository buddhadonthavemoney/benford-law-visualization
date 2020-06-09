from tabulate import tabulate

try:				#checks if the file exist if not throws an exception
	import graph
	import chitest
	benford=[ 30.1 , 17.6 , 12.5 , 9.7 , 7.8 , 6.7 , 5.8 , 5.1 , 4.6]
	title=['digit','benford (%)', 'river_data (%)']
	river_count=[0]*9
	data=['']*9
	def count(river_data):
		"""calculates the percentage of river associated with 1st digit of the river length"""
		for x in river_data:
			i=str(x)
			if i[0]=='1': river_count[0]=river_count[0]+1
			if i[0]=='2': river_count[1]=river_count[1]+1
			if i[0]=='3': river_count[2]=river_count[2]+1
			if i[0]=='4': river_count[3]=river_count[3]+1
			if i[0]=='5': river_count[4]=river_count[4]+1
			if i[0]=='6': river_count[5]=river_count[5]+1
			if i[0]=='7': river_count[6]=river_count[6]+1
			if i[0]=='8': river_count[7]=river_count[7]+1
			if i[0]=='9': river_count[8]=river_count[8]+1
		a=0
		for i in river_count:  #to calculate % and convert to string
			river_count[a]=float("{:.2f}".format((river_count[a]/len(river_data)*100)))
			data[a]=[a+1,benford[a],river_count[a]]
			a=a+1
		
		
	#mainblock 
	a=1
	b=0
	add=0
	river_data= [6690,6387,6380,6270,5550,5410,4667,4368,4371,4260,4241,4167,4023,\
	3998,3750,3645,3596,3379 ,3239,3184,3180,3180,3078,3060,3058,3057,\
	2989,2948,2850,2699,2693,2650,2627,2620,2615,2570,2549,2513,2510,2500,\
	2490,2450,2410,2428,2348,2300,2292,2287,2273,2250,2250,2333,2200,2188,2170,2153,2102,\
	2101,2100,2100,2092,2010,1978,1950,1927,1900,1870,1865,1809,1805,1800,1749,1726,1670,\
	1641,1610,1600,1600,1600,1600,1600,1599,1594,1591,1580,1575,1550,1532,1500,\
	1500,1490,1480,1465,1438,1438,1420,1420,415,1411,400,1400,1400,1376,1370,\
	1370,368,1364,1360,1352,1345,1323,1320,1320,1320,1300,1300,1289,1271,\
	1242,1240,1236,1231,1223,1220,1210,1200,1190,1175,1173,1162,1158,1143,\
	1143,1130,1130,1130,1130,1126,1123,1120,1115,1102,1100,1094,1086,1080,\
	1078,1050,1050,1050,1050,1049,1020,1015,1014,1012,1010,1010,1006,1000]    #river length

	no_terms=len(river_data)
	count(river_data)
	print(tabulate(data,headers=title,tablefmt="fancy_grid"))
	graph.plotfunc(8,benford,river_count,'river length')

except Exception:
	print('sorry the file doesn\'t exist')

