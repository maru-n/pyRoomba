import unittest
from pyroomba import Roomba
from time import sleep

#SERIAL_DEVICE = "/dev/tty.usbserial-DA017V7D"
SERIAL_DEVICE = "/dev/ttyUSB0"

class TestRoomba(unittest.TestCase):
    def setUp(self):
        self.roomba = Roomba(SERIAL_DEVICE)
        self.roomba.command_start()
        sleep(0.5)
        self.roomba.command_safe()
        sleep(0.5)

    def tearDown(self):
        self.roomba.command_stop()
        sleep(0.5)
        #self.roomba.command_reset()
        #sleep(1)

    def test_send_bytes(self):
        self.roomba.send_bytes([1])
        sleep(0.5)

    def test_drive_direct(self):
        self.roomba.command_drive_direct(-0.1,-0.1)
        sleep(0.5)
        self.roomba.command_drive_direct(0.1,-0.1)
        sleep(0.5)
        self.roomba.command_drive_direct(-0.1,0.1)
        sleep(0.5)
        self.roomba.command_drive_direct(0.1,0.1)
        sleep(0.5)
        self.roomba.command_drive_direct(0,0)

    def test_digit_leds_ascii(self):
        self.roomba.command_digit_leds_ascii('TEST')
        sleep(1)

if __name__ == '__main__':
    unittest.main()
