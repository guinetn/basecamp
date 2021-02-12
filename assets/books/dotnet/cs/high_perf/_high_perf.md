# HIGH PERFORMANCE C# 

Lots of effort goes into reducing allocation, not because the act of allocating is itself particularly expensive, but because of the follow-on costs in cleaning up after those allocations via the garbage collector (GC). No matter how much work goes into reducing allocations, however, the vast majority of workloads will incur them, and thus it’s important to continually push the boundaries of what the GC is able to accomplish, and how quickly.

download.page(dotnet/cs/high_perf/benchmarking.md)

download.page(dotnet/cs/high_perf/frugal_object.md)
download.page(dotnet/cs/high_perf/pooling.md)
download.page(dotnet/cs/high_perf/zero_copy.md)
download.page(dotnet/cs/high_perf/struct_of_arrays.md)
download.page(dotnet/cs/high_perf/stack_based_data.md)
download.page(dotnet/cs/high_perf/buffered_builder.md)

download.page(dotnet/cs/high_perf/io.pipelines.md)

- https://adamsitnik.com/
- https://adamsitnik.com/Array-Pool/
- https://www.youtube.com/watch?v=3r6gbZFRDHs&t=2255s
- Slides: https://prodotnetmemory.com/slides/PerformancePatterns/#1
- https://prodotnetmemory.com


	



