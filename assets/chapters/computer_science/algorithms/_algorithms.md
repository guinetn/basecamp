# Algorithms

download.chapter(computer_science/big-o.md)

- https://www.programmingalgorithms.com

## Sorting Algorithms:

Sorting is typically either O(n²) or O(nlogn)

|Time Complexities of Sorting Algorithms||||
|---|---|---|---|
|Algorithm| Best| Average| Worst |
|Quick Sort| Ω(n log(n))| Θ(n log(n))| O(n^2) |
|Bubble Sort| Ω(n)| Θ(n^2)| O(n^2) |
|Merge Sort| Ω(n log(n))| Θ(n log(n))| O(n log(n)) |
|Insertion Sort| Ω(n)| Θ(n^2)| O(n^2) |
|Selection Sort| Ω(n^2)| Θ(n^2)| O(n^2) |
|Heap Sort| Ω(n log(n))| Θ(n log(n))| O(n log(n)) |
|Radix Sort| Ω(nk)| Θ(nk)| O(nk) |
|Bucket Sort| Ω(n+k)| Θ(n+k)| O(n^2) |

### Quick Sort
Quicksort is generally considered the “fastest” sorting algorithm

### Bubble Sort
 simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. Example: First Pass: ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 )

### Merge Sort

### Insertion Sort

### Selection Sort

### Heap Sort

### Radix Sort

### Bucket Sort

## Searching

### Sequential Search
With an ordered container it is possible to visit them in sequence O(n)

|Case	             |Best Case	| Worst Case | Average Case ||
|---|---|---|---|
|item is present	 | 1        |	n	     | n/2 |​ sequential_search/ ordered_sequential_search|
|item is not present | n        |	n	     | n  sequential_search||
|item is not present | n        |	n	     | n/2 | ordered_sequential_search|

```python
def sequential_search(alist, item):
    position = 0

    while position < len(alist):
        if alist[position] == item:
            return True
        position = position + 1

    return False

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

sequential_search(testlist, 3)  # => False
sequential_search(testlist, 13)  # => True 
``` 

if items were in ascending order the algorithm does not have to continue looking through all of the items to report that the item was not found. It can stop immediately. 
```python
def ordered_sequential_search(alist, item):
    position = 0

    while position < len(alist):
        if alist[position] == item:
            return True

        # exit if ordered
        if alist[position] > item:
            return False

        position = position + 1

    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
ordered_sequential_search(testlist, 3)  # => False
ordered_sequential_search(testlist, 13)  # => True
``` 

### Binary Search

Divide and conquer strategy in O(logn)

Instead of searching the list in sequence, a binary search will use the ordered nature of the list to eliminate half of the left/right.
* start by examining the middle item
* If is the correct item, we are done
* If it is not and the item searching for is greater than the middle item, we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration. The item, if it is in the list, must be in the upper half. Repeat the process with the upper half. Start at the middle item and compare it against what we are looking for. Again, we either find it or split the list in half, therefore eliminating another large part of our possible search space. 

Each comparison eliminates around half of the remaining items from consideration. 
|Comparisons | ~ Number of Items Left |
|---|---|
|1|n/2|
|2|n/4|
|…||
|i|n/2^i|

The number of comparisons necessary to get to this point is i where n/2^i=1 ==> comparisons number is i=log n
 

```python
def binary_search(alist, item):
    if not alist:  # list is empty -- our base case
        return False

    midpoint = len(alist) // 2
    if alist[midpoint] == item:  # found it!
        return True

    if item < alist[midpoint]:  # item is in the first half, if at all
        return binary_search(alist[:midpoint], item)

    # otherwise item is in the second half, if at all
    return binary_search(alist[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
binary_search(testlist, 3)  # => False
binary_search(testlist, 13)  # => True
```

### Hashing

Previously we make improvements in our search algorithms by taking advantage of information about where items are stored in the collection with respect to one another. Knowing a list was ordered, we could search in logarithmic time using a binary search. 
Hash is a data structure that can be searched in O(1) time

A hash table is a collection of items which are stored in such a way as to make it easy to find them later. Each position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0.

#### Hash function
Maps an item and the slot that item belongs to
Take any item in the collection and return an integer in the range of slot names [0 ; n-1]
remainder method: 
(item/table size)
will typically be present in some form in all hash functions, since the result must be in the range of slot names.
Perfect hash function: maps each item into A UNIQUE slot
 
* load factor: number of slots occupied
λ = ​numberofitems / ​tablesize
​​
#### collision

item        | 77 |   |   |   | 26 | 93 | 17 |   |    | 31 | 54 |
slots       | 0  | 1 | 2 | 3 | 4  | 5  | 6  | 7 | 8  | 9  | 10 |      λ = 6/11
item hash     ↑
              44%11=0. Since 77 also had a hash value of 0, we would have a problem.
              collision: same hash for two different item

given an arbitrary collection of items, there is no systematic way to construct a perfect hash function. Luckily, we do not need the hash function to be perfect to still gain performance efficiency.

One way to always have a perfect hash function is to increase the size of the hash table so that each possible value in the item range can be accommodated. This guarantees that each item will have a unique slot. Although this is practical for small numbers of items, it is not feasible when the number of possible items is large. For example, if the items were nine-digit Social Security numbers, this method would require almost one billion slots. If we only want to store data for a class of 25 students, we will be wasting an enormous amount of memory.

Collision Resolution
When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table. This process is called collision resolution.
open addressing 
linear probing

## Recursion

method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. In computer science, recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.

### The Three Laws of Recursion

A recursive algorithm must
1. Have a base case
2. Change its state and move toward the base case
3. Call itself, recursively


```python

def iterative_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

iterative_sum([1, 3, 5, 7, 9])  # => 25
```

Recursion
```python
def sum_of(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_of(numbers[1:])

sum_of([1, 3, 5, 7, 9])  # => 25
```

Converting a number to any base <=16
```python
CHAR_FOR_INT = '0123456789abcdef'


def to_string(n, base):
    if n < base:
        return CHAR_FOR_INT[n]

    return to_string(n // base, base) + CHAR_FOR_INT[n % base]

to_string(1453, 16)  # => 5Ad
```

- https://bradfieldcs.com/algos/searching/hashing/

::::
download.chapter(computer_science/algorithms/algorithms_basic.md)
