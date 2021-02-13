"""
Author: Mohamed Tarek Mohamed
E-mail:mohamedtareck95@gmail.com 
"""

"""
Example Name: CreditCard

Describtion:
    The instances defined by the CreditCard class provide a simple model for traditional credit cards. 
    They have identifying information about the customer, bank, account number, credit limit, andcurrent balance. 
    The class restricts charges that would cause a card’s balance to go over its spending limit, but it does not 
    charge interest or late payments (we revisit such themes).
"""

class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acount, limit):
        """Create a new credit card instance"""
        """
        
        The initial balance is zero.
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        
        """

        self._customer = customer
        self._bank = bank
        self._account = acount
        self._limit = limit
        self._balance = 0 

    def get_customer(self):
        """Return customer name"""
        return self._customer
        
    def get_bank(self):
        """Return bank name"""
        return self._bank
        
    def get_account(self):
        """Return account id"""
        return self._account

    def get_limit(self):
        """Return card limit"""
        return self._limit
        
    def get_balance(self):
        """Return current account balance"""
        return self._balance

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit. 
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
            
    def make_payment(self, amount):
        """
        Process customer payment that reduces balance
        """
        self._balance -= amount


#class testing
if __name__ == "__main__":
    """    
    inserting three cards into a list named wallet. 
    We use loops to make some charges and payments, and 
    use various accessors to print results to the console.
    """
    wallet = []
    wallet.append(CreditCard( 'John Bowman' , 'California Savings' ,'56 5391 0375 9387 5309' , 2500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Federal' ,'58 3485 0399 3395 1954' , 3500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Finance' ,'60 5391 0375 9387 5309' , 5000) )

    for val in range(0, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print(f"customer : {wallet[c].get_customer()}")
        print(f"bank : {wallet[c].get_bank()}")
        print(f"Account : {wallet[c].get_account()}")
        print(f"limit : {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f"new balance = {wallet[c].get_balance()}")
