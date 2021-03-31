"""Lambda Expressions

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Small anonymous functions can be created with the lambda keyword. Lambda functions can be used
wherever function objects are required. They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function definition. Like nested function
definitions, lambda functions can reference variables from the containing scope.
"""




# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2
print(getSum(10, 3))

s=lambda a,b:a+b
print(s(2,4))



x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

# lambda power is when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)))








def test_lambda_expressions():
    """Lambda Expressions"""

    # This function returns the sum of its two arguments: lambda a, b: a+b
    # Like nested function definitions, lambda functions can reference variables from the
    # containing scope.

    def make_increment_function(delta):
        """This example uses a lambda expression to return a function"""
        return lambda number: number + delta

    increment_function = make_increment_function(42)

    assert increment_function(0) == 42
    assert increment_function(1) == 43
    assert increment_function(2) == 44

    # Another use of lambda is to pass a small function as an argument.
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # Sort pairs by text key.
    pairs.sort(key=lambda pair: pair[1])

    assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
