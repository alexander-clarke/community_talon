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

tag(): user.file_manager

tag(): user.svn
tag(): user.p4
tag(): user.adb

tag(): user.unreal_commands

# function questue {    adb.exe shell "am broadcast -a android.intent.action.RUN -e cmd '$args'"},
quest ((you | u) ee | youey): insert("questue ")

settings():
    user.powershell_always_refresh_title = false
