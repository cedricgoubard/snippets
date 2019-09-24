function get-gitstatus { git status -sb $args }
Set-Alias -Name g -Value get-gitstatus

function get-githist { git hist $args }
Set-Alias -Name gh -Value get-githist

function gitadd { git add $args }
Set-Alias -Name ga -Value gitadd

function gitpull { git pull $args }
Set-Alias -Name gpl -Value gitpull

function gitbranch { git branch $args }
Set-Alias -Name gb -Value gitbranch

function gitcommit { git commit $args }
Set-Alias -Name gco -Value gitcommit

function gitshow { git show $args }
Set-Alias -Name gs -Value gitshow
