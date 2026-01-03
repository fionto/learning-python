# Script per consolidare tutti gli esercizi Python in un unico file
# Percorso sorgente degli esercizi
$sourcePath = "C:\GitRepositories\learning-python\Day03_for_loop"

# Percorso di destinazione (Desktop)
$desktopPath = [Environment]::GetFolderPath("Desktop")
$outputFile = Join-Path $desktopPath "lists_exercises_consolidated.txt"

# Ottieni tutti i file .py ordinati per nome
$pythonFiles = Get-ChildItem -Path $sourcePath -Filter "*.py" | Sort-Object Name

# Crea/sovrascrivi il file di output
"=" * 60 | Out-File -FilePath $outputFile -Encoding UTF8
"ESERCIZI - PYTHON CRASH COURSE" | Out-File -FilePath $outputFile -Append -Encoding UTF8
"Generato il: $(Get-Date -Format 'dd/MM/yyyy HH:mm')" | Out-File -FilePath $outputFile -Append -Encoding UTF8
"=" * 60 | Out-File -FilePath $outputFile -Append -Encoding UTF8
"" | Out-File -FilePath $outputFile -Append -Encoding UTF8

# Contatore per gli esercizi
$count = 0

foreach ($file in $pythonFiles) {
    $count++
    
    # Aggiungi separatore e nome del file
    "" | Out-File -FilePath $outputFile -Append -Encoding UTF8
    "-" * 60 | Out-File -FilePath $outputFile -Append -Encoding UTF8
    "FILE: $($file.Name)" | Out-File -FilePath $outputFile -Append -Encoding UTF8
    "-" * 60 | Out-File -FilePath $outputFile -Append -Encoding UTF8
    "" | Out-File -FilePath $outputFile -Append -Encoding UTF8
    
    # Leggi e aggiungi il contenuto del file
    Get-Content -Path $file.FullName -Encoding UTF8 | Out-File -FilePath $outputFile -Append -Encoding UTF8
    
    # Aggiungi una riga vuota dopo ogni esercizio
    "" | Out-File -FilePath $outputFile -Append -Encoding UTF8
}

# Aggiungi footer
"" | Out-File -FilePath $outputFile -Append -Encoding UTF8
"=" * 60 | Out-File -FilePath $outputFile -Append -Encoding UTF8
"TOTALE ESERCIZI: $count" | Out-File -FilePath $outputFile -Append -Encoding UTF8
"=" * 60 | Out-File -FilePath $outputFile -Append -Encoding UTF8

# Conferma
Write-Host "Completato! $count esercizi consolidati in:" -ForegroundColor Green
Write-Host $outputFile -ForegroundColor Cyan