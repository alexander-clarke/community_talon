#defines the commands that sleep/wake Talon
mode: all
-
^sleep all [<phrase>]$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
^go to sleep [<phrase>]$: speech.disable()
^wake up$: speech.enable()
^touch and go to sleep [<phrase>]$: 
  mouse_click(0)
  speech.disable()
