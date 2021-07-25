## IAsyncEnumerable<T>

C# 8.0
Asynchronous version of IEnumerable<T>
Lets you await foreach over these to consume their elements and yield return to them to produce elements.   
See ASYNC STREAMS = ASYNC ENUMERABLE

```cs
async IAsyncEnumerable<int> GetBigResultsAsync()
{
    await foreach (var result in GetResultsAsync())
    {
        if (result > 20) yield return result; 
    }
}
```

```cs
using (var session = documentStore.OpenAsyncSession())
{
    await foreach (var entry in GetDocumentsFromDatabase2(session))
    {
        Console.WriteLine($"Processing entry '{entry.Id}'");
    }
}

static async IAsyncEnumerable<Order> GetDocumentsFromDatabase2(IAsyncDocumentSession session)
{
    var skip = 0;
    do
    {
        var entries = await session.Query<Order>().OrderByDescending(x => x.Id).Skip(skip).Take(100).ToListAsync();
        foreach (var entry in entries)
            yield return entry;
        skip += 100;
        if (entries.Count < 100)
            break;
    } while (true);
}
```
    