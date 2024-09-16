with open("input.txt","w") as k:
    a,b = map(int, input().split())
    k.write(str(a) + " " + str(b))

with open("input.txt", "r") as f:
    string = f.read().split()
    line = [int(x) for x in string]
    res = line[0] + line[1]**2

with open("output.txt", "w") as g:
    g.write(str(res))
