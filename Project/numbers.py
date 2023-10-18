ns = []
for _ in range(4):
    ns.append(int(input("Enter a number: ")))
n1 = ns[0] + ns[1]
n2 = ns[2] + ns[3]
n = n1/n2
print("%.2f" % n)