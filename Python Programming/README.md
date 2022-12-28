# Python Crash Course

## Expect to Learn?

* Learn about different kinds of data and the ways you can store data in lists and dictionaries within your programs.
* Learn to build collections of data and work through those collections in efficient ways.
* Learn to use while and if loops to test for certain conditions are true.
* A technique that greatly helps to automate processes.
* Learn to accept input from users to make your programs interactive and to keep your programs running as long as the user is active.
* Explore how to write functions to make parts of a program reusable, to write blocks of code that perform certain actions once, which you can then use as many times.
* Learn to write programs that handle common errors gracefully.
* Learning how to write tests for a code to develop programs without worrying about introducing bugs.
* AND MUCH MORE


### Python Keywords

Each of the following keywords has a specific meaning, and you’ll see an error if you try to use them as a variable name.
False    class      finally    is         returnNone     continue   for        lambda     tryTrue     def        from       nonlocal   whileand      del        global     not        withas       elif       if         or         yieldassert   else       import     passbreak    except     in         raise

### Python Built-in Functions
You won’t get an error if you use one of the following readily available built-in functions as a variable name, but you’ll override the behavior of that function:


abs()          
divmod()      
input()         
open()      
staticmethod()
all()          
enumerate()
int()           
ord()       
str()
any()          
eval()        
isinstance()    pow()       sum()basestring()   execfile()    issubclass()    print()     super()  bin()          file()        iter()          property()  tuple()bool()         filter()      len()           range()     type() bytearray()    float()       list()          raw_input() unichr()callable()     format()      locals()        reduce()    unicode()chr()          frozenset()   long()          reload()    vars() classmethod()  getattr()     map()           repr()      xrange()cmp()          globals()     max()           reversed()  zip()compile()      hasattr()     memoryview()    round()     __import__()complex()      hash()        min()           set()       apply()delattr()      help()        next()          setattr()   buffer()dict()         hex()         object()        slice()     coerce()dir()          id()          oct()           sorted()    intern()

### Resources 
*  Excellent resource for exploring the Python standard library is a site called Python Module of the Week. Go to http://pymotw.com/ and look at the table of contents.
## Summary 

### Chapter 1 - Getting Started
  * learned a bit about Python in general, and installed Python to windows system.
  * learned how to Run Python in Visual Studio Code on Windows.
  * learned to run snippets of Python code in a terminal session.
  * Ran actual program, hello_world.py and learned a bit about troubleshooting.

### Chapter 2 - VARIABLES AND SIMPLE DATA TYPES
 * learned to work with variables and to use descriptive variable names and how to resolve name errors and syntax errors when they arise.
 * learned what strings are and how to display strings using lowercase, uppercase, and titlecase.
 * learned to strip unneeded whitespace from different parts of a string.
 * learned to write explanatory comments to make your code easier for you and others to read.

### <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%203%20-%20Lists">Chapter 3 - LISTS</a>

* learned what lists are and how to work with the individual items in a list. 
* learned how to define a list and how to add and remove elements. 
* learned to sort lists permanently and temporarily for display purposes. 
* learned how to find the length of a list and how to avoid index errors when working with lists.


### <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%204%20-%20working%20with%20lists">Chapter 4 - WORKING WITH LISTS</a>

* learned how to work efficiently with the elements in a list. 
* learned how to work through a list using a for loop, how Python uses indentation to structure a program, and how to avoid some common indentation errors. 
* learned to make simple numerical lists, as well as a few operations which can be perform on numerical lists. 
* learned how to slice a list to work with a subset of items and how to copy lists properly using a slice. 
* learned about tuples, which provide a degree of protection to a set of values that shouldn’t change, and how to style your increasingly complex code to make it easy to read.

### <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%205%20-%20if%20statements">Chapter 5 - IF STATEMENTS</a>

* learned how to write conditional tests, which always evaluate to True or False. 
* learned to write simple if statements, if-else chains, and if-elif-else chains. Useed these structures to identify particular conditions needed to test and to know when those conditions have been met in your programs. 
* learned to handle certain items in a list differently than all other items while continuing to utilize the efficiency of a for loop. 
* revisited Python’s style recommendations to ensure that your increasingly complex programs are still relatively easy to read and understand.

### <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%206%20-%20Dictionaries">Chapter 6 - DICTIONARIES</a>

* learned how to define a dictionary and how to work with the information stored in a dictionary. 
* learned how to access and modify individual elements in a dictionary, and how to loop through all of the information in a dictionary. 
* learned to loop through a dictionary’s key-value pairs, its keys, and its values. 
* learned how to nest multiple dictionaries in a list, nest lists in a dictionary, and nest a dictionary inside a dictionary.

### <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%207%20-%20User%20Input%20and%20While%20Loop">Chapter 7 - USER INPUT AND WHILE LOOPS</a>

* learned how to use input() to allow users to provide their own information in the programs. 
* learned to work with both text and numerical input and how to use while loops to make programs run as long as users want them to. 
* learned several ways to control the flow of a while loop by setting an active flag, using the break statement, and using the continue statement. 
* learned how to use a while loop to move items from one list to another and how to remove all instances of a value from a list. 
* learned how while loops can be used with dictionaries.

### <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%208%20-%20functions">Chapter 8 - FUNCTIONS</a>

* learned how to write functions and to pass arguments so that your functions have access to the information they need to do their work. 

* learned how to use positional and keyword arguments, and how to accept an arbitrary number of arguments. You saw functions that display output and functions that return values. 

* learned how to use functions with lists, dictionaries, if statements, and while loops. You also saw how to store your functions in separate files called modules, so your program files will be simpler and easier to understand. 

* learned to style your functions so your programs will continue to be well-structured and as easy as possible for you and others to read.

* One of your goals as a programmer should be to write simple code that does what you want it to, and functions help you do this. They allow you to write blocks of code and leave them alone once you know they work. When you know a function does its job correctly, you can trust that it will continue to work and move on to your next coding task.

* Functions allow you to write code once and then reuse that code as many times as you want. When you need to run the code in a function, all you need to do is write a one-line call and the function does its job. When you need to modify a function’s behavior, you only have to modify one block of code, and your change takes effect everywhere you’ve made a call to that function.

* Using functions makes your programs easier to read, and good function names summarize what each part of a program does. Reading a series of function calls gives you a much quicker sense of what a program does than reading a long series of code blocks.

* Functions also make your code easier to test and debug. When the bulk of your program’s work is done by a set of functions, each of which has a specific job, it’s much easier to test and maintain the code you’ve written. You can write a separate program that calls each function and tests whether each function works in all the situations it may encounter. When you do this, you can be confident that your functions will work properly each time you call them.
### <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%209%20-%20CLASSES">Chapter 9 - CLASSES<a/>

* learned how to write your own classes. 
* learned how to store information in a class using attributes 
* how to write methods that give your classes the behavior they need. 
* learned to write __init__() methods that create instances from your classes with exactly the attributes you want. 
* saw how to modify the attributes of an instance directly and through methods. 
* learned that inheritance can simplify the creation of classes that are related to each other
* learned to use instances of one class as attributes in another class to keep each class simple.
* how storing classes in modules and importing classes you need into the files where they’ll be used can keep your projects organized. 
* learned about the Python standard library, and saw an example based on the OrderedDict class from the collections module. 
* learned to style your classes using Python conventions.
