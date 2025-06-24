from talon import Module

mod = Module()
apps = mod.apps
apps.microsoft_teams = """
os: linux
and app.name: /teams/
os: linux
and app.name: /Teams/
"""

mod.apps.microsoft_teams = r"""
os: windows
and app.name: Microsoft Teams
os: windows
and app.exe: /^ms\-teams\.exe$/i
"""
