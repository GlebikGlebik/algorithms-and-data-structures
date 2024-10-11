from time import *

with open ("input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))

with open ("input.txt", "r") as f:
    with open ("output.txt", "w") as g:
        n = int(f.readline())
        b = f.readline().split()
        a = [int(x) for x in b]
        for i in range( n - 1):
            m = i
            for j in range(i + 1, n):
                if a[m] > a[j]:
                    m = j
            if m != i:
                p = min(m,i) + 1
                v = max(m,i) + 1
                g.write("Swap elements at indices " + str(p) + " and " + str(v) + ".")
                g.write("\n")
            a[m], a[i] = a[i], a[m]
        g.write("No more swaps needed.")


#print(a)
'''
3 1 4 2 2 
1 3 4 2 2 

'''