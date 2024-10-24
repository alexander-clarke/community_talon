import os
import subprocess

from talon import Module

mod = Module()


@mod.action_class
class Actions:
    def system_command(cmd: str):
        """execute a command on the system"""
        subprocess.call(cmd, shell=True)

    def system_command_nb(cmd: str):
        """execute a command on the system without blocking"""
        subprocess.Popen(cmd, shell=True)
