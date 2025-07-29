# x = "banana" # -> ['b', 'a', 'n', 'a', 'n', 'a']
# for y in range(9,15):
#    print(y)

# for i in range(16) :
#     print(i)

# a=0
# while (a <= 15) :
#     print(a)
#     a =a+1

# z =0 
# b = False
# while(b == False):

#     print(z)
#     z=z+1
#     if z > 15:
#         b = True

# x = [41, 9, 12, 3, 74, 15]
# smallest = x[0]
# print("Before:", smallest)
# for itervar in x:
#     if itervar < smallest:
#         smallest = itervar
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# word = "bananana"
# i = word.find("na") # Regarde l'index du premier "na" trouvé
# i = word.count("na") # Compte le nombre de "na"
# print(i)


words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]
print(n)