class ATM:
  def __init__(self,account_number,account_balance=0):
    self.account_number=account_number
    self.account_balance=account_balance
  
  def Check_balance(self):
    return self.account_balance

  def deposit_funds(self,amount):
    self.account_balance += amount
    print(f"Deposited ${amount}. New balance: ${self.account_balance}")
    print()
  
  def withdraw_funds(self,withdrawed_amount):
    if self.account_balance-withdrawed_amount >=0:
      self.account_balance -= withdrawed_amount
      print(f"Withdrew ${withdrawed_amount}. New balance: ${self.account_balance}")
      print()
    else:
      print(f"{withdrawed_amount} cannot be withdrawed due to low funds, your balance is = {self.account_balance}")
      print()



class ATMController(ATM):
  def __init__(self,account_number,account_balance=0):
    super().__init__(account_number,account_balance)

  def menu(self):
    while True:
      print("1. Check Balance")
      print("2. Deposit Funds")
      print("3. Withdraw Funds")
      print("4. Quit")
      print()

      try:
        choice=int(input("Enter your choice = "))
        print()
        if choice == 1:
          print(f"Your balance is ${self.account_balance}")
          print()
        elif choice == 2:
          amount=int(input("Enter the amount to deposit = "))
          self.deposit_funds(amount)
        elif choice == 3:
          withdrawed_amount=int(input("Enter the amount to withdraw = "))
          print()
          self.withdraw_funds(withdrawed_amount)
        elif choice == 4:
          print("Thank you for using our ATM. Goodbye!")
          return True
        else:
          print("Invalid choice. Please select a valid option between 1-4.")
      except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
  account1 = ATMController("001", 10000)
  account2 = ATMController("002", 60000)
  account3 = ATMController("003", 100000)
  account4 = ATMController("004", 120000)
  account5 = ATMController("005", 40000)

  account_object = [account1,account2,account3,account4,account5]
  print("Welcome to the ATM!")
  while True:
    try:
      account_number = input("\nEnter your account number (001-005) or press 0 to exit = ")
      print()
      if account_number == "0":
        print("Thank you for using our ATM. Goodbye!")
        break
      for account in account_object:
        if account.account_number == account_number:
          exit_program = account.menu()
          if exit_program:  
            return
          break
      else:
        print("Invalid account number, we do not have this account number, try with a different account number (001-005) or call our helpline")
      
    except ValueError:
      print("Invalid input. Please enter a valid number.")
  

if __name__ == "__main__":
  main()

