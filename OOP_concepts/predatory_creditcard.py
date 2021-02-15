"""
Author: Mohamed Tarek Mohamed
E-mail: mohamedtareck95@gmail.com
"""

"""
Implementing a subclass that, for lack of a better name, we name PredatoryCreditCard. The new class will differ from the original in two ways: 
(1) if an attempted charge is rejected because it would have exceeded the credit limit, a $5 fee will be charged, and 
(2) there will be a mechanism for assessing a monthly interest charge on the outstanding balance, based upon an Annual Percentage Rate (APR) specified as a constructor parameter.

"""
import CreditCard

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acount, limit, apr):

        """    Create a new predatory credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)"""

        super().__init__(customer, bank, acount, limit) # call super constructor
        self._apr = apr

    def charge(self, price):
        """    Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied."""
        success = super().charge(price)  # call inherited method

        if not success:
            self._balance += 5  # assess penalty
        return success          # caller expects return value
        
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self. apr, 1/12)
            self. balance = monthly_factor


    

if __name__ == "__main__":
    print("Hello")


