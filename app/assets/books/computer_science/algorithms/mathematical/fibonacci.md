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


- https://bradfieldcs.com/algos/recursion/dynamic-programming/
- https://www.cantorsparadise.com/how-fibonacci-can-help-us-convert-between-miles-and-kilometers-6b5344782bbb

0,1,1, 2, 3, 5, 8, 13, 21, 34, 55,…      
multiplying a Fibonacci number by φ, is roughly the same thing as finding the next Fibonacci numbers.      
F(n+1) = F(n) * phi
to convert 5 miles to kilometers, we would find the next Fibonacci number, which is 8, so our approximation is that 5 miles = 8 kilometers. In reality, 5 miles is 8.04672 km.
to convert 10 miles to kilometers. 10 isn’t a Fibonacci number, so we have to rewrite 10 as the sum of Fibonacci numbers (8+2). Then, we get (8+2) mi = (13+3) km = 16km. If we used the actual conversion factor, we get 10 mi = 16.0934 km.