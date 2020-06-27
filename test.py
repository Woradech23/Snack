StockOriginal = 100
StockCoffee = 100
StockChocolate = 100
Budget = 1000
Choice = 0
history = []
i = 0
while True:
  print("==Login==")
  print("Username :",end ="")
  Username = input()
  print("Password :",end ="")
  Password = input()

  if(Username=="ct" and Password=="123"):
    while Choice != "4":
      print("")
      print("==Menu==")
      print("Stock: ")
      print("Original :",end="")
      print(StockOriginal)
      print("Coffee: ",end ="")
      print(StockCoffee)
      print("Chocolate: ",end ="")
      print(StockChocolate)
      
      print("")
      print("Budget: ",end="")
      print(Budget)
      print("")
      print("=Select=")
      print("1.Sell")
      print("2.Buy")
      print("3.History")
      print("4.Close day")

      print("")
      print("Select Choice:",end="")
      Choice = input()
      
      if(Choice=="1"):
        print("Sell Original: ",end ="")
        SellOriginal = int(input())
        print("Sell Coffee: ",end ="")
        SellCoffee = int(input())
        print("Sell Chocolate: ",end="")
        SellChocolate = int(input())

        a = StockOriginal-SellOriginal
        StockOriginal = a

        b = StockCoffee-SellCoffee
        StockCoffee = b

        c = StockChocolate-SellChocolate
        StockChocolate = c

        d = Budget+(SellOriginal*50)+(SellCoffee*50)+(SellChocolate*50)
        Budget = d



      elif(Choice=="2"):
        print("Buy Original: ",end ="")
        BuyOriginal = int(input())
        print("Buy Coffee: ",end ="")
        BuyCoffee = int(input())
        print("Buy Chocolate: ",end="")
        BuyChocolate = int(input())

        a = StockOriginal+BuyOriginal
        StockOriginal = a

        b = StockCoffee+BuyCoffee
        StockCoffee = b

        c = StockChocolate+BuyChocolate
        StockChocolate = c

        d = Budget-((BuyOriginal*40)+(BuyCoffee*40)+(BuyChocolate*40))
        Budget = d



      elif(Choice == "3"):
        print("=History=")
        for i in range(len(history)):
          print("Day",end="")
          print(i)
          print("Sell")
          print("Buy")
        

      elif(Choice == "4"):
        print()



      else:
        print("the Choice that you select is out of order")
      
    i = i+1
    print("End the Day")
    Choice = 0


  else:
    print("Username or Password is incorrect plese try again")
