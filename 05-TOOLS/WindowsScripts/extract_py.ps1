# Script per consolidare esercizi Python in file Markdown
# Ricerca ricorsiva con ricostruzione struttura cartelle
# Output in 08-VALIDATION

# Forza encoding UTF-8 per caratteri accentati
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Configurazione percorsi
$basePath = "C:\GitRepositories\learning-python"
$sourcePath = Join-Path $basePath "02-EXERCISES"
$destPath = Join-Path $basePath "08-VALIDATION"

Write-Host ""
Write-Host "CONSOLIDATORE ESERCIZI PYTHON v2" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Sorgente:     $sourcePath" -ForegroundColor Yellow
Write-Host "Destinazione: $destPath" -ForegroundColor Yellow
Write-Host ""

# Verifica che la cartella sorgente esista
if (-not (Test-Path -Path $sourcePath -PathType Container)) {
    Write-Host "Errore: La cartella sorgente '$sourcePath' non esiste." -ForegroundColor Red
    exit 1
}

# Crea cartella destinazione se non esiste
if (-not (Test-Path -Path $destPath -PathType Container)) {
    New-Item -Path $destPath -ItemType Directory -Force | Out-Null
    Write-Host "Creata cartella destinazione: $destPath" -ForegroundColor Green
}

# Trova tutte le cartelle che contengono file .py (ricorsivo)
$foldersWithPython = Get-ChildItem -Path $sourcePath -Recurse -Filter "*.py" | 
    Select-Object -ExpandProperty DirectoryName | 
    Sort-Object -Unique

if ($foldersWithPython.Count -eq 0) {
    Write-Host "Errore: Nessun file .py trovato in '$sourcePath' o sottocartelle." -ForegroundColor Red
    exit 1
}

Write-Host "Trovate $($foldersWithPython.Count) cartelle con file Python." -ForegroundColor Green
Write-Host ""

# Contatori globali
$totalFiles = 0
$totalFolders = 0

foreach ($folder in $foldersWithPython) {
    # Calcola il percorso relativo dalla sorgente
    $relativePath = $folder.Substring($sourcePath.Length).TrimStart('\')
    
    # Estrai il nome della cartella finale
    $folderName = Split-Path -Path $folder -Leaf
    
    # Estrai il prefisso numerico (es. "04_01" da "04_01_ForLoops")
    if ($folderName -match '^(\d+(?:_\d+)*)') {
        $numericPrefix = $matches[1]
    } else {
        # Se non c'è prefisso numerico, usa il nome cartella
        $numericPrefix = $folderName
    }
    
    # Costruisci il nome del file di output
    $outputFileName = "${numericPrefix}_exercises.md"
    
    # Costruisci il percorso di destinazione mantenendo la struttura
    $destFolderPath = Join-Path $destPath $relativePath
    $outputFile = Join-Path $destFolderPath $outputFileName
    
    # Crea la cartella di destinazione se non esiste
    if (-not (Test-Path -Path $destFolderPath -PathType Container)) {
        New-Item -Path $destFolderPath -ItemType Directory -Force | Out-Null
    }
    
    # Ottieni tutti i file .py nella cartella corrente (non ricorsivo)
    $pythonFiles = Get-ChildItem -Path $folder -Filter "*.py" | Sort-Object Name
    
    if ($pythonFiles.Count -eq 0) {
        continue
    }
    
    # Costruisci il contenuto Markdown
    $content = @()
    
    # Header
    $content += "# $folderName"
    $content += ""
    $content += "**Esercizi consolidati**: $($pythonFiles.Count)"
    $content += "**Generato il**: $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
    $content += "**Sorgente**: ``$relativePath``"
    $content += ""
    $content += "---"
    $content += ""
    
    # Aggiungi ogni file Python
    foreach ($file in $pythonFiles) {
        # Nome file come heading
        $content += "## $($file.BaseName)"
        $content += ""
        
        # Contenuto in blocco ```python
        $content += '```python'
        $content += Get-Content -Path $file.FullName -Raw -Encoding UTF8
        $content += '```'
        $content += ""
        $content += "---"
        $content += ""
        
        $totalFiles++
    }
    
    # Scrivi il file
    $content | Out-File -FilePath $outputFile -Encoding utf8BOM
    
    $totalFolders++
    Write-Host "  [OK] $relativePath -> $outputFileName" -ForegroundColor Green
}

# Riepilogo finale
Write-Host ""
Write-Host "=================================" -ForegroundColor Cyan
Write-Host "COMPLETATO!" -ForegroundColor Green
Write-Host ""
Write-Host "  Cartelle processate: $totalFolders" -ForegroundColor Cyan
Write-Host "  File Python totali:  $totalFiles" -ForegroundColor Cyan
Write-Host "  Output in:           $destPath" -ForegroundColor Cyan
Write-Host ""