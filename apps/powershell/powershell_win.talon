os: windows
and win.title: /Windows PowerShell/
os: windows
and app.exe: powershell.exe
-
# makes the commands in terminal.talon available
tag(): terminal

# activates the implementation of the commands/functions in terminal.talon
tag(): user.generic_windows_shell

# makes commands for certain applications available
# you can deactivate them if you do not use the application
tag(): user.git
tag(): user.anaconda
# tag(): user.kubectl

tag(): user.svn
tag(): user.p4
tag(): user.adb

tag(): user.unreal_commands

quest ((you|u) ee| youey): insert("questue ")