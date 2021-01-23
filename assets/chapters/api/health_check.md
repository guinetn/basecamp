### HEALTH CHECK

As part of .NET Core SDK, Microsoft has delivered an amazing healthcheck runtime.
Setup in your Startup class, your app will host a set of health check endpoints that you can query to assert its health.
- https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-3.1

```c#
using System.Threading;
using System.Threading.Tasks;

namespace Microsoft.Extensions.Diagnostics.HealthChecks
{
    /// <summary>
    /// Represents a health check, which can be used to check the status of a component in the application, such as a backend service, database or some internal
    /// state.
    /// </summary>
    public interface IHealthCheck
    {
        /// <summary>
        /// Runs the health check, returning the status of the component being checked.
        /// </summary>
        /// <param name="context">A context object associated with the current execution.</param>
        /// <param name="cancellationToken">A <see cref="CancellationToken"/> that can be used to cancel the health check.</param>
        /// <returns>A <see cref="Task{HealthCheckResult}"/> that completes when the health check has finished, yielding the status of the component being checked.</returns>
        Task<HealthCheckResult> CheckHealthAsync(HealthCheckContext context, CancellationToken cancellationToken = default);
    }
}

```