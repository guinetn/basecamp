https://www.programiz.com/python-programming/closure

- nested function 
- nonlocal variable
- value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

Use:
	Avoid the use of global values and provides some form of data hiding. 
	When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more 
	elegant solution. But when the number of attributes and methods get larger, it's better to implement a class.


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # Nested functions. Can access variables of the enclosing scope
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")     # returned function was bound to the name another.  
another()                        # On calling another(), the message was still remembered although we had already finished executing the print_msg() function. This technique is called "closure"


non-local variables are read-only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them.