# not mode: sleep
mode: all
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.game")
    user.gdb_disable()
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
    mode.disable("user.game")
^mixed mode$:
    mode.disable("sleep")
    mode.enable('dictation')
    mode.enable("command")