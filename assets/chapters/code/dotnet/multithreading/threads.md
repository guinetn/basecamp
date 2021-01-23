# Threads

Trading ways
- Thread: Long running tasks
ThreadStart delegates starts your own threads
- ThreadPool: Briefs jobs
* directly: ThreadPool.QueueUserWorkItem
* indirectly: asynchronous methods (xxx.BeginYYYY, BeginInvoke on a delegate)

## Thread.Sleep
Makes the current thread sleep 

## THREADS

Long running tasks

```c#
using System;
using System.Threading;

public class Test
{
    static void Main()
    {
        ThreadStart job = new ThreadStart(ThreadJob);
        Thread thread = new Thread(job);
        thread.Start();
        // short: new Thread(new ThreadStart(ThreadJob)).Start();
        
        ParameterizedThreadStart
        Thread paramThread = new Thread(new ParameterizedThreadStart(makeDouble));
        paramThread.Start(100);
 
        for (int i=0; i < 5; i++)
        {
            Console.WriteLine ("Main thread: {0}", i);
            Thread.Sleep(1000);
        }
    }
    
    static void ThreadJob()
    {
        for (int i=0; i < 10; i++)
        {
            Console.WriteLine ("Other thread: {0}", i);
            Thread.Sleep(500);
        }
    }
    static int makeDouble(int value) {         
        Console.WriteLine ("makeDouble: {0}", value *2);            
    }
}
```

```C#
using System;
using System.Threading;

public class Test
{
    static void Main()
    {
        Counter classInstance = new Counter();
        ThreadStart job = new ThreadStart(classInstance.Count);
        Thread thread = new Thread(job);
        thread.Start();
        
        for (int i=0; i < 5; i++)
        {
            Console.WriteLine ("Main thread: {0}", i);
            Thread.Sleep(1000);
        }
    }
}

public class Counter
{
    public void Count()
    {
        for (int i=0; i < 10; i++)
        {
            Console.WriteLine ("Other thread: {0}", i);
            Thread.Sleep(500);
        }
    }
}

```

## MULTITHREADING ISSUE #1: DATA RACES

```c#
using System;
using System.Threading;

public class Test
{
    static int count=0;
    
    static void Main()
    {
        ThreadStart job = new ThreadStart(ThreadJob);
        Thread thread = new Thread(job);
        thread.Start();
        
        for (int i=0; i < 5; i++)
            count++;        
            /*
            1. Reads the current value of count
            2. Increments that number
            3. Writes the new value back to the count variable
            If one thread gets as far as reading current value, then other thread takes over
            */
        
        thread.Join(); // pauses main thread until the other thread has completed
        Console.WriteLine ("Final count: {0}", count); // isn't guaranteed to be 10
    }
    
    static void ThreadJob()
    {
        for (int i=0; i < 5; i++)        
            count++;        
    }
}    
```

download.chapter(code/dotnet/multithreading/lock_monitor.md)


## MULTITHREADING ISSUE #2: DEADLOCKS

When two threads each hold a monitor that the other one wants. Each blocks, waiting for the monitor that it's waiting for to be released - and so the monitors are never released, and the application hangs 


:::::
download.chapter(code/dotnet/multithreading/signaling_wait_pulse.md)
download.chapter(code/dotnet/multithreading/signaling_resetevent.md)