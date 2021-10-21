sentence = input("please enter a sentence : ")

count =1
for i in range(len(sentence)):
    if (sentence[i]==' '):
        count +=1
print ("there are ",count, ' words in your sentence!')
