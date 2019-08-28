function get-gitstatus { git status -sb }
Set-Alias -Name g -Value get-gitstatus

function get-githist { git hist }
Set-Alias -Name gh -Value get-githist

function gitadd { git add }
Set-Alias -Name ga -Value gitadd

function gitpull { git pull }
Set-Alias -Name gp -Value gitpull

function gitbranch { git branch }
Set-Alias -Name gb -Value gitbranch

function gitcommit { git commit }
Set-Alias -Name gc -Value gitcommit

function gitshow { git show }
Set-Alias -Name gs -Value gitshow
