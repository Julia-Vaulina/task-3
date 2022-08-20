import re

name1 = "1.txt"
name2 = "2.txt"

n1 = len(re.findall(r"\n+?", open("1.txt").read())) + 1
n2 = len(re.findall(r"\n+?", open("2.txt").read())) + 1
print(n1, n2)

if n1 > n2:
    open("3.txt", "w").write(name1 + '\n' + str(n1) + '\n' + open("1.txt", "r").read() + '\n' + name2 +
                             '\n' + str(n2) + '\n' + open("2.txt", "r").read())
else:
    open("3.txt", "w").write(name2 + '\n' + str(n2) + '\n' + open("2.txt", "r").read() + '\n' + name1 +
                             '\n' + str(n1) + '\n' + open("1.txt", "r").read())
