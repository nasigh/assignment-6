WORDS_BANK=[]
def Menu():
    print("\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA")
    print("1. Translation English To Persian\n")
    print("2. Translation Persian To English\n")
    print("3. Add New Word\n")
    print("4. Exit")
    print("\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA","\U0001F4DA")
def Load_Data() :
    with open("words_bank.txt" , 'r') as f: 
        Temp_Text = f.read()
        MyWords = Temp_Text.split('\n')
    for i in range(0, len(MyWords), 2) :
        WORDS_BANK.append({'english' : MyWords[i] , 'persian' : MyWords[i+1]})       
def SaveWord():
    EnglishWord = input("Enter English Word\n")
    PersianWord = input("Enter Persian Word\n")
    WORDS_BANK.append({'english' : EnglishWord , 'persian' : PersianWord})
    f = open('words_bank.txt', 'a')
    f.write('\n'+ EnglishWord +'\n'+ PersianWord)
    f.close()         
def English_To_Persian():
    EnglishWord = input('Enter Your Text (ENGLISH) : ')
    UserWord= EnglishWord.split(' ')
    OutPutT= ''
    for TempUser in UserWord:
        for TempWord in WORDS_BANK:
            if TempUser == TempWord['english']:
                OutPutT += TempWord['persian'] + ' '
                break
        else:
            OutPutT += UserWord + ' ' 
    print("\n\nTranslation Of Your Text Is : ", OutPutT,"\n\n")    
def Persian_To_English():
    PersianWord= input('Enter Your Text (PERSIAN) : ')
    UserWord= PersianWord.split(' ')
    OutPutT= ''
    for TempUser in UserWord:
        for TempWord in WORDS_BANK:
            if  TempUser == TempWord['persian']:
                OutPutT += TempWord['english'] + ' '
                break
        else:
            OutPutT += UserWord + ' '
    print("\n\nTranslation Of Your Text Is : ", OutPutT,"\n\n")    
Load_Data()        
while True:
    Menu()
    Choice= input('Enter A Number : ')
    if Choice == '1' :
        English_To_Persian()
    elif Choice == '2': 
        Persian_To_English()
    elif Choice == '3' :
        SaveWord()
    elif Choice == '4': 
        exit()
    else:
        print('Wrong')