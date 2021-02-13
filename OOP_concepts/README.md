@Kottoz
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
 


## Class Definition 



## Class Definition 
    - In Python, every piece of data is represented as an instance of some class
