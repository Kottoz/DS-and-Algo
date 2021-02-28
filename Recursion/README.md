# Recursion
One way to describe repetition within a computer program is the use of loops, such as Python’s while-loop and for-loop constructs . An entirely different way to achieve repetition is through a process known asrecursion.

Recursion is a technique by which a function makes one or more calls to itself during execution.

When one invocation of the function make a recursive call, that invocation is suspended until the recursive call completes.

With a recursive algorithm, we will account for each operation that is performed based upon the particular activation of the function that manages the flow of control at the time it is executed.

### The Factorial Function
each individual activation of factorial executes a constant number of operations. Therefore, we conclude that the overall number of operations for computing factorial(n) is O(n), as there are n+1 activations, each of which accounts for O(1) operations.

### Binary Search 

binary search, that is used to efficiently locate a target value within a sorted sequence of ```n``` elements

When the sequence is unsorted, the standard approach to search for a target value is to use a loop to examine every element, until either finding the target or exhausting the data set. This is known as the sequential search algorithm. This algorithm runs in ```O(n)``` time (i.e., linear time) since every element is inspected in the worst case.

### File Systems
operating systems define file-system directories in recursive way.
