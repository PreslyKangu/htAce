#def fibonacci(init):
	#num = init (input ("Generating the sequence?:"))
	#i = 1
	#if num == 0:
	#	fibonacci = []
	#elif num == 1:
	#	fibonacci = [1]
	#elif num == 2:
	#	fibonacci = [1,1]
	#elif num > 2:
	#	fibonacci = [1,1]
	#while i <(num -1):
	#	fibonacci.append ( fibonacci[i] + fibonacci[i-1]),
	#	i+= 1
	#return fibonacci
#print (fibonacci())
#input()


# total = int(input("How many? "))
# numfib = [0, 1]
# for i in range(1, total):
##### numfib.append(numfib[i] + numfib[i-1])
# print(numfib[1:total+1])


#def Fibonacci(n):
#Flist = []
#for i in range(n):
#if i == 0 or i ==1 :
#Flist.append(1)
#continue
#Flist.append(Flist[-2] + Flist[-1])

#return Flist

#print(Fibonacci(int(input('How many Fibonnaci numbers to generate?\n'))))





# To get user input
def get_input(prompt):
return int(input(prompt))

# Returns the nth fibonacci number
def fibonacci_of(n):
if n == 0:
return 0
if n == 1:
return 1
return fibonacci_of(n-1) + fibonacci_of(n-2)

# Generates a list of fibonacci numbers sequence up to n
def fibonacci_seq_upto(n):
fib_list = []
for i in range(1, n+1):
fib_list.append(fibonacci_of(i))
return fib_list

n = get_input("How many fibonacci numbers would you like to generate: ")

print("Fibonacci sequence up to " + str(n) + " is \n" + str(fibonacci_seq_upto(n)))