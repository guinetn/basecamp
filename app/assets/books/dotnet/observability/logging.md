## logging

give you the root cause of the problem
In distributed world ensure log records have in-depth information to debug that can be queried  from a central place. Each log record needs to have a correlation id, so they’re tracked in a single transaction to get the big picture. Generating a correlation ID at the start of a transaction and then logging it in each message related to that transaction makes it easier to search for all related messages from the centralized logging systems.

# LOGGERS

download.page(dotnet/observability/loggers/log4net.md)
download.page(dotnet/observability/loggers/nlog.md)
download.page(dotnet/observability/loggers/serilog.md)

## More


- https://docs.microsoft.com//aspnet/core/fundamentals/logging
- https://blog.elmah.io/monitoring-net-scheduled-tasks-tools-and-alternatives/
- https://michaelscodingspot.com/logging-in-dotnet/
- https://dzone.com/articles/5-good-reasons-to-use-a-log-server

- https://intellitect.com/net-core-dependency-injection/
- https://github.com/IntelliTect-Samples/2016.04.01-EssentialNetLoggingWithNetCore
- https://intellitect.com/implementing-a-custom-ilogger-with-exception-handling-for-net-core/
- https://michaelscodingspot.com/logging-in-dotnet/
- https://www.ezzylearning.net/tutorial/logging-in-asp-net-core-5-using-serilog