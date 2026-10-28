
p
array = np.array([3,6,9.12])
division = array/3
print(division) #output [1. 2. 3. 4.]
print (type(division)) #output <class 'numpy.ndarray'>

list = [3, 6, 9, 12]
division = list/3 #error unsupported operand type(s) for /: 'list' and 'int'
