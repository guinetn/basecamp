# Linq

Enumerable.Range(1, 5).Select(i => {})

* Sort a string
var s = "zacb";
var s2 = String.Concat(s.OrderBy(c => c)); // abcz
var s2 = String.Concat(s.OrderBy(c => c).Distinct()); // remove duplicates


var elements = new List<string>() {"water air earth fire", "grass sky thunder air"}; 
var query = elements.SelectMany(f => f.Split(' ')).OrderBy(x => x)
.GroupBy(x =>x).Select((x, i) => new { Element = x, Count = x.Count() }); 
var first = query.First(); 
Console.WriteLine(first.Count); 

var list = new List<string>() {"water", "air"};
var r = list.Contains("air");
System.Console.WriteLine("air" + r); // true
var r2 = list.Find(x=> x=="air");
System.Console.WriteLine("air2: " + r2); // true
System.Console.WriteLine(list[1]); // true

string s= "zacbc";
var s2 = String.Concat(s.OrderBy(c => c));
System.Console.WriteLine(s2); // abccz
s2 = String.Concat(s.OrderBy(c => c).Distinct());
System.Console.WriteLine(s2); // abcz			

## [Linq Methods](https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.aggregate?view=net-5.0)

- Aggregate
- All
- Any
- Append
- AsEnumerable
- Average
- Cast
- Concat
- Contains
- Count
- DefaultIfEmpty
- Distinct
- ElementAt
- ElementAtOrDefault
- Empty
- Except
- First
- FirstOrDefault
- GroupBy
- GroupJoin
- Intersect
- Join
- Last
- LastOrDefault
- LongCount
- Max
- Min
- OfType
- OrderBy
- OrderByDescending
- Prepend
- Range
- Repeat
- Reverse
- Select
- SelectMany
- SequenceEqual
- Single
- SingleOrDefault
- Skip
- SkipLast
- SkipWhile
- Sum
- Take
- TakeLast
- TakeWhile
- ThenBy
- ThenByDescending
- ToArray
- ToDictionary
- ToHashSet
- ToList
- ToLookup
- Union
- Where
- Zip

## More

- https://www.linqpad.net/
- https://www.ezzylearning.net/tutorial/introduction-to-language-integrated-query-linq
- https://intellitect.com/notes-on-some-c-3-0-features-that-make-linq-possible/