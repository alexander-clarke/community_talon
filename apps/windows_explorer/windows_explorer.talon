app: windows_explorer
app: windows_file_browser
-
tag(): user.file_manager
go app data: user.file_manager_open_directory("%AppData%")
go program files: user.file_manager_open_directory("%programfiles%")
