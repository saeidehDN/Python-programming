n = int(input("n = "))
s = 0.0
for i in range(1, n+1):
    x = float(input("Number " + str(i) + " = "))
    s += x
m = s/n
print("average =", m)

