filePath = 'S:\\Learn_WIth_OStad\\Python_Project\\Nagad\\Data\\data.txt'
def addMoney(inp):
    f = open(filePath, 'w')
    val = (input('Enter Money: '))
    pin = int(input("Enter pin: "))
    if pin == inp:
        f.write(val)
        print("Added money successfully...")
    else:
        print("Invalid pin number..")
    
    f.close()


def cashOut(inp):
    f = open(filePath,'r')
    mon = f.read()
    f.close()
    if mon:
        prev = int(mon)
    else:
        prev = 0
    print("Current balance:",prev)
    pre = int(input("Enter amount: "))
    pin = int(input("Enter pin: "))
    if inp == pin:
        if prev>pre:
            f = open(filePath,'w')  
            f.write(str(prev-pre))
            print("Cash out successful.. New banlance:",prev-pre)
        else:
            print("Insufficient balance..")
    else:
        print("Invalid Pin...")


def sendMoney(inp):
    f = open(filePath,'r')
    mon = f.read()
    if mon:
        prev = int(mon)
    else:
        prev = 0
    num = input("Enter reciever account number: ")
    am = int(input("Enter amount: "))
    pin = int(input("Enter PIN "))
    if prev == 0:
        print("account balance is NULL.")
    
    elif prev>am:
        if inp == pin:
            f = open(filePath,'w')
            f.write(str(prev-am))
            f.close()
            print("Send successful..New balance:",prev-am)
        else:
            print("Invalid Pin..")
    else:
        print("Insufficient Balance..")


    

def MobileRecharge(inp):
    f = open(filePath,'r')
    mon = f.read()
    if mon:
        prev = int(mon)
    else:
        prev = 0
    num = input("Enter mobile number: ")
    am = int(input("Enter recharge amount: "))
    pin = int(input("Enter PIN "))
    if prev == 0:
        print("account balance is NULL.")
    elif prev>am:
        if inp == pin:
            f = open(filePath,'w')
            f.write(str(prev-am))
            f.close()
            print("Recharge successful..New balance:",prev-am)
        else:
            print("Invalid Pin..")
    else:
        print("Insufficient Balance..")

def payment(inp):
    f = open(filePath,'r')
    mon = f.read()
    if mon:
        prev = int(mon)
    else:
        prev = 0
    num = input("Enter billing number: ")
    am = int(input("Enter amount: "))
    pin = int(input("Enter PIN "))
    if prev == 0:
        print("account balance is NULL.")
    elif prev>am:
        if inp == pin:
            f = open(filePath,'w')
            f.write(str(prev-am))
            f.close()
            print("Bill Payment successful..New balance:",prev-am)
        else:
            print("Invalid Pin..")
    else:
        print("Insufficient Balance..")

def conPin():
    return int(input("Confirm PIN "))
def myNagad(inp):
    f = open(filePath,'r')
    mon = f.read()
    if mon:
        prev = int(mon)
    else:
        prev = 0
    print("1. my balance")
    print("2. Reset pin")
    print("3. AC details")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Total Balance:",prev)
    elif choice == 2:
        pin1 = int(input("Enter new PIN "))
        pin2 = conPin()
        if pin1 == pin2:
            global_inp = pin1
            print("Pin reset Successful..")
        else:
            print("Enter same pin.")
            while True:
                pin2 = conPin()
                if pin1 == pin2:
                    global_inp = pin1
                    print("Pin reset Successful..")
                    break
                else:
                    print("Enter same pin.")

            
    elif choice == 3:
        print("Current Balance: ",prev)
        print("Pin Code:",inp)

loop = True
print("*******************")
print("___****NAGAD****___")
print()
global_inp = int(input("Enter Four digit PIN number : "))
while loop:
    print("*******************")
    print("___****NAGAD****___")
    print("0. Add money")
    print("1. Cash out")
    print("2. Send Money")
    print("3. Mobile Recharge")
    print("4. Payment")
    print("5. My nagad")
    print("6. exit")
    choice = input("Choice Number : ")
    if choice == '0':
        addMoney(global_inp)
    if choice == '1':
        cashOut(global_inp)
    elif choice == '2':
        sendMoney(global_inp)
    elif choice == '3':
        MobileRecharge(global_inp)
    elif choice == '4':
        payment(global_inp)
    elif choice == '5':
        myNagad(global_inp)
    elif choice == '6':
        exit()
    else:
        print("Insert valid number..")

# 1. Cash out
# 2. Send Money
# 3. Mobile Recharge
# 4. Payment
# 5. Bill pay
# 6. My nagad
# 7. PIN reset