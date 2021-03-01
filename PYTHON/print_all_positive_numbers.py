list1 = []
list2 = []
n = int(input("Enter number of elements : "))

print("Enter list one by one ... ")
for i in range(n):
    list1.append(int(input()))

for i in list1:
    if i >= 0:
        list2.append(i)

print("Positive Elements : ")
for i in list2:
    print(i)
