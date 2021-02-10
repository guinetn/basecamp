# Screen

Clear-Host = cls
Write-Host "hi"

Out-Host            
writes directly to the PowerShell host, but it doesn't produce object-based output for the pipeline. So it can't be piped to Get-Member.
Get-ChildItem | Out-Host -Paging     output page-by-page display

$number = Get-Random -Minimum 1 -Maximum 10
do {
  $guess = Read-Host -Prompt "What's your guess?"
  if ($guess -lt $number) {
    Write-Output 'Too low!'
  }
  elseif ($guess -gt $number) {
    Write-Output 'Too high!'
  }
}
until ($guess -eq $number)