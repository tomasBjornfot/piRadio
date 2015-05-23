import os
import time
class Radio:
        def __init__(self):
                self.stations = []
                self.station = ''
                self.stationNumber = 1
                self.numberOfStations = 0
        def startStation(self,station):
                print "start station",station
                self.setStation(station)
                self.add()
                self.play()
        def stopStation(self):
                print "stops station"
                self.stop()
                self.clear()
        def nextStation(self):
                self.stopStation()
                self.stationNumber = self.stationNumber + 1;
                if self.stationNumber > self.numberOfStations:
                        self.stationNumber = 1
                self.startStation(self.stationNumber)
        def readStations(self):
                with open('stations','r') as f:
                        for line in f:
                                self.stations.append(line.rstrip())
                                print "added",line.rstrip(),"to stations"
                self.numberOfStations = len(self.stations)
                print "number of stations",self.numberOfStations
        def setStation(self,stationNumber):
                self.station = self.stations[stationNumber-1]
        def add(self):
                os.system('mpc add '+self.station)
        def play(self):
                os.system('mpc play')
        def stop(self):
                os.system('mpc stop')
        def clear(self):
                os.system('mpc clear')
        def setVolume(self,vol):
                os.system('mpc volume '+str(vol))
                print "volume set to",vol



