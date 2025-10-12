
a = open('text.txt')
for line in a:
    line = line.rstrip()
    #print(line.upper())
    word = line.split()
    #print(word)
    if line == '' or word[0] == 'on' :
        print('skip')
        continue
    else :
        print('coucou')