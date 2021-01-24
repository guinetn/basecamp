# BASIC ALGORITHMS

## Fibonacci

Sum of the two preceding numbers

F[n] = F[n-1] + F[n-2] 
F(0)=0  F(1)=1

    n 		0 	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17
    F[n] 	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	987	1597
        
int Fibonacci(int num) { return num < 2 ? num : Fibonacci(num - 1) + Fibonacci(num - 2); }
     
function fib(n) { return n<2 ? n : fib(n-2) + fib(n-1); }
                
```python
#Naive Fibonacci sequence
def F(n):
	if n<2:
		return n
	else:
		return F(n-1)+F(n-2)
```
    F(4) calculation is
          4     
      ┌───┴───┐
      3       2      F(2) is computed twice!
    ┌─┴─┐   ┌─┴─┐
    1   2   0   1  
      ┌─┴─┐
      1   0   

To improve the algorithm, instead of calculating F(2) twice, we store the solution somewhere to only calculate it once:

```python
# Fibonacci sequence with memoization (synamic programming)
def fibonacciVal(n):
	memo[0], memo[1] = 0, 1
	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]
```

Using dynamic programming we sacrifice recursive solution elegance and readability but gain a much better O(n) running time and O(1) space cost. Starting with 0 and 1
```python
const fib = (n) => {
  let a = 0
  let b = 1
  for (let i = 0; i < n; i++) {
    let temp = a
    a = a + b
    b = temp
  }
  return a
}
```


https://bradfieldcs.com/algos/recursion/dynamic-programming/
                
## Fizz-Buzz

A test of programming ability
Write a program that prints the numbers from 1 to 100, but
* for multiples of three print "Fizz" instead of the number 
* for the multiples of five print "Buzz"
* for numbers which are multiples of both three and five print "FizzBuzz"

why is hard ?
The structure of the if statements is tricky, there are two tests for the same condition 

for(int x = 1; x <= 100; x++) {
	string output = "";
	if(x%3 == 0) output += "Fizz";
	if(x%5 == 0) output += "Buzz";
	if(output == "") output = x.ToString();
	Console.WriteLine(output);
}

## Memoization

An optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again

caching technique for function call
Making long recursive/iterative functions run much faster.
Memoization is another good use case for curry function.

Dynamic Programming store the solution to a problem so we do not need to recalculate it. Memoisation is the act of storing a solution.

```js
//We can beef up our module by adding functions later
var Memoizer = (function(){
    //Private data
    var cache = {};
    //named functions are awesome!
    function cacher(func){
        return function(){
        var key = JSON.stringify(arguments);
        if(cache[key]){
            return cache[key];
        }
        else{
            val = func.apply(this, arguments);
            cache[key] = val;
            return val;
        }
    }
    }    
    //Public data
    return{
        memo: function(func){
        return cacher(func);
        }
    }
})()


var fib = Memoizer.memo(function(n){
    if (n < 2){
        return 1;
    }else{
        return fib(n-2) + fib(n-1);
    }
});

fib(10); ...........
fib(10); 89   // Doesn't have to recalculate anything
fib(7);  21   // Doesn't have to recalculate anything
fib(11); ...loading... 144  // already cached fib(1-10) so faster
```

* Fibonacci sequence

```python
def F(n):
	if n == 0 or n == 1:
		return n
	else:
		return F(n-1)+F(n-2)
```

```python
# Fibonacci sequence with memoization
def fibonacciVal(n):
	memo[0], memo[1] = 0, 1
	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]
```


## Matrix

matA x matB
matrix multiplication requirements: A no of columns = B no of rows

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]

if len(A[0])==len(B):
    print("\npossible")
else:
    print("\nNot possible")
    print("\for matrix multiplication to be possible no of columns in matrix 1 = no of rows in matrix 2")
    
print("\nEnter The Values in the matrix 1: ")

#"# iterate through A rows
for i in range(len(A)):
    # iterate through B columns
    for j in range(len(B[0])):
        # iterate through rows of 
        for k in range(len(B[0])):
            result[i][j] += A[i][k] * B[k][j]   xy = x k k y
for r in result:
    print(r)

          A        B    =      C
	1 2 3    1 2 3     30  36  42
	4 5 6    4 5 6     66  81  96
	7 8 9    7 8 9     102 126 150
    
## PALINDROME
	a word, phrase, number, or other sequence of characters which reads the same backward or forward
	"A man, a plan, a canal, Panama"
	Axa, radar, toot, madam
    
    use a deque: remove both last/first of them directly, we can compare them and continue only if they match. If we can keep matching first and the last items, we will eventually either run out of characters or be left with a deque of size 1 depending on whether the length of the original string was even or odd. In either case, the string must be a palindrome.

	IsPalindrome Recursive public static bool IsPalindrome(string text)
	{
		if (text.Length <= 1)
			return true;
		else
		{
			if ( text[0] != text[ text.Length - 1 ] )
				return false;
			else
				return IsPalindrome( text.Substring( 1, text.Length-2 ) );
		} 
	}
    
    from collections import deque

    def is_palindrome(characters):
        character_deque = deque(characters)

        while len(character_deque) > 1:
            first = character_deque.popleft()
            last = character_deque.pop()
            if first != last:
                return False

        return True


    is_palindrome('lsdkjfskf')   # => False
    is_palindrome('radar')   # => True
    
    https://bradfieldcs.com/algos/deques/palindrome-checker/

## ANAGRAMS (PERMUTATIONS)

O(n)    Sort and Compare
        Count and Compare
O(n²)   Checking Off
n!      All possibilities 
n=20 → 2,432,902,008,176,640,000
function anagramCheckingOff (string1, string2) {
  if (string1.length !== string2.length) return false

  const string2ToCheckOff = string2.split('')

  for (let i = 0; i < string1.length; i++) {
    let letterFound = false
    for (let j = 0; j < string2ToCheckOff.length; j++) {
      if (string1[i] === string2ToCheckOff[j]) {
        string2ToCheckOff[j] = null
        letterFound = true
        break
      }
    }
    if (!letterFound) return false
  }

  return true
}

assert.equal(true, anagramCheckingOff('abcd', 'dcba'))
assert.equal(false, anagramCheckingOff('abcd', 'abcc'))
    
- https://bradfieldcs.com/algos/analysis/an-anagram-detection-example/
    
## TOWERS OF HANOI

French mathematician Edouard Lucas in 1883
https://bradfieldcs.com/algos/recursion/tower-of-hanoi/

download.code(assets/chapters/computer_science/assets/hanoi.cpp)

## SHORTEST PATHS

https://bradfieldcs.com/algos/recursion/dynamic-programming/
