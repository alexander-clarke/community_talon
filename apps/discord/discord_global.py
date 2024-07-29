from talon import Module, app, actions, ctrl, ui

mod = Module()

@mod.action_class
class discord_global_actions:
  def discord_global_mute():
    """"""
    
    actions.key("ctrl-alt-shift-t")

    #check for any teams running
    if any(map(lambda app: app.name=="Microsoft Teams", ui.apps(background=False))):
      # Unfortunately app=... doesn't work on windows we have to do the workaround
      # ctrl.key_press("m", ctrl=True, shift=True, app="microsoft_teams")
      current_app = actions.app.name()
      focused_on_teams = current_app == "Microsoft Teams"
      if not focused_on_teams:
        actions.user.switcher_focus("Microsoft Teams")

      #teams mute hotkey
      actions.key("ctrl-shift-m")

      if not focused_on_teams:
        actions.user.switcher_focus(current_app)
    
        
  def discord_global_screen_share():
    """"""
    actions.key("ctrl-alt-shift-s")
