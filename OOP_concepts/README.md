# Object Oriented Programming Goals, Principles, and patterns

## Object Oriented Programming Goals

- The main actor of in OOP is **Object** which is an istance of a **Class**.

- Class is like a real world classes like Car, which is all cars around the world despise it is four x four, hybird, electrical, hatchback cars, and so on all of them are instancess from the same **Class** which is car, tesla is an instance from that class which has its aspects and features.

- Software implementations should achieve robustness, adaptability, and reusability.

    - **Robustness**: a program produces the right output for all the anticipated inputs in the program’s application. In addition, we want software to be robust, that is, capable of handling unexpected inputs that are not explicitly defined for its application.
        - For example, if a program is expecting a positive integer (perhaps representing the price of an item) and instead is given a negative integer,then the program should be able to recover gracefully from this error.

    - **Portability**, which is the ability of software to run with minimal change on different hardware and operating system platforms. 

    - **Reusability**: the same code should be usable as a component of different systems in various applications.


## Object Oriented Programming Design Principles
- [Modularity](#modularity)
- [Abstraction](#abstraction)
- [Encapsulation](#ancapsulation)

### Modularity

- **Modularity** refers to an organizing principle in which different components of a software system are divided into separate functional units.
- Using modularity to bring a clarity of thought that provides a natural way of organizing functions into distinct manageable units.
- In Python, we have already seen that a module is a collection of closely related functions and classes that are defined together in a single file of source code. 
- The use of modularity helps support the goals. Robustness is greatly increased because it is easier to test and debug separate components
before they are integrated into a larger software system.
- bugs that persist in a complete system might be traced to a particular component, which can be fixed in relative isolation. The structure imposed by modularity also helps enable software reusability.
- If software modules are written in a general way, the modules can be reused when related need arises in other contexts.

### Abstraction

- **Abstraction** Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on how to use the application.
- An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.
- An ADT specifies what each operation does, but not how it does it.
- Look at Abstraction examble in notebook.

### Encapsulation

- Different components of a software system should not reveal the internal details of their respective implementations. One of the main advantages of encapsulation is that it gives one programmer freedom to implement the details of a component, without concern that other programmers will be writing code that intricately depends on those internal decisions.
-  Encapsulation yields robustness and adaptability

## Object Oriented Programming Design Patterns
- Computing researchers and practitioners have developed a variety of organizational concepts and methodologies for designing quality object-oriented software
that is concise, correct, and reusable.
- design patterns fall into two groups—patterns for solving algorithm design problems and patterns for solving software engineering problems. 
- The algorithm design patterns we discuss include the following:
    - Recursion (Chapter 4).
    - Amortization (Sections 5.3 and 11.4)
    - Divide-and-conquer (Section 12.2.1)
    - Prune-and-search, also known as decrease-and-conquer (Section 12.7.1)
    - Brute force (Section 13.2.1)
    - Dynamic programming (Section 13.3).
    - The greedy method (Sections 13.4.2, 14.6.2, and 14.7)

- Likewise, the software engineering design patterns we discuss include:
    - Iterator (Sections 1.8 and 2.3.4)
    - Adapter (Section 6.1.2)
    - Position (Sections 7.4 and 8.1.2)
    - Composition (Sections 7.6.1, 9.2.1, and 10.1.4)
    - Template method (Sections 2.4.3, 8.4.6, 10.1.3, 10.5.2, and 11.2.1)
    - Locator (Section 9.5.1)
    - Factory method (Section 11.2.1)
 


# SoftWare Development
- Traditional software development involves several phases. Three major steps are:
    1. [Design](#design)
    2. [Implementation](#mplementation)
    3. [Testing and Debugging](#testing-and-debugging)

## Design
- In the design step that we decide how to divide the workings of our program into classes, we decide how these classes will interact, what data each will store, and what actions each will perform.
- Indeed, one of the main challenges that beginning programmers face is deciding what classes to define to do the work of their program. While general prescriptions are hard to come by, there are some rules of thumb that we can apply when determining how to design our classes:
    1. **Responsibilities**: 
        - Divide the work into different actors, each with a different responsibility.
        - Try to describe responsibilities using action verbs.
    2. **Independence**: 
        - Define the work for each class to be as independent from other classes as possible. 
        - Subdivide responsibilities between classes so that each class has autonomy over some aspect of the program. 
        - Give data (as instance variables) to the class that has jurisdiction over the actions that require access to this data.
    3. **Behaviors**: 
        - Define the behaviors for each class carefully and precisely, so that the consequences of each action performed by a class will be well understood by other classes that interact with it. 
        - These behaviors will define the methods that this class performs, and the set of behaviors for a class are the interface to the class, as these form the means for other pieces of code to interact with objects from the class.

- We can use UML to design our project like the following ![Credit Card UML Diagram](DS-and-Algo/OOP_concepts/imges/CreditCardUMLDiagram.png) 

## Testing and Debugging
- Verifying the correctness of a program over all possible inputs is usually infeasible, we should aim at executing the program on a representative subset of inputs.
-  At the very minimum, we should make sure that every method of a class is tested at least once.
- Programs often tend to fail on special cases of the input.
- For example, when testing a method that sorts (that is, puts in order) a sequence of integers, we should consider the following inputs:
    - The sequence has zero length (no elements).
    - The sequence has one element.
    - All the elements of the sequence are the same.
    - The sequence is already sorted.
    - The sequence is reverse sorted.
- It is also advantageous torun the program on a large collection of randomly generated inputs.
- The dependencies among the classes and functions of a program induce a hierarchy. if we have Class A which is dependant on Class A and we need to test functionality of class A how do we do that?, there are two common stratigies Bottom-Up and top-Down.
    - Top-Down is called stubbing, a boot-strapping technique that replaces a lower-level component with a stub, a replacement for the component that simulates the functionality of the original. For example, if function A calls function B to get the first line of a file, when testing A we can replace B with a stub that returns a fixed string.
    - Bottom-up testing proceeds from lower-level components to higher-level components. For example, bottom-level functions, which do not invoke other functions, are tested first, followed by functions that call only bottom-level functions, and so on. 
    - 
- class that does not depend upon any other classes can be tested before another class that depends on the former. this is called **Unit Test**, functionality of a specific component is tested in isolation of the larger software project.
- Python provides several forms of support for automated testing. When functions or classes are defined in a module, testing for that module can be embedded
in the same file. 
```python
if __name__ == "__main__" :
# perform tests...
```
- will be executed when Python is invoked directly on that module, but not when the module is imported for use in a larger software project. It is common to put tests in such a construct to test the functionality of the functions and classes specifically defined in that module.
- More robust support for automation of unit testing is provided by Python’s *unittest* module. 
- This framework allows the grouping of individual test cases into larger test suites

- The simplest debugging technique consists of using print statements to track the values of variables during the execution of the program.
- A better approach is to run the program within a debugger.


# Class Definition
- In Python, every piece of data is represented as an instance of some class. 
- A class provides a set of behaviors in the form of member functions (also known as methods).
- A class also serves as a blueprint for its instances, effectively determining the way that state information for each instance is represented in the form of attributes (also known as fields, instance variables, or data members).

###  Operator Overloading and Python’s Special Methods
- We know that each element in python is instance(Object/Container) of class for examble ```x = 5``` is integer as python is a dynamic typing language so you don't need to make a decleration. 
- The mechanism works like this: If we have an expression ```"x + y"``` and x is an instance of class ```K```, then Python will check the class definition of ```K```. If ```K``` has a method ```__add__``` it will be called with ```x.__add__(y)```, otherwise we will get an error message:
```python
Traceback (most recent call last):
  File "", line 1, in 
TypeError: unsupported operand type(s) for +: 'K' and 'K'
``` 
- You can see that

```python
x = 5 
#is like 
x = int(5) #Initialize an instance from int class with value = 5 
y = int(7) #Initialize an instance from int class with value = 5 

#so if we need to add value of x instance to y we just do 
z = x + y
>>> 12
``` 
- Python’s built-in classes provide natural semantics for many operators.
- By default, the + operator is undefined for a new class.
- However, the author of a class may provide a definition using a technique known as operator overloading.
- Best resource to learn more about [Operator Overloading](https://www.python-course.eu/python3_magic_methods.php).
- see Length class examble. 
    - How to use [Class attributes](https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide#:~:text=A%20Python%20class%20attribute%20is,an%20instance%20of%20a%20class.&text=For%20Java%20or%20C%2B%2B%20programmers,identical%E2%80%94to%20the%20static%20member.)

###  Implied Methods
- As a general rule, if a particular special method is not implemented in a user-defined class, the standard syntax that relies upon that method will raise an exception. For example, evaluating the expression, a+b, for instances of a user-defined class without add or radd will raise an error.
- However, there are some operators that have default definitions provided by Python, in the absence of special methods.
- For example, the bool method, which supports the syntax ```if foo:```  has default semantics so that every object other than ```None``` is evaluated as ```True```
- Container types, the ```__len__``` method is typically defined to return the size of the container.


###  Iterators
- An iterator for a collection provides one key behavior: It supports a special method named next thatreturns the ```__next__``` element of the collection, if any, or raises a StopIteration exception to indicate that there are no further elements.
- There are many types of objects in Python that qualify as being iterable. Basic container types, such as list, tuple, and set, qualify as iterable types.
- A string can produce an iteration of its characters, a dictionary can produce an iteration of its keys, and a file can produce an iteration of its lines. Userdefined types may also support iteration. 
- An iterator is an object that manages an iteration through a series of values. If variable, ```i```, identifies an iterator object, then each call to the built-in function, ```next(i)```, produces a subsequent element from the underlying series, with a ```StopIteration``` exception raised to indicate that there are no further elements.
- An iterable is an object, obj, that produces an iterator via the syntax ```iter(obj)```.
- calling ```iter(data)``` on a list instance produces an instance of the list iterator class. That iterator does not store its own copy of the
list of elements. Instead, it maintains a current index into the original list, representing the next element to be reported. Therefore, if the contents of the original list are modified after the iterator is constructed, but before the iteration is complete, the iterator will be reporting the updated contents of the list.

### Generators
- the most convenient technique for creating iterators in Python is through the use of generators. A generator is implemented with a syntax that is very similar to a function, but instead of returning values, a ```yield``` statement is executed to indicate each element of the series. 






# Inheritance
- A natural way to organize various structural components of a software package is in a hierarchical fashion, with similar abstract definitions grouped together in a level-by-level manner that goes from specific to more general as one traverses up the hierarchy. 
- In object-oriented terminology, the existing class is typically described as the base class, parent class, or superclass, while the newly defined class is known as the subclass or child class.
- There are two ways in which a subclass can differentiate itself from its superclass. A subclass may specialize an existing behavior by providing a new implementation that overrides an existing method. A subclass may also extend its superclass by providing brand new methods.
- look at predatory creditcard file.

### Abstract Base Classes
- When defining a group of classes as part of an inheritance hierarchy, one technique for avoiding repetition of code is to design a base class with common functionality that can be inherited by other classes that need it.
-  The real purpose of the ABC class was to centralize the implementations of behaviors that other classes needed, thereby streamlining the code that is relegated to those subclasses.
