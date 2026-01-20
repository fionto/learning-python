# Script: Generatore ASCII Tree in Markdown
# Percorso fisso: C:\GitRepositories\learning-python
# Output: Desktop\progetto.md con formattazione allineata

$sourceFolder = "C:\GitRepositories\learning-python"
$desktopPath = [Environment]::GetFolderPath("Desktop")
$outputFile = Join-Path $desktopPath "progetto.md"

# Verifica esistenza cartella sorgente
if (-not (Test-Path $sourceFolder)) {
    Write-Host "ERRORE: Il percorso $sourceFolder non esiste" -ForegroundColor Red
    exit
}

# Colonna di allineamento per i commenti
$alignColumn = 35

# Funzione ricorsiva per generare l'albero
function Get-TreeStructure {
    param(
        [string]$Path,
        [string]$Prefix = ""
    )
    
    $items = Get-ChildItem -Path $Path -Force | Where-Object {
        # Escludi cartella .git e file .ps1
        $_.Name -ne ".git" -and $_.Extension -ne ".ps1"
    } | Sort-Object { $_.PSIsContainer }, Name
    
    $output = @()
    
    foreach ($item in $items) {
        if ($item.PSIsContainer) {
            # Gestione cartelle
            $folderName = "$($item.Name)/"
            $line = "$Prefix├── $folderName"
            $padding = " " * [Math]::Max(1, $alignColumn - $line.Length)
            $output += "$line$padding# Cartella"
            
            # Ricorsione nelle sottocartelle
            $subItems = Get-TreeStructure -Path $item.FullName -Prefix "$Prefix    "
            $output += $subItems
        }
        else {
            # Gestione file
            $line = "$Prefix├── $($item.Name)"
            $padding = " " * [Math]::Max(1, $alignColumn - $line.Length)
            $output += "$line$padding# File"
        }
    }
    
    return $output
}

# Costruzione contenuto Markdown
$rootFolderName = Split-Path $sourceFolder -Leaf
$content = @()
$content += "``````text"
$content += "$rootFolderName/"

# Genera struttura ad albero
$treeContent = Get-TreeStructure -Path $sourceFolder
$content += $treeContent

$content += "``````"

# Salva file con codifica UTF8
$content | Out-File -FilePath $outputFile -Encoding UTF8 -Force

Write-Host "File generato con successo: $outputFile" -ForegroundColor Green
Write-Host "Cartelle e file analizzati (esclusi .git e .ps1)" -ForegroundColor Cyan