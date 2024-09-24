



balance = 1015

while True:

  print("Select an option")

  print("1. Check Balance")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Exit")

  option = input("Enter option number:")

  if option == "1":
      print(f"Your current balance is: ${balance} ")


  elif option == "2":
      deposit_amount = int(input("Enter the amount: "))
      balance += deposit_amount
      print(F"You have successfully deposited ${deposit_amount}. New balance ${balance}")


  elif option == "3":
      Withdraw_amount = int(input("Enter amount: "))
      if Withdraw_amount <= balance :
          balance -= Withdraw_amount
          print(f"You have withdraw ${Withdraw_amount}. Your current balance is ${balance}")
      else:
          print("You don't have enough balance. ")


  elif option == "4":
      print("Thank you, Have a nice day")
      break
      

  else:
    print("Invalid, Please try again")