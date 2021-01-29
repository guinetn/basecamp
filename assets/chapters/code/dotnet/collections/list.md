# List


List<string> myCollection = new List<string>() { "Bob", "Alex", "Joe" } ;

```c#
using System;
using System.Collections.Generic;

public class Part : IEquatable<Part> , IComparable<Part>
{
    public string PartName { get; set; }
    public int PartId { get; set; }

    public override string ToString() => "ID: " + PartId + "   Name: " + PartName;
    
    public override bool Equals(object obj)
    {
        if (obj == null) return false;
        Part objAsPart = obj as Part;
        if (objAsPart == null) return false;
        else return Equals(objAsPart);
    }
    public int SortByNameAscending(string name1, string name2)
    {
        return name1.CompareTo(name2);
    }

    // Default comparer for Part type.
    public int CompareTo(Part comparePart)
    {
        if (comparePart == null)
            return 1; // A null value means that this object is greater.
        else
            return this.PartId.CompareTo(comparePart.PartId);
    }
    public override int GetHashCode()
    {
        return PartId;
    }
    public bool Equals(Part other)
    {
        if (other == null) return false;
        return (this.PartId.Equals(other.PartId));
    }
    // Should also override == and != operators.
}

// sort by part number
// sort by part name
public class Example
{
    public static void Main()
    {        
        List<Part> parts = new List<Part>();
        parts.Add(new Part() { PartName = "regular seat", PartId = 1434 });
        parts.Add(new Part() { PartName= "crank arm", PartId = 1234 });
        parts.Add(new Part() { PartName = "shift lever", PartId = 1634 }); ;        
        parts.Add(new Part() { PartId = 1334 });  // Name intentionally left null.
        parts.Add(new Part() { PartName = "banana seat", PartId = 1444 });
        parts.Add(new Part() { PartName = "cassette", PartId = 1534 });
        
        Console.WriteLine("\nBefore sort:");
        foreach (Part aPart in parts)        
            Console.WriteLine(aPart); // call the overridden Part.ToString()
        
        // Sort the list: default comparer which is the implemented Part.Compare() 
        parts.Sort();

        Console.WriteLine("\nAfter sort by part number:");
        foreach (Part aPart in parts)        
            Console.WriteLine(aPart);        

        // Call the Sort(Comparison(T) overload using an anonymous method for the Comparison delegate.
        // This method treats null as the lesser of two values.
        parts.Sort(delegate(Part x, Part y)
        {
            if (x.PartName == null && y.PartName == null) return 0;
            else if (x.PartName == null) return -1;
            else if (y.PartName == null) return 1;
            else return x.PartName.CompareTo(y.PartName);
        });

        Console.WriteLine("\nAfter sort by name:");
        foreach (Part aPart in parts)        
            Console.WriteLine(aPart);      
    }
}
```

### Cloning a list

***Elements are value types***
List<YourType> newList = new List<YourType>(oldList);

***Elements are reference types***: need a deep copy

* If implements ICloneable: 
List<ICloneable> oldList = new List<ICloneable>();
List<ICloneable> newList = new List<ICloneable>(oldList.Count);
oldList.ForEach((item) => { newList.Add((ICloneable)item.Clone()); });
    
* If doesn't implements ICloneable: copy-constructor    
List<YourType> oldList = new List<YourType>();
List<YourType> newList = new List<YourType>(oldList.Count);
oldList.ForEach((item)=> { newList.Add(new YourType(item)); });

ICloneable never stated whether the clone was deep or shallow, so you cannot determine which type of Clone operation will be done when an object implements it. This means that if you want to do a deep clone of List<T>, you will have to do it without ICloneable to be sure it is a deep copy
YourType.CopyFrom(YourType itemToCopy) that returns a new instance of YourType.

newList.AddRange(oldList.Select(i => i.Clone()) 
newList.AddRange(oldList.Select(i => new YourType(i))

* Shallow copy

var x = new List<int>() { 3, 4 };
var y = x.ToList();
x.Add(5)
x

var shallowClonedList = new List<MyObject>(originalList);

List<int> oldList = new List<int>( ) {1,2,3,4,5};
List<int> newList = oldList.GetRange(0, oldList.Count);
        
public static List<T> Clone<T>(this List<T> oldList)
{
    var newList = new List<T>(oldList.Capacity);
    newList.AddRange(oldList);
    return newList;
}
        
### Ordering a List<string>
myList = List.OrderBy(c => c).ToList();

List<string> typeCheck = myList as List<string>;
if (typeCheck != null)
    typeCheck.Sort();
else
{
    //... some other sort solution
}

if (typeof(List<string>).IsAssignableFrom(myList.GetType()))
    ((List<string>)myList).Sort();
else
{
    //... some other sort solution
}