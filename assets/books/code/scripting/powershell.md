# Dotnet - Powershell

It uses commands (cmdlets)
System administration tasks: managing the registry to WMI (Windows Management Instrumentation) — are exposed via PowerShell cmdlets

($env:path.split(';')) | where {$_ -like '*mingw*'} | ls

$array = @(1,'hello')
$array | Get-Member
Get-Member -InputObject $array
Name           MemberType            Definition
----           ----------            ----------
Add            Method                int IList.Add(System.Object value)

Get-Member -InputObject $array | ForEach-Object { $_.Name }
Get-Member -InputObject $array | ForEach-Object { $_.MemberType }
Get-Member -InputObject $array  | where {$_.MemberType -like '*Method*'} 
Get-Member -InputObject $array  | where {$_.MemberType -like '*Property*'} 



On startup, PowerShell will run any .ps1 files it finds in the "My Documents/PowerShell"
Typically a xxxx_profile.ps1
$profile is an automatic variable that points at your user profile for all PowerShell hosts
C:\Users\nguin\Documents\PowerShell\Microsoft.PowerShell_profile.ps1   
!! The file is listed but can not exists, it's the default!
For me I just have a 'profile.ps1" 

%USERPROFILE% 'C:\Users\nguin'
## Windows PATH environment variable 
*  is where applications look for executables -- meaning it can make or break a system or utility installation
Admins can use PowerShell to manage the PATH variable -- a process that entails string manipulation.
$env:Path
Path strings that refer to a directory are technically correct with or without a trailing slash -- '\' -- and, either way, that path will resolve correctly. 

Modify user/system environment variables permanently (i.e. will be persistent across shell restarts)
    Permanent modify a system environment variable
    [Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)
    Permanent modify a user environment variable
    [Environment]::SetEnvironmentVariable("INCLUDE", $env:INCLUDE, [System.EnvironmentVariableTarget]::User)
        
$addPath = 'C:\TopSecret\Bin'
// Iterate through all existing paths and check if the new path is already included with or without a '\' on the end
Set-PathVariable {
    param (
        [string]$AddPath,
        [string]$RemovePath
    )
    $regexPaths = @()
    if ($PSBoundParameters.Keys -contains 'AddPath'){
        $regexPaths += [regex]::Escape($AddPath)
    }

    if ($PSBoundParameters.Keys -contains 'RemovePath'){
        $regexPaths += [regex]::Escape($RemovePath)
    }
    
    $arrPath = $env:Path -split ';'
    foreach ($path in $regexPaths) {
        $arrPath = $arrPath | Where-Object {$_ -notMatch "^$path\\?"}
    }
    $env:Path = ($arrPath + $addPath) -join ';'
}
    
To remove all " from paths in the PATH environment variable for your session: 
$($Env:PATH).Split(';') | %{ $str += "$($_.Trim('"'));" }; $Env:PATH=$str
    
download.page(code/scripting/ps_files_recursive_action.md)


## :: Static member operator
Call the static properties operator and methods of a .NET Framework class.
```powershell
[datetime] | gm -static     Find the static properties and methods of an object (gm = alias Get-Member)
[datetime]::now
[datetime]::Utcnow
```
## Get Members
$array = @(1,'hello')
$array | Get-Member
Get-Member -InputObject $array

$array = [int[]]::new(5)
for ($index = 0; $index -lt 5; $index++) {
    $array[$index] = $index * 2
}

[System.Collections.Generic.List[int]]$list = @()
foreach ($value in 1..5) {    
    $list.Add($value)
}
gm -InputObject $list



$List = [System.Collections.Generic.List[object]]@(1..5)
$List.AddRange(5..10)
$List = [System.Collections.Generic.List[int]]@(1..5)
$List.AddRange([int[]](5..10))

$File = Get-Item c:\test\textFile.txt
$File.PSObject.Properties | Where-Object isSettable | Select-Object -Property Name

Name
----
PSPath
PSParentPath
PSChildName
PSDrive
PSProvider
PSIsContainer
IsReadOnly
CreationTime
CreationTimeUtc
LastAccessTime
LastAccessTimeUtc
LastWriteTime
LastWriteTimeUtc
Attributes


## More

- https://intellitect.com/how-i-installed-software-on-a-server/
- https://searchwindowsserver.techtarget.com/tutorial/Implement-simple-server-monitoring-with-PowerShell
- https://searchitoperations.techtarget.com/answer/Manage-the-Windows-PATH-environment-variable-with-PowerShell
- https://searchitoperations.techtarget.com/answer/Perform-a-Windows-event-log-search-with-PowerShell