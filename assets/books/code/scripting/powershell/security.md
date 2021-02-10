## SECURITY

Not a security boundary
Designed to prevent a user from unknowingly running a script
A determined user can easily bypass the execution policy

### Execution policy

Only affects commands running in a script
Interactively run commands are not in Execution policy scope

- Restricted (defaut on clients)
- RemoteSigned (defaut on servers)
Requires downloaded scripts to be signed by a trusted publisher in order to be run.

> Get-ExecutionPolicy

To change the execution policy:
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

GPO: Group Policy Object
To apply a group stategy: GPMC.msc

### Credentials

>Get-Credential
enter user/pwd