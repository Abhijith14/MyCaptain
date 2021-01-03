list = []

n = int(input("Enter the limit : "))

for i in range(n):
	list.append(int(input()))

for i in list:
	if i > 0:
	    print(str(i) + ", ")

