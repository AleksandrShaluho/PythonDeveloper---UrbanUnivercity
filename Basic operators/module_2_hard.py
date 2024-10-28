#надоело вводить числа руками) Пусть за меня работает компьютер)
import random

# функция определения второго ключа
def GetSecondKey(FirstKey):
    SecondKey=''
    i=1
    while i!= FirstKey:
        for j in range(i+1,FirstKey):
            if FirstKey%(i+j)==0:
# можно было бы пары собирать в список, но по условиям задачи от нас ждут строку, распаковка списка этолишняя итерация
               SecondKey+=(str(i)+str(j))
        i+=1
    return SecondKey
#функция которая выводит значения конкретной пары ключей и проверяет верность второго ключа
def PutInKeys(FirstKey, SecondKey):
    print(f'FirstKey is: {FirstKey}. SecondKey is: {SecondKey}')
    print('Checking your keys...')
    if IsKeysValid(FirstKey,SecondKey):
        print("Welcome, stranger! I don't know how but you've done it..")
    else:
        print("Keys incorrorect! You'll DIE there...A-HA-HA-HA!!!!")
#функция проверки верности второго ключа. Все пары ключей переписаны из условия задачи в словарь
def IsKeysValid(FirstKey,SecondKey):
    KeysStorage = {3:'12',
                   4:'13',
                   5:'1423',
                   6:'121524',
                   7:'162534',
                   8:'13172635',
                   9:'1218273645',
                   10:'141923283746',
                   11:'11029384756',
                   12:'12131511124210394857',
                   13:'112211310495867',
                   14:'1611325212343114105968',
                   15:'1214114232133124115106978',
                   16:'1317115262143531341251161079',
                   17:'11621531441351261171089',
                   18:'12151811724272163631545414513612711810',
                   19:'118217316415514613712811910',
                   20:'13141911923282183731746416515614713812911'
                   }
    if  SecondKey== KeysStorage[FirstKey]:
        return True
    else:
        return False
#собственно программа, использующая заранее описанные функции
FirstKey = random.randint(3,20)
PutInKeys(FirstKey,GetSecondKey(FirstKey))
