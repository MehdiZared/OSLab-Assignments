import random
Words = ['tree','book','linux','python','java','sadjad','rock','javascript','blue']

word = random.choice(Words)
UserTrue = []
Correct = 0
Joon = 5

while True  :
    for i in range (len(word)) :
        if word[i] in UserTrue :
            print(word[i],end=' ')
            Correct +=1
        else:   
             print('_',end=' ')

    user = input('please enter a charachter : ')

    if user in word :
        UserTrue.append(user)
        print("Correct")
    else:
        print ("wrong")
        Joon-=1

    if Joon ==0 :
        print("You Lost")
        break
    if Correct == len(word) : 
        print("You Win !")
        break