#!/usr/bin/python3
import os
from subprocess import run
"""
    Provide some useful tools for Android developpment.
"""

# Definitions
def connect(ip = ""):
    if b"transport_id" in run(["adb", "devices", "-l"], capture_output=True).stdout:
        return True
    elif ip:
        try:
            r = run(["adb", "connect", ip], capture_output=True)
            if b'unable to connect' in r.stdout:
                return False
            else:
                return True
        except:
            return False
    else:
        return False
def wait_device(ip=""):
    try:
        while not connect(ip=ip):
            if os.path.exists(os.getenv("HOME")+'/rttk_roms/stop_wait'):
                os.remove(os.getenv("HOME")+'/rttk_roms/stop_wait')
                break
            pass
    except KeyboardInterrupt:
        print("Aborted.")
def get_logcat(color=False):
    if color:
        r= run(["adb","logcat","-Cd"], capture_output=True)
    else:
        r= run(["adb","logcat","-d"], capture_output=True)
    return r.stdout.decode('utf-8')
def clear_logcat():
    run(['adb', 'logcat', '-c'], capture_output=True)
def reboot(mode=''):
    run(['adb', 'reboot', mode], capture_output=True)
def reboot_recovery():
    reboot("recovery")
def reboot_bootloader():
    run(['adb', 'reboot-bootloader'], capture_output=True)
def reboot_system():
    reboot()
def get_dmesg():
    return run(['adb','shell', 'dmesg'], capture_output=True).stdout.decode('utf-8')
def logcat_grep(kw="", color=False):
    if color:
        r= run(["adb","logcat","-Cd", "|","grep", kw], capture_output=True)
    else:
        r= run(["adb","logcat","-d", "|","grep", kw], capture_output=True)
    return r.stdout.decode('utf-8')
def dmesg_grep(kw=""):
    return run(['adb','shell', 'dmesg', "|", "grep", kw], capture_output=True).stdout.decode('utf-8')
def sideload(file_path="", reboot_sideload=False):
    if reboot_sideload and not b'sideload' in run(["adb","get-status"], capture_output=True).stdout:
        run(['adb', 'reboot', 'sideload'], capture_output=True)
    while not b'sideload' in run(["adb","get-status"], capture_output=True).stdout:
        if os.path.exists(os.getenv("HOME")+'/rttk_roms/stop_wait'):
            os.remove(os.getenv("HOME")+'/rttk_roms/stop_wait')
            return
    run(['adb', 'sideload', file_path])

# Documentation
connect.__doc__="""Check connexion : if ip specified and not already connected, connect online. """
wait_device.__doc__="""Stop execution until a device connect or ~/rttk_roms/stop_wait file is created (and remove it). """
get_logcat.__doc__="""Get logcat content from the device, with or without color. """
clear_logcat.__doc__="""Clear logcat content. """
reboot.__doc__="""Reboot device into a specific mode, by default reboot to system. """
reboot_recovery.__doc__="""Reboot device into recovery mode. """
reboot_bootloader.__doc__="""Reboot device into bootloader. """
reboot_system.__doc__="""Reboot device into system. """
get_dmesg.__doc__="""Return dmesg content. """

# Specific tool execution
def execute(tool_name):
    if not tool_name in ['connect', 'wait_device', 'get_logcat', 'clear_logcat', 'reboot', 'reboot_recovery', 'reboot_bootloader', 'reboot_system', 'get_dmesg', 'logcat_grep', 'dmseg_grep', 'sideload']:
        raise Exception("Wrong tool name "+str(tool_name))
    if tool_name == "connect":
        if connect(ip=input("Specify an ip if you want to connect wireless []: ")):
            print("Success")
        else:
            print("Failed")
    elif tool_name == "wait_device":
        wait_device(ip=input("Specify an ip if you want to connect wireless []: "))
        print("Done")
    elif tool_name == "get_logcat":
        print(get_logcat())
        print("Done")
    elif tool_name == "clear_logcat":
        clear_logcat()
        print("Done")
    elif tool_name == "reboot":
        reboot(mode=input("Reboot mode [system]: "))
        print("Done")
    elif tool_name == "reboot_recovery":
        reboot_recovery()
        print("Done")
    elif tool_name == "reboot_bootloader":
        reboot_bootloader()
        print("Done")
    elif tool_name == "reboot_system":
        reboot_system()
        print("Done")
    elif tool_name == "get_dmesg":
        get_dmesg()
        print("Done")
    elif tool_name == "logcat_grep":
        logcat_grep(kw=input("grep keyword : "))
        print("Done")
    elif tool_name == "dmesg_grep":
        dmesg_grep(kw=input("grep keyword : "))
        print("Done")
    elif tool_name == "sideload":
        sideload(file_path=input("file path : "))
        print("Done")
    input("Press [ENTER] to continue")
# Test
if __name__ == '__main__':
    print("You have to run RomTestToolKit from main program. ")