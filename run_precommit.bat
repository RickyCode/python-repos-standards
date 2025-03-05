@echo off
REM Batch script to run pre-commit and git restage multiple times

echo Running pre-commit and git restage sequence...

git restage

pre-commit run
IF %ERRORLEVEL% NEQ 1 (
    echo Pre-commit completado...
    git restage
    exit /b
)

git restage
echo Git restage step 1 completed.

pre-commit run
IF %ERRORLEVEL% NEQ 1 (
    echo Pre-commit completado...
    git restage
    exit /b
)

git restage
echo Git restage step 2 completed.

pre-commit run
IF %ERRORLEVEL% NEQ 1 (
    echo Pre-commit completado...
    git restage
    exit /b
)

git restage
echo Git restage step 3 completed.

echo Sequence complete!
pause
