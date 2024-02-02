class GooglePay:
    def __init__(self):
        self.user_data = {}
        self.bills = {
            1: "Adani Electricity",
            2: "Tata Power",
            3: "Torrent Power",
            4: "Vaghani Energy"
        }

    def welcome(self):
        print("Welcome to Google Pay")

    def login(self):
        name = input("Enter your name: ")
        number = input("Enter your mobile number: ")
        otp = input("Enter OTP received on your mobile: ")

        self.user_data = {
            'name': name,
            'number': number,
            'otp': otp
        }

    def choose_option(self):
        print("Choose an option:")
        print("1. Electricity Bills")
        print("2. Mobile Recharge")
        print("3. Recharge with Phone Number")
        print("4. Request Money")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.electricity_bills()
        elif choice == 2:
            self.mobile_recharge()
        elif choice == 3:
            self.recharge_with_phone_number()
        elif choice == 4:
            self.request_money()

    def electricity_bills(self):
        print("Choose an electricity provider:")
        for key, value in self.bills.items():
            print(f"{key}. {value}")        

        bill_choice = int(input("Enter your choice: "))
        bill_provider = self.bills.get(bill_choice)

        if bill_provider:
            account_number = input("Enter 10-digit account number: ")
            self.make_payment(bill_provider, account_number)
        else:
            print("Invalid choice.") 
    
    def mobile_recharge(self):
        print("Choose your mobile operator:")
        print("1. Jio")
        print("2. Airtel")
        print("3. Vi")


        operator_choice = int(input("Enter your choice: "))

        if operator_choice in [1, 2, 3]:
            self.show_recharge_offers()
        else:
            print("Invalid choice.")
