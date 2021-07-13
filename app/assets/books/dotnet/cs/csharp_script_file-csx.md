# .csx

Roslyn made C# scripts possible. There's a Jan 2016 MSDN blogpost by Mark Michaelis titled C# Scripting if you're interested.

C# Script File introduced with Roslyn (open-source .NET Compiler Platform: compilers and code analysis APIs for C# and Visual Basic .NET). You don't have to have everything in a class and method, a csx file is like it's own method, and everything in the file will be executed on start. It also supports some additional directives (like #load to load another script).

https://galdin.dev/blog/csharp-scripts-using-dotnet-script/
https://github.com/dotnet/roslyn/blob/master/docs/wiki/Scripting-API-Samples.md

* https://github.com/glennblock/scriptcs
script file used by ScriptCS to allow you to create executables without having to create a project file.

* dotnet-script
- https://galdin.dev/blog/csharp-scripts-using-dotnet-script/
- https://github.com/filipw/dotnet-script
dotnet-script, which is a cross-platform .NET Core global tool with full intellisense support on VS Code via omnisharp and covers most use-cases for your experimenting needs.


- http://scriptcs.net/
- https://github.com/scriptcs/scriptcs

* REPL
C:\> scriptcs
scriptcs (ctrl-c or blank to exit)

> var message = "Hello, world!";
> Console.WriteLine(message);
Hello, world!
> 

C:\>

*
app.csx
using Raven.Client;
using Raven.Client.Embedded;
using Raven.Client.Indexes;

Console.WriteLine("Starting RavenDB server...");

EmbeddableDocumentStore documentStore = null;
try
{
    documentStore = new EmbeddableDocumentStore { UseEmbeddedHttpServer = true };
    documentStore.Initialize();

    var url = string.Format("http://localhost:{0}", documentStore.Configuration.Port);
    Console.WriteLine("RavenDB started, listening on {0}.", url);

    Console.ReadKey();
}
finally
{
    if (documentStore != null)
        documentStore.Dispose();
}

Install the RavenDB.Embedded package from NuGet using the install command.
scriptcs -install RavenDB.Embedded

> scriptcs app.csx
INFO : Starting to create execution components
INFO : Starting execution
Starting RavenDB server...
.. snip ..
RavenDB started, listening on http://localhost:8080.