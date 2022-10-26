from random import choice, randint
import random
f,sanoq,data,insertData = open("English_words.txt").readlines(),1,[],[]
def sonRandom(a,b):
    return(random.randint(a,b))
for i in range(len(f)):
    array = f[i].split()
    data.append(array[0].capitalize())
for i in range(len(f)):
    insertArray = f[i].split()
    res,k = {},"numb"
    res[k] = i+1
    k = "question"
    res[k] = insertArray[1].capitalize()
    k = "answer"
    res[k] = insertArray[0].capitalize()
    k,v = 'options',[data[sonRandom(0,2297)],data[sonRandom(0,2297)],data[sonRandom(0,2297)]]
    v.insert(random.randint(0,3),insertArray[0].capitalize())
    res[k] = v
    print(res,",\n")