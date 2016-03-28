#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
from . import roomba


def digit_leds_ascii_opcode_func(args):
    ascii_str = args[0]
    if len(ascii_str) != 4:
        raise roomba.RoombaException('digital leds ascii must be 4 chars.')
    bytes = [164]
    for c in ascii_str:
        b = ord(c)
        bytes.append(b)
    return bytes


GETTING_STARTED_COMMANDS = [{
        'name': 'Start',
        'opcode': 128
    },{
        'name': 'Reset',
        'opcode': 7
    },{
        'name': 'Stop',
        'opcode': 173
    # },{
    #     'name': '￼Baud',
    #     'opcode': 129
    }
]

MODE_COMMANDS = [{
        'name': 'Safe',
        'opcode': 131
    },{
        'name': 'Full',
        'opcode': 132
    }]

CLEANING_COMMANDS = [
    # {
    #     'name': 'Clean',
    #     'opcode': 135
    # },{
    #     'name': 'Max',
    #     'opcode': 136
    # },{
    #     'name': 'Spot',
    #     'opcode': 134
    # },{
    #     'name': 'Seek Dock',
    #     'opcode': 143
    # },{
    #     'name': 'Power',
    #     'opcode': 133
    #     'name': 'Schedule',
    #     'opcode': 167
    # },{
    #     'name': 'Set Day/Time',
    #     'opcode': 168
    # }
]

def drive_direct_opcode_func(args):
    vr = args[0]
    vl = args[1]
    if vr < -500 or 500 < vr or vl < -500 or 500 < vl:
        raise roomba.RoombaException('wheel speed must be in range -500 ~ 500 mm/sec.')
    return struct.pack(">Bhh", 145, args[0], args[1])

ACTUATOR_COMMANDS = [{
    #     'name': 'Drive',
    #     'opcode': 137
    # },{
        'name': 'Drive Direct',
        'opcode': 145,
        'opcode_func': drive_direct_opcode_func
    # },{
    #     'name': 'Drive PWM',
    #     'opcode': 146,
    #     'args': 'hh'
    # },{
    #     'name': 'Motors',
    #     'opcode': 138,
    # },{
    #     'name': 'PWM Motors',
    #     'opcode': 144,
    # },{
    #     'name': 'LEDs',
    #     'opcode': 139,
    # },{
    #     'name': 'Scheduling LEDS',
    #     'opcode': 162,
    # },{
    #     'name': 'Digit LEDs Raw',
    #     'opcode': 163,
    # },{
    #     'name': 'Buttons',
    #     'opcode': 165,
    },{
        'name': 'Digit LEDs ASCII',
        'opcode': 164,
        'opcode_func': digit_leds_ascii_opcode_func
    # },{
    #     'name': 'Song',
    #     'opcode': 140,
    # },{
    #     'name': 'Play',
    #     'opcode': 141,
    }]

INPUT_COMMANDS = [
    # {
    #     'name': 'Sensors',
    #     'opcode': 142,
    # },{
    #     'name': 'Query List',
    #     'opcode': 149,
    # },{
    #     'name': 'Stream',
    #     'opcode': 148,
    # },{
    #     'name': 'Pause/Resume Stream',
    #     'opcode': 150,
    # }
]

COMMANDS = GETTING_STARTED_COMMANDS + MODE_COMMANDS + CLEANING_COMMANDS + ACTUATOR_COMMANDS + INPUT_COMMANDS
