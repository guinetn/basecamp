# pipelines

To do high-performance I/O in .NET
- Have high performance parsing streaming data
- Reduce code complexity

https://docs.microsoft.com/en-us/dotnet/standard/io/pipelines

### Pipe
Create a PipeWriter/PipeReader pair
All data written into the PipeWriter is available in the PipeReader:

var pipe = new Pipe();
PipeReader reader = pipe.Reader;
PipeWriter writer = pipe.Writer;