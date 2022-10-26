f = open("English_words.txt").readlines()
# print(f)

# t = 0
# for i in f:
#     i = i.split()
#     if len(i) > 2:
#         print(i)
#         t+=1

#-----------------------------------------------
res = {}
for i in range(len(f)):
    k,v = f[i].split()   
    res[k] = v
print(res)