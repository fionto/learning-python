# Script per consolidare esercizi Python in un file Markdown
# Con input interattivo e syntax highlighting

# 1) Chiedi la cartella sorgente
Write-Host ""
Write-Host "CONSOLIDATORE ESERCIZI PYTHON" -ForegroundColor Cyan
Write-Host "=============================" -ForegroundColor Cyan
Write-Host ""

$sourcePath = Read-Host "Inserisci il percorso della cartella con i file .py"

# Verifica che la cartella esista
if (-not (Test-Path -Path $sourcePath -PathType Container)) {
    Write-Host "Errore: La cartella '$sourcePath' non esiste." -ForegroundColor Red
    exit 1
}

# Ottieni il nome della cartella per il file di output
$folderName = Split-Path -Path $sourcePath -Leaf

# 4) File di output nella stessa cartella, con nome della cartella
$outputFile = Join-Path $sourcePath "$folderName.md"

# Ottieni tutti i file .py ordinati per nome
$pythonFiles = Get-ChildItem -Path $sourcePath -Filter "*.py" | Sort-Object Name

# Verifica che ci siano file Python
if ($pythonFiles.Count -eq 0) {
    Write-Host "Errore: Nessun file .py trovato in '$sourcePath'." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Trovati $($pythonFiles.Count) file Python." -ForegroundColor Green
Write-Host "Elaborazione in corso..." -ForegroundColor Yellow
Write-Host ""

# 2) Crea file Markdown
$content = @()

# Header
$content += "# $folderName"
$content += ""
$content += "**Esercizi consolidati**: $($pythonFiles.Count)"
$content += "**Generato il**: $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
$content += ""
$content += "---"
$content += ""

# Contatore
$count = 0

foreach ($file in $pythonFiles) {
    $count++
    
    # Nome file come heading
    $content += "## $($file.BaseName)"
    $content += ""
    
    # 3) Contenuto in blocco ```python
    $content += '```python'
    $content += Get-Content -Path $file.FullName -Raw
    $content += '```'
    $content += ""
    $content += "---"
    $content += ""
}

# Scrivi tutto il contenuto nel file
$content | Out-File -FilePath $outputFile -Encoding UTF8

# Conferma
Write-Host "Completato!" -ForegroundColor Green
Write-Host ""
Write-Host "  File creato: $outputFile" -ForegroundColor Cyan
Write-Host "  Esercizi:    $count" -ForegroundColor Cyan
Write-Host ""