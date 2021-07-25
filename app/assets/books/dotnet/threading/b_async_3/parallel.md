## PARALLEL

Be parallel with 
- Parallel.xxx
- Task.WhenAll(tasks..)

Parallel.For(0, 1_000_000, i => { ar[i] = i; })
Parallel.For(0, 1_000_000, new ParallelOptions { MaxDegreeOfPArallelism = 10 /* -1: cpu core auto detection*/} ,i => { ar[i] = i; })
Parallel.ForEach(...)
Parallel.Invoke(...)


1. Parallel does not mean faster

[benchmark]  // 1.005 ms
public int[] NormalLoop() {
    var arr = new int[1_000_000]
    for(var i=0; i<1_000_000; i++) 
        ar[i] = i;
    return ar;
}

[benchmark] // 1.364 ms...depends on cpu, how many threads, overhead due to the aggregation of the segmented buckets created
public int[] ParallelLoop() {
    var arr = new int[1_000_000]
    Parallel.For(0, 1_000_000, i => { ar[i] = i; });
    return ar;
}
    


Foreach doesn't support async/await


## Sample

1. Async Foreach: breaks the data source into partitions allowing for specifying the degree of parallelism and accepts a lambda to execute for each item

```c#
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
namespace Extensions
{
    public static class Extensions
    {
        public static Task ForEachAsync<T>(this IEnumerable<T> source, int dop, Func<T, Task> body)
        {
            return Task.WhenAll(
                from partition in Partitioner.Create(source).GetPartitions(dop)
                select Task.Run(async delegate
                {
                    using (partition)
                        while (partition.MoveNext())
                            await body(partition.Current);
                }));
        }
    }
}

public static IEnumerable<Entry> GetDocumentsFromDatabase(IDocumentSession session)
{
    var skip = 0;
    do
    {
        var entries = session.Query<Entry>().Where(x => !x.Deleted).OrderByDescending(x => x.DateModified).Skip(skip).Take(1024).ToList();
        foreach (var entry in entries)
            yield return entry;
        skip += 1024;
        if (entries.Count < 1024)
            break;
    } while (true);
}

// fetching 20 pages from the database in parallel, then iterating over the results from each. Pausing execution of the thread on each result and yielding that item to the async lambda we have going on in the other thread
await GetDocumentsFromDatabase(session).ForEachAsync(dop: 20, body: async entry =>
{
    _logger.Info($"Processing entry '{entry.Id}'");
});
```

2. Modernizing Async Foreach

```cs
public static Task ParallelForEachAsync<T>(this IEnumerable<T> source, int dop, Func<T, Task> body)
{
    async Task AwaitPartition(IEnumerator<T> partition)
    {
        using (partition)
        {
            while (partition.MoveNext())
            { await body(partition.Current); }
        }
    }
    return Task.WhenAll(
        Partitioner
            .Create(source)
            .GetPartitions(dop)
            .AsParallel()
            .Select(p => AwaitPartition(p)));
}
```

3. Using IAsyncEnumerable

```cs
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

using (var session = documentStore.OpenAsyncSession())
{
    await foreach (var entry in GetDocumentsFromDatabase2(session))
    {
        Console.WriteLine($"Processing entry '{entry.Id}'");
    }
}
```

but a a bit faster with TaskScheduler + ActionBlock:

```cs
public static Task AsyncParallelForEach<T>(this IEnumerable<T> source, Func<T, Task> body, 
int maxDegreeOfParallelism = DataflowBlockOptions.Unbounded, TaskScheduler scheduler = null)
{
    var options = new ExecutionDataflowBlockOptions
    {
        MaxDegreeOfParallelism = maxDegreeOfParallelism
    };
    if (scheduler != null)
        options.TaskScheduler = scheduler;

    var block = new ActionBlock<T>(body, options);

    foreach (var item in source)
        block.Post(item);

    block.Complete();
    return block.Completion;
}

using (var session = documentStore.OpenSession())
{
    session.Advanced.MaxNumberOfRequestsPerSession = int.MaxValue;

    SynchronizationContext.SetSynchronizationContext(new SynchronizationContext());

    await GetDocumentsFromDatabase(session).AsyncParallelForEach(async entry => { 
            Console.WriteLine($"Processing entry '{entry.Id}'");
        }, 20, TaskScheduler.FromCurrentSynchronizationContext()
    );
}
```

4. Using C# 8.0 async streams to optimizing parallel async Foreach: add async/await

```cs
public static async Task AsyncParallelForEach<T>(this IAsyncEnumerable<T> source, Func<T, Task> body, 
int maxDegreeOfParallelism = DataflowBlockOptions.Unbounded, TaskScheduler scheduler = null)
{
    var options = new ExecutionDataflowBlockOptions
    {
        MaxDegreeOfParallelism = maxDegreeOfParallelism
    };
    if (scheduler != null)
        options.TaskScheduler = scheduler;

    var block = new ActionBlock<T>(body, options);

    await foreach (var item in source)
        block.Post(item);

    block.Complete();
    await block.Completion;
}
```

- https://medium.com/@alex.puiu/parallel-foreach-async-in-c-36756f8ebe62
- https://www.youtube.com/watch?v=lHuyl_WTpME&t=514s