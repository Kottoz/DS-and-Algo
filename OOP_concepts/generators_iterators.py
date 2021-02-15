"""
Author: Mohamed Tarek Mohamed
E-mail:mohamedtareck95@gmail.com 
"""

"""
Example Name: Generators and Iterators

Describtion:
    Just playing witth Generators
"""

def fibonacci():
    a = 0 
    b = 1
    while True:
        yield a             #retport fib current number
        future = a + b      # 0, 1, 1, 2, 3, 5, 8, 13, 21,...
        a = b
        b = future


if __name__ == "__main__":
    print(fibonacci().__next__())

