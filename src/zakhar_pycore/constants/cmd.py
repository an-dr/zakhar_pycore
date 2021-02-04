# *************************************************************************
#
# Copyright (c) 2021 Andrei Gramakov. All rights reserved.
#
# This file is licensed under the terms of the MIT license.
# For a copy, see: https://opensource.org/licenses/MIT
#
# site:    https://agramakov.me
# e-mail:  mail@agramakov.me
#
# *************************************************************************


class CMD:
    class MOVE:
        FORWARD = 119
        BACKWARD = 115
        LEFT = 97
        RIGHT = 100
        SHIVER = 0x71
        STOP_KB = 0x20
        STOP = 0xA0
        SPEED0 = 0x30
        SPEED1 = 0x31
        SPEED2 = 0x32
        SPEED3 = 0x33
        MPU_CALIBRATE = 99
        TEST = 0x74

    class FACE:
        CALM = 0x30
        BLINK = 0x31
        ANGRY = 0x32
        HAPPY = 0x33
        SAD = 0x34


class NO_CMD:
    NO_COMMANDS = -1
