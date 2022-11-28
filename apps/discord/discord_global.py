from talon import Module, app, actions

mod = Module()


@mod.action_class
class discord_global_actions:
  def discord_global_mute():
    """"""
    if True:
      actions.key("ctrl-alt-shift-t")
    else:
      focused_on_discord  = True
      if not actions.app.name().lower() =="discord":
        actions.user.switcher_focus("discord")
        focused_on_discord = False
      
      actions.user.discord_mute()
      
      if not focused_on_discord:
        actions.key("alt-tab")
        
  def discord_global_screen_share():
    """"""
    actions.key("ctrl-alt-shift-s")
      