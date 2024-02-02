def billlist():
    user_data = {}
    bills = ["1.Adani Electricity","2.Tata Power","3.Torrent Power","4.Vaghani Energy"]
    for i in range(4):
        print(bills[i])



def welcome():
    print("Welcome to Google Pay\n\n\n")
def login():
    name = str(input("Enter your name: "))
    number = int(input("Enter your mobile number: "))
    mpin = int(input("Enter Mpin received on your mobile: "))
    user_data = {'name': name, 'number': number, 'mpin': mpin}
 
    
def electricity_bills():
    print("\nChoose an electricity provider:\n")
    billlist()
    bill_choice = int(input("\nEnter your choice: "))
    if bill_choice==1:
        print()
        accno=int(input("\nEnter 10-digit account number:"))
        pendamount=1000
        print("Pending Bill :",pendamount,"₹")
        atopay= float(input("Enter the amount you want to pay: "))
        if atopay <= pendamount:
            pendamount = pendamount-atopay
            print("\nBill Paid successfully! Remaining amount:",pendamount,"₹")
        else:
            print("Payment amount is more than the pending amount. Payment failed.")
    elif bill_choice==2:
        print()
        accno=int(input("\nEnter 10-digit account number:"))
        pendamount=5000
        print("Pending Bill :",pendamount,"₹")
        atopay= float(input("Enter the amount you want to pay: "))
        if atopay <= pendamount:
            pendamount = pendamount-atopay
            print("\nBill Paid successfully! Remaining amount:",pendamount,"₹")
        else:
            print("Payment amount is more than the pending amount. Payment failed.")
    elif bill_choice==3:
        print()
        accno=int(input("\nEnter 10-digit account number:"))
        pendamount=10000
        print("Pending Bill :",pendamount,"₹")
        atopay= float(input("Enter the amount you want to pay: "))
        if atopay <= pendamount:
            pendamount = pendamount-atopay
            print("\nBill Paid successfully! Remaining amount:",pendamount,"₹")
        else:
            print("Payment amount is more than the pending amount. Payment failed.")
    elif bill_choice==4:
        print()
        accno=int(input("\nEnter 10-digit account number:"))
        pendamount=5999
        print("Pending Bill :",pendamount,"₹")
        atopay= float(input("Enter the amount you want to pay: "))
        if atopay <= pendamount:
            pendamount = pendamount-atopay
            print("\nBill Paid successfully! Remaining amount:",pendamount,"₹")
        else:
            print("Payment amount is more than the pending amount. Payment failed.")
        
    else:
        print("input error!!")

def show_recharge_offers():
    print("\nChoose your mobile operator:\n")
    print("1. vi")
    print("2. jio")
    print("3. airtel")
    vi=["1. 28 days - 299₹ ","2. 3 months - 699₹ ","3. 1 year - 3200₹"]
    jio=["1. 28 days - 239₹ ","2. 3 months - 555₹ ","3. 1 year - 1999₹"]
    airtel=["1. 28 days - 299₹ ","2. 3 months - 750₹ ","3. 1 year - 2999₹"]
    recharge_choice = int(input("Enter your choice: "))
    print("\nRecharge Offers:")
    if recharge_choice==1:
        for i in range(3):
            print(vi[i])
    elif recharge_choice==2:
        for i in range(3):
            print(jio[i])
    elif recharge_choice==3:
        for i in range(3):
            print(airtel[i])
    else:
        print("input error!!")
    s=int(input("\nenter the plan number to pay :"))
    if s==1 or s==2 or s==3:
        print("\npayment successful !!")
    else :
        print("invalid input!!")


def request_money():
        requested_number = int(input("\nEnter the number you want to request money : "))
        reqmoney=int(input("\nEnter amount :"))
        print("Your request is send ✅")
        
# s=billlist()
# a=electricity_bills()
# r=show_recharge_offers()
# t=request_money()

def choose_option():
        print("Choose an option:")
        print("1. Electricity Bills")
        print("2. Mobile Recharge")
        print("3. Request Money")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            electricity_bills()
            choose_option()
        elif choice == 2:
            show_recharge_offers()
            choose_option()
        elif choice == 3:
            request_money()
            choose_option()
        else:
            print("invalid input!!")
           
welcome()
login()
choose_option()