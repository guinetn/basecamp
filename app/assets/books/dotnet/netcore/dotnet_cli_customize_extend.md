## Extending the .NET CLI

### Add your verb to `dotnet` command 

- https://mattwarren.org/2016/10/03/Adding-a-verb-to-the-dotnet-CLI-tooling/
- https://intellitect.com/ildasm-with-net-core/

Any executable found in the PATH named in this way, that is as dotnet-{command}, will be invoked by the dotnet driver.
When you run `dotnet build`, the driver will run the `dotnet-build` executable. 
All of the arguments following the command are passed to the command being invoked. 

1. NuGet Packages on per-project basis
create a portable console application that runs on top of .NET Core.
Your application can then be packaged up (using dotnet pack) and distributed through NuGet. 
To consume, you simply need to make a reference to the tooling in project.json. 
The custom tooling is only available in the context of the project that references/restores the NuGet package.
Your project needs to follow the .NET CLI driver-command nomenclature of dotnet-[command]

To consume, you simply need to add a Tools section in projects’ project.json, like so:

“tools”: {
  “dotnet-domything”: {
    “version”: “1.0.0”,
    “imports”: [“dnxcore50”]
  }
}

Once dotnet restore is run on the project, the NuGet tool and all of its dependencies are resolved. 
You can then happily use the command dotnet-domything, but only in context of your project

2. System Path on per-machine basis
to build custom .NET CLI tooling that can be used across multiple projects, but only on the given machine. The one drawback is portability to another machine requires deploying the tool elsewhere

The dotnet driver can invoke any command that follows the dotnet-[command] convention. The default resolution logic will first probe several locations in the context of the project and finally fall back to the system PATH. If the requested command exists in the system PATH and is a binary that can be invoked, the dotnet driver can invoke it.

The custom binary tool can be pretty much anything that the operating system can execute. On Unix or OSX systems, this means any command script saved as dotnet-domything that has the execute bit set via chmod +x. On Windows, it means anything that Windows knows how to run.

SAMPLE ADD VERB TO DOTNET CLI
https://andrewlock.net/creating-a-simple-moving-average-calculator-in-csharp-1-a-simple-moving-average-calculator/
>dotnet run sma 2, 4, 5, 3, 8, 6, 4 -k 3
