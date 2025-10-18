@echo off
setlocal enabledelayedexpansion

set "processed=0"
set "failed=0"

echo Starting Google AdSense insertion process...
echo.

:: Process files in batches
for %%f in (
    "categories\characters\disney.html"
    "categories\characters\fairy-tales.html"
    "categories\characters\fantasy.html"
    "categories\characters\gaming.html"
    "categories\characters.html"
    "categories\educational\geometry.html"
    "categories\educational\puzzles.html"
    "categories\educational\stationery.html"
    "categories\educational.html"
    "categories\food\apple-viewer.html"
    "categories\food\cakes.html"
    "categories\food\candy.html"
    "categories\food\fast-food.html"
    "categories\food\fruits.html"
    "categories\food\ice-cream.html"
    "categories\food\vegetables.html"
    "categories\food.html"
    "categories\holidays\christmas.html"
    "categories\holidays\halloween\fireworks.html"
    "categories\holidays\halloween.html"
) do (
    call :process_file "%%f"
)

echo First batch completed. Processed: %processed%, Failed: %failed%
echo.

for %%f in (
    "categories\holidays\summer.html"
    "categories\holidays\thanksgiving.html"
    "categories\holidays.html"
    "categories\insects\bees.html"
    "categories\insects\butterflies.html"
    "categories\insects\other-bugs.html"
    "categories\insects.html"
    "categories\land-animals\farm-animals.html"
    "categories\land-animals\wild-animals.html"
    "categories\land-animals.html"
    "categories\nature\flowers.html"
    "categories\nature\natural-elements.html"
    "categories\nature\trees.html"
    "categories\nature.html"
    "categories\ocean-animals\fish.html"
    "categories\ocean-animals\mammals.html"
    "categories\ocean-animals\sea-creatures.html"
    "categories\ocean-animals.html"
    "categories\sports\activities.html"
    "categories\sports\index.html"
) do (
    call :process_file "%%f"
)

echo Second batch completed. Processed: %processed%, Failed: %failed%
echo.

for %%f in (
    "categories\sports\sports-equipment.html"
    "categories\sports\toys.html"
    "categories\sports.html"
    "categories\vehicles\air.html"
    "categories\vehicles\airplanes.html"
    "categories\vehicles\buses.html"
    "categories\vehicles\cars.html"
    "categories\vehicles\construction.html"
    "categories\vehicles\emergency.html"
    "categories\vehicles\helicopters.html"
    "categories\vehicles\land.html"
    "categories\vehicles\rockets.html"
    "categories\vehicles\sea.html"
    "categories\vehicles\ships.html"
    "categories\vehicles\taxi.html"
    "categories\vehicles\trains.html"
    "categories\vehicles\trucks.html"
    "categories\vehicles.html"
    "color-by-number\animals\index.html"
    "color-by-number\animals\lion.html"
    "color-by-number\holidays\index.html"
    "pdf-detail.html"
) do (
    call :process_file "%%f"
)

echo.
echo ========================================
echo Processing Complete!
echo Successfully processed: %processed% files
echo Failed: %failed% files
echo ========================================
goto :eof

:process_file
set "file=%~1"
if not exist "%file%" (
    echo ERROR: File %file% not found
    set /a failed+=1
    goto :eof
)

:: Check if AdSense already exists
findstr /C:"Google AdSense" "%file%" >nul 2>&1
if !errorlevel! equ 0 (
    echo SKIP: %file% already has AdSense code
    goto :eof
)

:: Use PowerShell to do the replacement
powershell -Command "(Get-Content '%file%') -replace '</script>\n    <meta charset=\"UTF-8\">', '</script>\n\n<!-- Google AdSense -->\n<script async src=\"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6031811659039199\"\n     crossorigin=\"anonymous\"></script>\n    <meta charset=\"UTF-8\">' | Set-Content '%file%'"

:: Verify the change was made
findstr /C:"Google AdSense" "%file%" >nul 2>&1
if !errorlevel! equ 0 (
    echo SUCCESS: Added AdSense code to %file%
    set /a processed+=1
) else (
    echo ERROR: Failed to process %file%
    set /a failed+=1
)
goto :eof