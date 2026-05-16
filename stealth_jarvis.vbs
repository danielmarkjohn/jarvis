Set WshShell = CreateObject("WScript.Shell")
' 0 means hide the window completely
WshShell.Run chr(34) & "C:\AAA_Codespace\Project Hail Mary\jarvis\start_jarvis.bat" & Chr(34), 0
Set WshShell = Nothing