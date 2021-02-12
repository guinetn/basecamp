## ValueTask

System.Threading.Tasks

ValueTask
ValueTask<TResult> 

To improve asynchronous performance in common use cases where decreased allocation overhead is important.

a struct capable of wrapping either a TResult or a Task<TResult>. This means it can be returned from an async method, and if that method completes synchronously and successfully, nothing need be allocated: we can simply initialize this ValueTask<TResult> struct with the TResult and return that. Only if the method completes asynchronously does a Task<TResult> need to be allocated, with the ValueTask<TResult> created to wrap that instance (to minimize the size of ValueTask<TResult> and to optimize for the success path, an async method that faults with an unhandled exception will also allocate a Task<TResult>, so that the ValueTask<TResult> can simply wrap that Task<TResult> rather than always having to carry around an additional field to store an Exception).

```cs
public override ValueTask<int> ReadAsync(byte[] buffer, int offset, int count)
{
    try
    {
        int bytesRead = Read(buffer, offset, count);
        return new ValueTask<int>(bytesRead);
    }
    catch (Exception e)
    {
        return new ValueTask<int>(Task.FromException<int>(e));
    }
}
```

https://devblogs.microsoft.com/dotnet/understanding-the-whys-whats-and-whens-of-valuetask/
