# Types

***VALUE TYPES***
struct, enum, bool, int, char, float, double, decimal

***REFERENCE TYPES***
class, array, delegate, interface, object, string

***PREDEFINED TYPES = BUILT-IN TYPES***
int, char, float, double, decimal, bool, struct, enum, string, object

using System;
Important types not defined in C#
Contains the most .Net framework types (DateTime...)

***DISCOVER PROPERTIES, METHODS...***
'w32time' | Get-Member   
$CustomObject = [pscustomobject]@{ Name = 'w32time' }
$CustomObject | Get-Member
 
int i = 5;
string s = "Hello";
double d = 1.0;
int[] numbers = new int[] {1, 2, 3};
int[] numbers = { 1, 3, 5, 7, 9 };
foreach (var n in numbers) Console.WriteLine(n);
Dictionary<int,Order> orders = new Dictionary<int,Order>();

Range(0, 6).Select(i => ...)

download.page(dotnet/types/default_values.md)

          
::::
download.page(dotnet/types/ref/interfaces.md)
::::
download.page(dotnet/types/ref/string.md)
::::
download.page(dotnet/types/ref/delegates.md)
::::
download.page(dotnet/types/ref/class.md)
::::
download.page(dotnet/types/ref/dynamic.md)
::::
download.page(dotnet/types/ref/record.md)
::::
download.page(dotnet/language/covariance.md)
::::
download.page(dotnet/types/val/structs.md)
::::
download.page(dotnet/types/val/range.md)
::::
download.page(dotnet/types/val/span.md)
::::
download.page(dotnet/types/val/memory.md)