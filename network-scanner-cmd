@echo off
setlocal enabledelayedexpansion
set network=192.168.1.
set start=1
set end=254

for /L %%i in (%start%, 1, %end%) do (
    set ip=%network%%%i
    ping -n 1 !ip! > nul
    if !errorlevel!==0 (
        echo Device found: !ip!
    )
)
