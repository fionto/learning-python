<#
.SYNOPSIS
    Syncs local Git repositories to a OneDrive backup folder using Robocopy.

.DESCRIPTION
    This script mirrors the content of C:\GitRepositories to a specified OneDrive path.
    WARNING: Using /MIR means if you delete a file locally, it WILL be deleted in the backup.

.NOTES
    Author: BudgetBridge Student
    Date: 2026-02-28
#>

# --- CONFIGURATION ---
# Source: Your main working folder
$SourcePath = "C:\GitRepositories"

# Destination: Your OneDrive Backup folder
# Ensure this path exists before running!
$DestPath = "R:\OneDrive\10 - Backup\60-69 git\61_Ryzen"

# --- SAFETY CHECKS ---

# 1. Check if Source exists
if (-not (Test-Path -Path $SourcePath)) {
    Write-Host "❌ ERROR: Source path not found: $SourcePath" -ForegroundColor Red
    exit 1
}

# 2. Check if Destination exists (Create it if missing, but warn if it looks wrong)
if (-not (Test-Path -Path $DestPath)) {
    Write-Host "⚠️  Destination path does not exist. Creating it..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path $DestPath | Out-Null
}

# 3. Prevent accidental reversal (Basic sanity check)
# If the destination looks like the system drive root, abort.
if ($DestPath -eq "C:\" -or $DestPath -eq "C:\GitRepositories") {
    Write-Host "❌ CRITICAL ERROR: Destination path is invalid or matches source. Aborting to prevent data loss." -ForegroundColor Red
    exit 1
}

# --- EXECUTION ---

Write-Host "🚀 Starting Sync..." -ForegroundColor Cyan
Write-Host "   From: $SourcePath"
Write-Host "     To: $DestPath"
Write-Host "   Mode: MIRROR (/MIR) - Exact Clone (Deletions will propagate)" -ForegroundColor Yellow
Write-Host "---------------------------------------------------"

# Robocopy Arguments:
# /MIR       : Mirror directory tree (copies new/changed, deletes extra in dest)
# /Z         : Restartable mode (good for large files/unstable networks)
# /R:3       : Retry 3 times on failed files (default is 1 million!)
# /W:5       : Wait 5 seconds between retries
# /MT:8      : Multi-threaded (8 threads) for faster speed
# /NFL /NDL  : No File List / No Dir List (cleaner output, only shows errors/summary)
# /NP        : No Progress (prevents console spamming with percentages)

$RoboArgs = @(
    "$SourcePath",
    "$DestPath",
    "/MIR",
    "/Z",
    "/R:3",
    "/W:5",
    "/MT:8",
    "/NFL",
    "/NDL",
    "/NP"
)

# Run Robocopy
& robocopy @RoboArgs

# Check Exit Code
# Robocopy returns codes > 7 for errors, but 0-7 are success levels (e.g., files copied)
$ExitCode = $LASTEXITCODE

if ($ExitCode -gt 7) {
    Write-Host "❌ Sync completed with ERRORS (Code: $ExitCode)" -ForegroundColor Red
} elseif ($ExitCode -gt 0) {
    Write-Host "✅ Sync completed successfully (Files were copied/updated)." -ForegroundColor Green
} else {
    Write-Host "✅ Sync completed (No changes needed, folders are identical)." -ForegroundColor Green
}

Write-Host "---------------------------------------------------"
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")