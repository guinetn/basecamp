## Tasks

System.Threading.Tasks

### TPL - Task Parallel Library

### Task

Task
Task<TResult>
[System.Threading.Tasks.Task] | Get-Member
[System.Threading.Tasks.Task] | Get-Member -static

```cs
public class Task : IAsyncResult, IDisposable
```


“promise”: object that represents the eventual completion of some operation
You initiate an operation and get back a Task for it, and that Task will complete when the operation completes, which may happen synchronously as part of initiating the operation (e.g. accessing some data that was already buffered), asynchronously but complete by the time you get back the Task (e.g. accessing some data that wasn’t yet buffered but that was very fast to access), or asynchronously and complete after you’re already holding the Task (e.g. accessing some data from across a network). Since operations might complete asynchronously, you either need to block waiting for the results (which often defeats the purpose of the operation having been asynchronous to begin with) or you need to supply a callback that’ll be invoked when the operation completes. In .NET 4, providing such a callback was achieved via ContinueWith methods on the Task, which explicitly exposed the callback model by accepting a delegate to invoke when the Task completed:


async-await from C#5: To simplify using the TPL

## More
- https://devblogs.microsoft.com/dotnet/understanding-the-whys-whats-and-whens-of-valuetask/
- https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.task?view=net-5.0