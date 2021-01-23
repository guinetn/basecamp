# NUnit

Unit-testing framework for all .Net languages.

### Install
Full NUnit install via NuGet.
NUnitLite install via NuGet.

### Configure

<ItemGroup>
  <PackageReference Include="Microsoft.NET.Test.Sdk" Version="15.5.0" />
  <PackageReference Include="NUnit" Version="3.9.0" />
  <PackageReference Include="NUnit3TestAdapter" Version="3.9.0" />
</ItemGroup>

.NET Core command line test:
> dotnet test .\test\NetCore10Tests\NetCore10Tests.csproj

https://nunit.org/
https://github.com/nunit/nunit-csharp-samples