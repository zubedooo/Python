linelist=list()
while True:
    line=raw_input()
    if line=='quit':
        break
    else:
        linelist.append(line)
for i in range(len(linelist)-1,-1,-1):
    print(linelist[i])
