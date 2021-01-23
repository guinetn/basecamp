# ThreadPool

Briefs jobs

```c#
WaitCallback callback = delegate (object state) { Fetch ((string)state); };
ThreadPool.QueueUserWorkItem (callback, myUrl);

```