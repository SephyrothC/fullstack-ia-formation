a = open('text.txt')
for line in a:
    line = line.rstrip()
    print(line.upper())