class Atm:
#constructer(special funcation)->superpower
   def __init__(self):
    self.pin=""
    self.balance=0
    self.menu()
   def menu(self):
    user_input=input(
      """
      HI how can i help you?
      1. press 1 to creat pin
      2. press 2 to change pin
      3. press 3 to check balance
      4.press 4 to withdraw
      5. anything else to exit
      """
  )
    if user_input=="1":
      #creat pin
      self.creat_pin()
    elif user_input=="2":
      #change pin
      self.change_pin()
    elif user_input=="3":
        #check balance
        self.check_balance()

    elif user_input=="4":
          #withdraw
          self.withdraw()
    else:
        exit()

   def creat_pin(self):
    user_pin=int(input("enter your pin-> "))
    self.pin=user_pin
    user_balance=int(input("enter your balance-> "))
    self.balance=user_balance
    print("WOw! pin created successfully.")
    self.menu()

   def change_pin(self):
    old_pin=int(input("enter your old pin->"))
    if old_pin == self.pin:
      new_pin=int(input("enter your new pin=>"))
      self.pin=new_pin
      print("pin changed successfully")
      self.menu()
    else:
        print("nhi ker skta re baba")
        self.menu()

   def check_balance(self):
        user_pin = int(input("Enter your pin: "))
        if user_pin == self.pin:
            print("Your balance is: ", self.balance)
        else:
            print("Incorrect pin.")
        self.menu()

   def withdraw(self):
        user_pin = int(input("Enter your pin: "))
        if user_pin == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful. Your new balance is: ", self.balance)
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect pin.")
        self.menu()

obj =Atm()