import sys
if(len(sys.argv)!=2):
    print("usage: python "+sys.argv[0]+" <integer greater than 0 and less than 10^52>")
    sys.exit()
num=int(sys.argv[1])
if(num<=0 or num>=(10**52)):
    print("usage: python "+sys.argv[0]+" <integer greater than 0 and less than 10^52>")
    sys.exit()
out=""


def il(number):
    if(number == 1):
        return "일"
    elif(number == 2):
        return "이"
    elif(number == 3):
        return "삼"
    elif(number == 4):
        return "사"
    elif(number == 5):
        return "오"
    elif(number == 6):
        return "육"
    elif(number == 7):
        return "칠"
    elif(number == 8):
        return "팔"
    elif(number == 9):
        return "구"
    else:
        return ""

def ship(number):
    if(number==10):
        return "십"
    return il(number//10)+"십"

def baek(number):
    if(number==100):
        return "백"
    return il(number//100)+"백"

def cheon(number):
    if(number==1000):
        return "천"
    return il(number//1000)+"천"

def man(number):
    print(number)
    if(number//(10**4)==1):
        return "만"
    return manStep(number//(10**4), True)+"만"

def eok(number):
    if(number == (10**8)):
        return "억"
    return manStep(number//(10**8), True)+"억"

def jo(number):
    if(number == (10**12)):
        return "조"
    return manStep(number//(10**12), True)+"조"

def gyeong(number):
    if(number == (10**16)):
        return "경"
    return manStep(number//(10**16), True)+"경"

def hae(number):
    if(number == (10**20)):
        return "해"
    return manStep(number//(10**20), True)+"해"

def ja(number):
    if(number == (10**24)):
        return "자"
    return manStep(number//(10**24), True)+"자"


def yang(number):
    if(number == (10**28)):
        return "양"
    return manStep(number//(10**28), True)+"양"


def gu(number):
    if(number == (10**32)):
        return "구"
    return manStep(number//(10**32), True)+"구"


def gan(number):
    if(number == (10**36)):
        return "간"
    return manStep(number//(10**36), True)+"간"


def jeong(number):
    if(number == (10**40)):
        return "정"
    return manStep(number//(10**40), True)+"정"


def jae(number):
    if(number == (10**44)):
        return "재"
    return manStep(number//(10**44), True)+"재"


def geuk(number):
    if(number == (10**48)):
        return "극"
    return manStep(number//(10**48), True)+"극"

def manStep(number, prefix):
    if(number==0):
        return ""
    cheonStep=number//1000
    baekStep=number%1000
    shipStep=baekStep%100
    ilStep=shipStep%10
    baekStep=baekStep//100
    shipStep=shipStep//10
    space=""
    if(ilStep==0 or (prefix and ilStep==1)):
        ilStep=""
    else:
        ilStep=il(ilStep)
        space=" "
    if(shipStep == 0):
        shipStep = ""
    elif(shipStep == 1):
        shipStep = "십"+space
    else:
        shipStep = il(shipStep)+"십"+space
        space = " "
    if(baekStep == 0):
        baekStep = ""
    elif(baekStep == 1):
        baekStep = "백"+space
    else:
        baekStep = il(baekStep)+"백"+space
        space = " "
    if(cheonStep == 0):
        cheonStep = ""
    elif(cheonStep == 1):
        cheonStep = "천"+space
    else:
        cheonStep = il(cheonStep)+"천"+space
    return cheonStep+baekStep+shipStep+ilStep



while(num>0):
    if(num < 10**4):
        out += manStep(num, False)
        num = 0
    elif(num < (10**8)):
        out += man(num)
        num = num % (10**4)
    elif(num < (10**12)):
        out += eok(num)
        num = num % (10**8)
    elif(num < (10**16)):
        out += jo(num)
        num = num % (10**12)
    elif(num < (10**20)):
        out += gyeong(num)
        num = num % (10**16)
    elif(num < (10**24)):
        out += hae(num)
        num = num % (10**20)
    elif(num < (10**28)):
        out += ja(num)
        num = num % (10**24)
    elif(num < (10**32)):
        out += yang(num)
        num = num % (10**28)
    elif(num < (10**36)):
        out += gu(num)
        num = num % (10**32)
    elif(num < (10**40)):
        out += gan(num)
        num = num % (10**36)
    elif(num < (10**44)):
        out += jeong(num)
        num = num % (10**40)
    elif(num < (10**48)):
        out += jae(num)
        num = num % (10**44)
    else:
        out += geuk(num)
        num = num % (10**48)
    if(num!=0):
        out+=" "

print(out)
