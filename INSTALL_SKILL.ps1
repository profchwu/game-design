[CmdletBinding()]
param(
    [string]$Destination,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$source = $PSScriptRoot
if (-not $Destination) {
    $codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
    $Destination = Join-Path (Join-Path $codexHome 'skills') 'game-design'
}

if (Test-Path $Destination) {
    if (-not $Force) {
        throw "Skill already exists: $Destination. Re-run with -Force to replace it."
    }
    Remove-Item -LiteralPath $Destination -Recurse -Force
}

New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Get-ChildItem -LiteralPath $source -Force | Where-Object { $_.Name -notin @('.git', 'README.md', 'INSTALL_SKILL.ps1') } | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
}

Write-Output "Installed game-design -> $Destination"
Write-Output 'Restart Codex so the Skill is discovered.'
