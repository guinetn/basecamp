# MEMORY ALLOCATION BEST PRACTISES

- Use IDisposable/using keyword to free unmanaged resources.

- Deferred members Initialization that are not required during the creation of the class object.


- Specify collections size if possible (List<T> sets the initial size to 4 elements, adding any part after 4, the collection size is doubled in memory)

- Use simple and well structured data model. Complexity = Garbage Collector whole graph analyzing time to check which objects can be collected.

- use yield statements to generate iterator pattern, which is an IEnumerator implementation,so the whole collection does not need to be in memory. It processes one item at a time.
public IEnumerable<int> GetValuesGreaterThan100(List<int> masterCollection)
{
foreach (var value in masterCollection)
{
if (value > 100)
yield return value;
}
}

- Avoid excessive grouping or aggregate functions in LINQ queries.

- Report that the method is obsolete
[Obsolete("This method will be obsolete soon. To replace it you can use the XYZ method.")]
public void MyComponentLegacyMethod()
{
// Here the implementation
}

if you want it to no longer be usable in any way, add 'True' parameter 

[Obsolete("This method will be obsolete soon. To replace it you can use the XYZ method.", true)]
public void MyComponentLegacyMethod()
{
// Here the implementation
}

