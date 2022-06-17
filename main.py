from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m=Menu()
c=CoffeeMaker()
mm=MoneyMachine()

is_on=True
while is_on:
  choice=input("What would you like").lower()
  if choice=="off":
    is_on=False
  elif choice=="report"
    c.report()
    mm.report()
  else:
    drink=m.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)

