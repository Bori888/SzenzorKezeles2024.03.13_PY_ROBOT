#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #kép a kijelzőn

        self.kep1= Image(ImageFile.BOTTOM_LEFT)
        self.kep2= Image(ImageFile.BOTTOM_RIGHT)


        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

    def akumlator_allapot(self):
        #konzoolablakra kiirás
        akuErtek  = ("Az aku töltötségi\n szintje: " +str(int(self.ev3.battery.voltage())/1000)+ " V")
        print(akuErtek)
        #robotra kiirás
        self.ev3.screen.print(akuErtek)
        wait(3000)


    def ne_zuhanjon_le(self):
        #: Haladjon az asztal széle fele a robot majd álljon meg a szélén.
        while(self.cs.reflection()>45):
            self.robot.drive(100, 0)
            print("Szín",self.cs.reflection() )
        self.robot.stop(Stop.BRAKE)
        

        


    def csipog(self):
        self.ev3.speaker.beep()

