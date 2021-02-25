# Chapter Three - Design Analysis

## Experimental Studies
If an algorithm has been implemented, we can study its running time by executing it on various test inputs and recording the time spent during each execution. 
A simple approach for doing this in Python is by using the time function of the time module. 
This function reports the number of seconds, or fractions thereof, that have elapsed since a benchmark time known as the epoch. 
The choice of the epoch is not significant to our goal, as we can determine the elapsed time by recording the time just before the algorithm and the time just after the algorithm, and computing their difference, as follows:
```Python
from time import time
start time = time( ) # record the starting time
run algorithm
end time = time( ) # record the ending time
elapsed = end time − start time # compute the elapsed time
```

An elapsed time measured in this fashion is a decent reflection of the algorithm efficiency, but it is by no means perfect. 
The time function measures relative to what is known as the “wall clock.” Because many processes share use of a computer’s central processing unit (or CPU), the elapsed time will depend on what other processes are running on the computer when the test is performed. A fairer metric is the number of CPU cycles that are used by the algorithm. 
This can be determined using the clock function of the time module, but even this measure might not be consistent if repeating the identical algorithm on the identical input, and its granularity will depend upon the computer system. 
Python includes a more advanced module, named timeit, to help automate such evaluations with repetition to account for such variance among trials.

- Experimental running times of two algorithms are difficult to directly compare unless the experiments are performed in the same hardware and software
environments.

Our goal is to develop an approach to analyzing the efficiency of algorithms that:
1. Allows us to evaluate the relative efficiency of any two algorithms in a way
that is independent of the hardware and software environment.
2. Is performed by studying a high-level description of the algorithm without
need for implementation.
3. Takes into account all possible inputs.

--- 

To analyze the running time of an algorithm without performing experiments, we perform an analysis directly on a high-level description of the algorithm (either in the form of an actual code fragment, or language-independent pseudo-code). We define a set of primitive operations such as the following:
- Assigning an identifier to an object
- Determining the object associated with an identifier
- Performing an arithmetic operation (for example, adding two numbers)
- Comparing two numbers
- Accessing a single element of a Python list by index
- Calling a function (excluding operations executed within the function)
- Returning from a function.

we will associate, with each algorithm, a function ```f(n)``` that characterizes the number of primitive operations that are performed as a function of the input size ```n```.

we will characterize running times in terms of the worst case, as a function of the input size, n, of the algorithm. Worst-case analysis is much easier than average-case analysis, as it requires only the ability to identify the worst-case input, which is often simple. Also, this approach typically leads to better algorithms. Making the standard of success for an algorithm to perform well in the worst case necessarily requires that it will do well on every input. That is, designing for the worst case leads to stronger algorithmic “muscles,” much like a track star who always practices by running up an incline.

### the seven most important functions used in the analysis of algorithms
1. [The Constant Function](#the-constant-function)
2. [The Logarithm Function](#the-logarithm-function)
3. [The Linear Function](#the-linear-function)
4. [The N-Log-N Function](#the-n-log-n-function)
5. [The Quadratic Function](#the-quadratic-function)
6. [The Cubic Function and Other Polynomials](#the-cubic-function-and-other-polynomials)
7. [The Exponential Function](#the-exponential-function)

#### The Constant Function
- The simplest function.
- ```f(n) = c```
- for any argument ```n```, the constant function ```f(n)``` assigns the value ```c```. In other words, it does not matter what the value of n is; ```f(n)``` will always be equal to the constant value ```c```.
- the most fundamental constant function is ```g(n) = 1```
- the constant function is useful in algorithm analysis, because it characterizes the number of steps needed to do a basic operation on a computer, like adding two numbers, assigning a value to some variable, or comparing two numbers.

#### The Logarithm Function
- This function is defined as follows: ```x = logb n``` if and only if ```bx = n```. By definition, ```logb 1 = 0```. The value ```b``` is known as the base of the logarithm.
- The most common base for the logarithm function in computer science is 2, as computers store integers in binary, and because a common operation in many algorithms is to repeatedly divide an input in half. In fact, this base is so common that we will typically omit it from the notation when it is 2. That is, for us, ```logn = log2 n```.

we can easily compute the smallest integer greater than or equal to logb n (its so-called ceiling, ```logb n```). For positive integer, ```n```, this value is equal to the number of times we can divide ```n``` by ```b``` before we get a number less than or equal to 1. 
For example, the evaluation of  ```log3 27``` is ```3```, because ```((27/3) 3)/3 = 1```. Likewise,  ```log4 64 is 3```, 
because ```((64/4)/4)/4 = 1```, and  ```log2 12``` is ```4```, because ```(((12/2)/2)/2)/2 = 0.75 ≤ 1```.

#### The Linear Function
- ```f(n) = n```
- The linear function also represents the best running time we can hope to achieve for any algorithm that processes each of n objects that are not already in the computer’s memory, because reading in the n objects already requires n operations.

#### The N-Log-N Function
- the n-log-n function, ```f(n) = nlogn```
- This function grows a little more rapidly than the linear function and a lot less rapidly than the quadratic function.
- we would greatly prefer an algorithm with a running time that is proportional to nlogn, than one with quadratic running time. 

#### The Quadratic Function
- quadratic function, ```f(n) = n^2```.
- The main reason why the quadratic function appears in the analysis of algorithms is that there are many algorithms that have nested loops, where the inner loop performs a linear number of operations and the outer loop is performed a linear number of times. Thus, in such cases, the algorithm performs ```n · n = n2``` operations.

#### The Cubic Function and Other Polynomials
- the cubic function, ```f(n) = n3```.
- Polynomials 

#### The Exponential Function
- ```f(n) = b^n```.
- where b is a positive constant, called the base, and the argument n is the exponent.
-  As was the case with the logarithm function, the most common base for the exponential function in algorithm analysis is b = 2.



## Asymptotic Analysis
In algorithm analysis, we focus on the growth rate of the running time as a function of the input size n.

### The “Big-Oh” Notation
- ```f(n) ≤ cg(n)```
- ```f(n) is big-Oh of g(n)```
- The big-Oh notation allows us to say that a function f(n) is “less than or equal to” another function g(n) up to a constant factor and in the asymptotic sense as n grows toward infinity.
- The big-Oh notation is used widely to characterize running times and space bounds in terms of some parameter n, which varies from problem to problem, but is always defined as a chosen measure of the “size” of the problem.
- The big-Oh notation allows us to ignore constant factors and lower-order terms and focus on the main components of a function that affect its growth.
- In general, we should use the big-Oh notation to characterize a function as closely as possible.

### Big-Omega
Just as the big-Oh notation provides an asymptotic way of saying that a function is “less than or equal to” another function.

### Big-Theta
say that two functions grow at the same rate, up to constant factors. We say that ```f(n) is Θ(g(n))```.

