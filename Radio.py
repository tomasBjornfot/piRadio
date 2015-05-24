import os
import time
class Radio:
    def __init__(self):
        self.stations = [] # all station URL's in the category
        self.station = '' # the URL of the current station.
        self.stationNumber = 1 # current station number (stations[n-1])
        self.stationNames = []  # all station names in the category
        self.stationCategory = [] # the current category
        self.numberOfStations = 0 # the number of stations in the category
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
                        line = line.rstrip()
                        lineVector = line.split(',')
                        self.stations.append(lineVector[0])
                        self.stationNames.append(lineVector[1])
                        self.stationCategory.append(lineVector[2])
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
