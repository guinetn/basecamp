## Serilog

More structured logging variables and objects. More modern than log4net.
Permet d’avoir des méta données sur les événements survenus. Cela permet d’exploiter plus facilement ces logs que des logs en texte brut.

- https://github.com/serilog/serilog-aspnetcore
- https://github.com/saleem-mirza/serilog-sinks-azure-analytics
- https://levelup.gitconnected.com/structured-logging-and-azure-log-analytics-416feda20970


### Log levels
- Verbose           _logger.LogTrace("This is trace");
- Debug             _logger.LogDebug("This is debug");
- Information       _logger.LogInformation("This is informational");
- Warning           _logger.LogWarning("This is warning");
- Error             _logger.LogError("This is error");
- Fatal             _logger.LogCritical("This is critical");

Captured in LogLevel_s column in Log Analytics
_logger.LogInformation("Get operation started {Guid}", Guid.NewGuid());   LogProperties_Guid_g column in Log Analytics

### Scopes
To add additional information to your logs without including them in the log message

```c#
using (_logger.BeginScope(new Dictionary<string, object> {
    ["CustomerNumber"] = "123456",
    ["Status"] = "Locked",
    ["Reason"] = "IdentityValidationFailed"
    }))
{
    _logger.LogInformation(new EventId(10, "AccountStateChanged"), "Customer account locked");
}


using (_logger.BeginScope("{CustomerNumber}", 456789))
using (_logger.BeginScope("{Status}", "PasswordReset"))
using (_logger.BeginScope("{Reason}", "RequestedByUser"))
{
    _logger.LogInformation(new EventId(10, "AccountStateChanged"), "Account Reset");
}
```

### Web request capture

```c#
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
        app.UseSwagger();
        app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "LoggerExample v1"));
    }
    app.UseSerilogRequestLogging();
    app.UseRouting();
...
```

### enricher property 
every log entry in Log Analytics will have that property as a column

```c#
Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Debug()
    .MinimumLevel.Override("Microsoft", LogEventLevel.Error)
    .Enrich.FromLogContext()
    .Enrich.WithProperty("Version", "1.0.0")
    .WriteTo.AzureAnalytics(workspaceId, primaryKey, "example4")
    .WriteTo.Console()
    .CreateLogger();
CreateHostBuilder(args).Build().Run();
```



```c#
using System;
using System.IO;

using log4net;
using log4net.Core;
[assembly: log4net.Config.XmlConfigurator( ConfigFile = "Log4Net.config", Watch = true )]

namespace Hello
{
	private static readonly log4net.ILog log = log4net.LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

        /// <summary>
        ///   The main entry point for the application
        /// </summary>
        [STAThread]
        public static void Main(string[] args)
        {
            log.Info("Application [ConsoleApp] Start");

            Console.WriteLine(…);
            Console.WriteLine(…);

 			log.Info("Application [ConsoleApp] End");
        }
    }
}
```

log4net.dll

log4net.xml

***Log4Net.config***
```xml
<?xml version="1.0" encoding="utf-8" ?>
<log4net>
    <!-- A1 is set to be a ConsoleAppender -->
    <appender name="ConsoleAppender" type="log4net.Appender.ConsoleAppender">

        <!-- A1 uses PatternLayout -->
        <layout type="log4net.Layout.PatternLayout">
            <conversionPattern value="%-4timestamp [%thread] %-5level %logger %ndc - %message%newline" />
        </layout>
    </appender>

    <root>
        <appender-ref ref="ConsoleAppender" />
    </root>
</log4net>
```




>Install-Package Serilog.AspNetCore
>Install-Package Serilog.Sinks.AzureAnalytics

Program.cs
```c#
public class Program
{
    public static void Main(string[] args)
    {
        var workspaceId = "[your workspace id]";
        var primaryKey = "[your primary key]";
        Log.Logger = new LoggerConfiguration()
            .MinimumLevel.Information()
            .MinimumLevel.Override("Microsoft", LogEventLevel.Error)
            .Enrich.FromLogContext()
            .WriteTo.AzureAnalytics(workspaceId, primaryKey, "myapp")
            .WriteTo.Console()
            .CreateLogger();
        CreateHostBuilder(args).Build().Run();
    }
public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .UseSerilog()
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.UseStartup<Startup>();
            });
}
```