# first method Using Recursions
def fibonnaci1 (k):
	if k == 1 or k == 2:
		return 1
	return fibonnaci1 (k-1) + fibonnaci1 (k-2)

for i  in range(1,10):
	print (fibonnaci1(i))

#second method.. Using Loops
def fibonnaci2(k):
	a,b = 1,1
	for i in range(k-1):
		a, b = b, a+b

	return a

for i  in range(1,10):
	print (fibonnaci2(i))

#third method... Using Generators
def fibonnaci3():
	a,b = 1,1
	while True:
		yield a
		a,b = b, a+b

k = 0
for i in fibonnaci3():
	if k >= 10:
		break
	print (i)
	k += 1
