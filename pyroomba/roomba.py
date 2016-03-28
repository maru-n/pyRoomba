#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import struct
import sys

SINGLE_COMMAND_LIST = [{
# Getting Started Commands
        'name': 'Start',
        'opcode': 128
    },{
        'name': 'Reset',
        'opcode': 7
    },{
        'name': 'Stop',
        'opcode': 173
    },{
    #     'name': '￼Baud',
    #     'opcode': 129
    # },{
# Mode Commands
        'name': 'Safe',
        'opcode': 131
    },{
        'name': 'Full',
        'opcode': 132
    },{
# Cleaning Commands
        'name': 'Clean',
        'opcode': 135
    },{
        'name': 'Max',
        'opcode': 136
    },{
        'name': 'Spot',
        'opcode': 134
    },{
        'name': 'Seek Dock',
        'opcode': 143
    },{
        'name': 'Power',
        'opcode': 133
    },{
    #     'name': 'Schedule',
    #     'opcode': 167
    # },{
    #     'name': 'Set Day/Time',
    #     'opcode': 168
    # },{
# Actuator Commands
    #     'name': 'Drive',
    #     'opcode': 137
    # },{
        'name': 'Drive Direct',
        'opcode': 145,
        'args': 'hh'
    },{
        'name': 'Drive PWM',
        'opcode': 146,
        'args': 'hh'
    },{
        'name': 'Motors',
        'opcode': 138,
    },{
        'name': 'PWM Motors',
        'opcode': 144,
    },{
        'name': 'LEDs',
        'opcode': 139,
    },{
        'name': 'Scheduling LEDS',
        'opcode': 162,
    },{
        'name': 'Digit LEDs Raw',
        'opcode': 163,
    },{
        'name': 'Buttons',
        'opcode': 165,
    },{
        'name': 'Digit LEDs ASCII',
        'opcode': 164,
    },{
        'name': 'Song',
        'opcode': 140,
    },{
        'name': 'Play',
        'opcode': 141,
    },{
# Input Commands
        'name': 'Sensors',
        'opcode': 142,
    },{
        'name': 'Query List',
        'opcode': 149,
    },{
        'name': 'Stream',
        'opcode': 148,
    },{
        'name': 'Pause/Resume Stream',
        'opcode': 150,
    }]



class Roomba(object):
    """Roomba class"""

    def __init__(self, port):
        if isinstance(port, str):
            self.__port = serial.Serial(port, 115200)
        else:
            self.__port = port
        self.__init_single_command_method()


    def __init_single_command_method(self):
        for cmd in SINGLE_COMMAND_LIST:
            def command(self, *args, cmd=cmd):
                if args:
                    bytes = struct.pack(">B" + cmd['args'], cmd['opcode'], args[0], args[1])
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
