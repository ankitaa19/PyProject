#create a python program of Google_Pay program using claas, object, inheritance, array,loops ,strings, self.lists, dictionaries, datatypes , modules and package create such that the google pay in the beggining it should wlcome you then ask for login next ask user to enter 1.name, 2, number ,3. otp. later ask user what you want to proceed with 1. electricity bills , 2. Mobile recharge, 3. Recharge with number, 4.Request money if choosen electricity display the self.list as 1. adani electricity 2. tata power 3. torrent power 4. vaghani energy .if selected any of these proceed to ask user to enter 10 dighit number and procced with the payment method, 2.monile recharge in this ask the user which sim you own 1, jio 2.airtel 3. Vi . if choosen 1 show three offer of 28days and 400rupees, secong 3months 790rupees third 1yr 3200rupees same for jio and airtel offers apply same offers 3. pay with phone number in this let the user enter the phone number  after entering the number let it display msg payment done 4. option for request money in this let user enter the number from the person he wants the money from then later display the default msg as user has accepted the request and ask user if he wants the money to be credited in his account in y/n if y display as 10,000 rupees credited if n exit 
class Pay:
    def __init__(self):
        #user data 
        self.user_data = {}
        self.bills = {
            1: "Adani Electricity",
            2: "Tata Power",
            3: "Torrent Power",
            4: "Vaghani Energy"
        }

    def welcome(self):
        #Welcome message
        print("Welcome !! Welcome !!")

    def login(self):
        #User Information
        name = input("Enter your name: ")
        number = input("Enter your mobile number: ")
        otp = input("Enter MPIN: ")
        # Stored data
        self.user_data = {
            'name': name,
            'number': number,
            'otp': otp
        }

    def choose_option(self):
        #Menu of options in google pay
        print("Choose an option:")
        print("1. Electricity Bills")
        print("2. Mobile Recharge")
        print("3. Request Money")
        choice = int(input("Enter your choice: "))

        #User Choice
        if choice == 1:
            self.electricity_bills()
        elif choice == 2:
            self.show_recharge_offers()
        elif choice == 3:
            self.request_money()

    def electricity_bills(self):
        #paying bills
        print("Choose an electricity provider:")
        for key, value in self.bills.items():
            print(f"{key}. {value}")

        # preferred electricity provider
        bill_choice = int(input("Enter your choice: "))
        bill_provider = self.bills.get(bill_choice)

        #electricity Payment
        if bill_provider:
            account_number = input("Enter 10-digit account number: ")
            
            # pending amount
            pending_amount = 740
            print(f"Pending amount: {pending_amount} INR")

            #User amount
            paid_amount = float(input("Enter the amount you want to pay: "))

            # User ammount is sufficient or not
            if paid_amount >= pending_amount:
                #successful payment
                pending_amount -= paid_amount
                print(f"Bill Paid successfully! Remaining amount: {pending_amount} INR")
                self.make_payment(bill_provider, account_number)
            else:
                #insufficient payment
                print("Payment amount is less than the pending amount. Payment failed.")
        else:
            #invalid choice
            print("Invalid choice.")

  
    def show_recharge_offers(self):
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

 

    def request_money(self):
        requested_number = int(input("\nEnter the number you want to request money : "))
        reqmoney=int(input("\nEnter amount :"))
        print("Your request is send ✅")

from in import 
class Invesment:
