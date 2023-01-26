Tax = 0.2
Tip = 0.12
order_price = float(input("Сумма счета составляет (доллары):"))
tax = order_price * Tax
tip = order_price * Tip
rest = order_price - (tax + tip)
print("Сумма чаевых составляет", " % .2f" % tip, "доллара,", "сумма налога составляет", " % .2f" % tax, "доллара,",
      "Остаток суммы составляет", " % .2f" % rest,"долларов" )