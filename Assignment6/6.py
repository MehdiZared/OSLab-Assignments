MyWords = []

def LoadData():
    print('Loading ...')
    FileAdress = 'words_bank.txt'
    while True : 
        try :
            with open(FileAdress,'r') as f :
                BigText = f.read()
                lines=BigText.split('\n')
            for i in range(0 , len(lines)-1 , 2):
                MyDict = {'English' : lines[i],"Persian" : lines[i+1]}  
                MyWords.append(MyDict)
        except OSError :
            print('File Not Found')
            FileAdress = input('Enter the word bank address : ')
        else :
            print('Loaded!')
            break

LoadData()

def TranslateEngtoPer(InputText):
    OutputText  = ""
    for w in InputText :
        for Dict in MyWords : 
            if Dict['English'] == w :
                OutputText += Dict['Persian'] +  " "
                break     
        else : 
            OutputText += w + " "
    return(OutputText)

def TranslatePertoEng(InputText):
    OutputText  = ""
    for w in InputText :
        for Dict in MyWords : 
            if Dict['Persian'] == w :
                OutputText += Dict['English'] +  " "
                break     
        else : 
            OutputText += w + " "
    return(OutputText)
    
def Add() : 
    eng = input("Please enter the English word : ")
    per = input("Please enter the Persian Translation : ")
    MyWords.append({'English':eng ,'Persian' : per})
    with open ('words_bank.txt' , 'w' ) as f :
        for words in MyWords :
            f.write(words['English'])
            f.write('\n')
            f.write(words['Persian'])
            f.write('\n')

while True : 
    print('Welcome to the Main Menu : ')
    print('1 - Translate English to Persian ')
    print('2 - Translate Persian to English ')
    print('3 - Add Words ')
    print('4 - Exit ')
    print('please enter your choice : ')
    C =int(input())



    if C == 1 :
        UserText = input('please weite your text !  : ')
        UserSentence = UserText.split('.')
        for i in range(len(UserSentence)) : 
            UserWords = UserSentence[i].split(' ')
            print(TranslateEngtoPer(UserWords))
    if C == 2 : 
        UserText = input('please weite your text !  : ')
        UserSentence = UserText.split('.')
        for i in range(len(UserSentence)) : 
            UserWords = UserSentence[i].split(' ')
        print(TranslatePertoEng(UserWords))
    if C == 3 : 
        Add()
    if C == 4 :
        exit()
    if C <1 or C>4 :        
        print("Enter a number between 1-4 !")  
        input('Please hit Enter to continue ')
