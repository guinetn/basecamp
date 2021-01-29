## String algorithms


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
    