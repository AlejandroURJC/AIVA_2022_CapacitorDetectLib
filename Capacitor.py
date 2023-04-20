class Capacitor:
    def __init__(self, c, r):
        self._centroid = c
        self._r = r
        self._size = None

    def getCentroid(self):
        return self._centroid

    def getRadius(self, ):
        return self._r

    def getSize(self, ):
        return self._size

    def setSize(self, s):
        self._size = s
