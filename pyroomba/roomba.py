#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import struct
import sys
from . import command_list

class Roomba(object):
    """Roomba class"""

    def __init__(self, port):
        if isinstance(port, str):
            self.__port = serial.Serial(port, 115200)
        else:
            self.__port = port
        self.__init_single_command_method()


    def __init_single_command_method(self):
        for cmd in command_list.COMMANDS:
            def command(self, *args, cmd=cmd):
                if "opcode_func" in cmd:
                    bytes = cmd['opcode_func'](args)
                    self.send_bytes(bytes)
                else:
                    self.send_bytes([cmd['opcode']])
            method_name = "command_" + cmd['name'].replace(" ", "_").lower()
            setattr(Roomba, method_name, command)


    def send_bytes(self, bytes):
        ret = self.__port.write(bytes)
        if ret != len(bytes):
            raise Exception("error occured on write serial code.")


class RoombaException(Exception):
    """RoombaException"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
