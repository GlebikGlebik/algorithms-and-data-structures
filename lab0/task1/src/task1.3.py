with open("../textf/input.txt", "w") as k:
    a,b = map(int, input().split())
    k.write(str(a) + " " + str(b))

with open("../textf/input.txt", "r") as f:
    string = f.read().split()
    line = [int(x) for x in string]
    if -10 ** 9 <= line[0] <= 10 ** 9 and -10 ** 9 <= line[1] <= 10 ** 9:
        res = line[0] + line[1]
        t = True
    else:
        t = False

with open("../textf/output.txt", "w") as g:
    if t == True:
        g.write(str(res))
    elif t == False:
        g.write("Incorrect input, please change the data")
