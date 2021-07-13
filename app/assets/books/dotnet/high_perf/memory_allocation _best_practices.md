# MEMORY ALLOCATION BEST PRACTISES

- Use IDisposable/using keyword to free unmanaged resources.
- Deferred members Initialization that are not required during the creation of the class object.
- Specify collections size if possible (List<T> sets the initial size to 4 elements, adding any part after 4, the collection size is doubled in memory)
- Use simple and well structured data model. Complexity = Garbage Collector whole graph analyzing time to check which objects can be collected.
- use yield statements to generate iterator pattern, which is an IEnumerator implementation,so the whole collection does not need to be in memory. It processes one item at a time.
- Avoid excessive grouping or aggregate functions in LINQ queries.

