## ASYNC AWAIT

C# 5.0
To simplify using the TPL (Task Parallel Library)
To deal with results that are not necessarily ready when you ask for them. They can be asynchronously awaited, and the thread can go do other stuff until they become available. 

Lets you consume (and produce) asynchronous results in straightforward code, without callbacks:

```cs
using System.Threading.Tasks;
await Task.Delay(1000);  // asynchronous delay = simulate some asynchronous work
```

```cs
async Task<int> GetBigResultAsync()
{
    var result = await GetResultAsync();
    if (result > 20) return result; 
    else return -1;
}
```

It is not so helpful if you want to consume (or produce) continuous streams of results, such as you might get from an IoT device or a cloud service. Async/await works only for single values, not sequences that are gradually and asynchronously produced over time, such as for instance measurements from an IoT sensor or streaming data from a service.
Async streams are there for that.

