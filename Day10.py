#parent class : User
#Has a function to show user details
#Child class : Bank
#stores details about the account balance
#stores details about the amount
#Allows for deposits,withdraw,view_balance



#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds : Balance Available : $", self.balance)
        else:
            self.balance = self.balance = self.amount
            print("Account balance has been updated : $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance has been updated : $", self.balance)



# creating real time ecommerce of comparing prices of a product
from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
from pathlib import path

source1 = https://www.amazon.in/Dell-Latitude-3410-Core-10th/dp/B08KJ9D2HD/ref=sr_1_1?crid=1NEWURW6GMYL1&dchild=1&keywords=dell+i3+10th+gen+laptop&qid=1624375243&s=computers&sprefix=dell+i3%2Ccomputers%2C380&sr=1-1
source2 = https://www.flipkart.com/dell-inspiron-core-i3-10th-gen-4-gb-1-tb-hdd-256-gb-ssd-windows-10-home-5491-2-1-laptop/p/itm629c8d754c646?pid=COMFT2ZVUVG5UNYE&lid=LSTCOMFT2ZVUVG5UNYEJHAADX&marketplace=FLIPKART&q=dell+i3+10th+gen&store=6bo%2Fb5g&srno=s_1_5&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&fm=SEARCH&iid=bbf298ce-b80f-4e3d-bfb8-937641e16f18.COMFT2ZVUVG5UNYE.SEARCH&ppt=sp&ppn=sp&ssid=a0tq27ojc00000001624375497108&qH=4656e63d27998bd2

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_arugment('--start-maximized')
wd = webdriver.Chrome(r'D:\Learning\Practice\Selenium\
print("*************************************************************************** \n")
print("                   Starting Program, Please wait ....... \n")

print("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element_by_xpath("/htm1/body/div[1]/div/div[3]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]")
pr_name = wd.find_element_by_xpath("/htm1/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[1]/h1/span")
product = pr_name.text
r_price = f_price.text
# print (r_price[1:])
print (" ---> Successfully retrived the price from Flipkart \n")
time.sleep(2)

print("Connecting to Amazon")
wd.get(source2)
wd.implicitly_wait(wait_imp)
a_price = wd.find_element_by_xpath("/htm1/body/div[4]/div[2]/div[4]/div[10]/div[12]/div/table/tbody/tr[2]/td[2]/span[1]")
raw_p = a_price.text
# print (raw_p[2:8])
print (" ---> Successfully retrived the price from Amazon \n")
time.sleep(2)


# Final display
print ("#-------------------------------------------------------------------------#")
print("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: "+r_price[1:])
print(" Price available at Amazon is: "+raw_p[2:8])








































































      











        
        
