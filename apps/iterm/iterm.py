import os

from talon import Context, Module, actions, ui

ctx = Context()
mod = Module()

mod.apps.iterm2 = """
os: mac
and app.bundle: com.googlecode.iterm2
"""
ctx.matches = r"""
app: iterm2
"""

directories_to_remap = {}
directories_to_exclude = {}


@ctx.action_class("user")
class UserActions:
    def file_manager_current_path():
        title = ui.active_window().title
        if ":" in title:
            title = title.split(":")[1].lstrip()
        if "~" in title:
            title = os.path.expanduser(title)
        if title in directories_to_remap:
            title = directories_to_remap[title]
        if title in directories_to_exclude:
            title = None
        return title

    def tab_jump(number: int):
        actions.key(f"cmd-{number}")

    def tab_final():
        actions.key("cmd-9")

    def terminal_clear_screen():
        """Clear screen"""
        actions.key("ctrl-l")

@ctx.action_class("app")
class AppActions:
    def tab_next():
        actions.key("cmd-shift-]")

    def tab_previous():
        actions.key("cmd-shift-[")
