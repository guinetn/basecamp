## NLog

NLog has quickly become the second most popular framework for .NET logging. They had support for .NET Core when v1.0 came out and continue to rapidly add new features. NLog even works across Xamarin, Mono, and other runtimes. NLog is a safe bet if you are thinking about selecting a new logging framework for ASP.NET Core.
Be sure to check out our tips and best practices guide on NLog. https://stackify.com/nlog-guide-dotnet-logging/


Logging frameworks: NLog, Serilog, Microsoft.Extensions.Logging. 
It is often a better choice for monitoring the output from these logging frameworks, rather than monitoring the Windows Event Log.
how to send an email on errors logged through NLog

```c#
class Program
{
    static void Main(string[] args)
    {
        var logger = NLog.LogManager.GetCurrentClassLogger();
        try
        {
            // Execute your scheduled task code
            logger.Info("Scheduled task is successful");
        }
        catch (Exception e)
        {
            logger.Error(e, "Error during scheduled task");
        }
        
        NLog.LogManager.Shutdown();
    }
}

NLog.config file:
<target name="Mail" xsi:type="Mail" smtpServer="smpt.myserver.com" smtpPort="587" ... />
```

