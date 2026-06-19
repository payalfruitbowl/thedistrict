while ($true) {
    # Check if there are any changes
    $status = git status --porcelain
    if ($status) {
        Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Changes detected. Committing and pushing..." -ForegroundColor Cyan
        git add .
        git commit -m "Auto-update from local"
        git push origin main
        Write-Host "Push complete!" -ForegroundColor Green
    }
    # Wait for 10 seconds before checking again
    Start-Sleep -Seconds 10
}
