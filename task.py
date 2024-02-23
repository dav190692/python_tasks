
#Task_1 Start

# class TransationLog:
#     def __init__(self):
#         self.__transactions = []
    
#     def log_transaction(self, transaction_detail):
#         self.__transactions.append(transaction_detail)
    
#     def display_transactions(self):
#         print("Transactions Log")
#         for index, transaction in enumerate(self.__transactions, start=1):
#             print(f"{index} : {transaction}")



# class CustomerAccount:
#     def __init__(self, customer_id:int, customer_name:str, account_balance:int):
#         self.__customer_id = self.set_customer_id(customer_id)
#         self.__customer_name = self.set_customer_name(customer_name)
#         self.__account_balance = self.set_customer_account_balance(account_balance)
#         self.transation_log = TransationLog()


#     def set_customer_account_balance(self, account_balance):
#         if account_balance > 0 and isinstance(account_balance, int):
#             return account_balance
#         else:
#             raise ValueError
    

#     def set_customer_id(self, customer_id):
#         if customer_id > 0 and isinstance(customer_id, int):
#             return customer_id
#         else:
#             raise ValueError

#     def set_customer_name(self, customer_name):
#         if not customer_name == "" and isinstance(customer_name, str):
#             return customer_name
#         else:
#             raise ValueError


#     def deposit(self, amount):
#         if amount > 0:
#             self.__account_balance += amount
#             self.transation_log.log_transaction(f"Deposited {amount}. New balance: {self.__account_balance}")
#         else:
#             print("Wrong deposit amount. Please deposit a positive value.")
    
    
#     def withdraw(self,amount):
#         if amount > 0 and self.__account_balance >= amount:
#             self.__account_balance -= amount
#             self.transation_log.log_transaction(f"Withdraw {amount}. New balance: {self.__account_balance}")
#         else:
#             print("Wrong withdraw amount. Please withdraw corect value.")    
        
    
# account1 = CustomerAccount(1, "Davit", 30000)
# account1.deposit(200)
# account1.transation_log.display_transactions()
# account1.withdraw(4000)
# account1.transation_log.display_transactions()

#Task1 End

#Task2 start
# class DynamicPricing:
 
#     def dynamic_pricing(self, count1, count2, price):
#         if count1 == count2:
#             print('The product quantity has not changed')
#         elif count1 == 0:
#             print('The product is completely sold out')
#         else:
#             percentage_based_in_counts = 100 - ((count2 *100)/count1)
#             discount_amount = (price * percentage_based_in_counts)/100 
#             price -= discount_amount
#             print(f'It is a dynamically generated price {price}')
             




# class Product:
#     def __init__(self, product_id, product_name, product_price, inventory_count):
#         self.__product_id = self.set_product_id(product_id)
#         self.__product_name = self.set_product_name(product_name)
#         self.__product_price = self.set_product_price(product_price)
#         self.__inventory_count = self.set_inventory_count(inventory_count)
#         self.count_after_cell = 0 
#         self.dynamic_pricing = DynamicPricing()

#     def set_product_id(self, product_id):
#         if product_id > 0 and isinstance(product_id, int):
#             return product_id
#         else:
#             raise ValueError

#     def set_product_name(self, product_name):
#         if not product_name == '' and isinstance(product_name, str):
#             return product_name
#         else:
#             raise ValueError


#     def set_product_price(self, product_price):
#         if product_price > 0 and isinstance(product_price, int):
#             return product_price
#         else:
#             raise ValueError
    
#     def set_inventory_count(self, inventory_count):
#         if inventory_count > 0 and isinstance(inventory_count, int):
#             return inventory_count
#         else:
#             raise ValueError
        
#     def apply_discount(self, discount_percentage):
#         if discount_percentage > 0 and isinstance(discount_percentage,int):
#             discount_value = (self.__product_price * discount_percentage)/100
#             if discount_value >= self.__product_price:
#                 print("Please write a small value for discount_percentage")
#             else:
#                 self.__product_price -= discount_value
#                 print(f"product new price is {self.__product_price}")
    
#     def sell(self, quantity):
#         if quantity <= self.__inventory_count and isinstance(quantity, int):
#             self.count_after_sell = self.__inventory_count - quantity
#             print(self.count_after_sell)
#         else:
#             raise ValueError('Please write true quantity value')
        
#     def dynamic_pricing_self(self):
#         return self.dynamic_pricing.dynamic_pricing(self.__inventory_count, self.count_after_sell, self.__product_price)




# product1 = Product(1, 'Milk', 6700, 23)

# product1.apply_discount(10)
# product1.apply_discount(10)
# product1.sell(19)
# product1.dynamic_pricing_self()



#task2 End


