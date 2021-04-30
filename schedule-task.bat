@echo off
schtasks /create /tn MIB-Automation /tr %CD%\run-agent.bat /sc weekly /d MON /st 09:00