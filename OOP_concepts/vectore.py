class Vector:
    """
    Represents vector in Multidimential space
    """
    def __init__(self, d):
        """
        Create d-dimensional vector of zeros.
        """
        self._coords = d * [0]

    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)
    
    def __getitem__(self, j):
        """Return jth coordinate of vector"""
        return self._coords[j]
    
    def __setitem__(self, i, value):
        """Set jth coordinate of vector to given value."""
        self._coords[i] = value
    
    def __add__(self, other):
        """Return sum of two vectors"""
        result = Vector(self.__len__())
        if not (self.__len__() == other.__len__()): # is equal to len(self) == other(self)
            raise ValueError("Both vectors not in the same length")
            return False
        
        for i in range(len(self._coords)):
            result[i] = self.__getitem__(i) + other.__getitem__(i) #is equal to self[i] + other[i]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other #is eual to self.__eq__() == other.__eq__()

    def __str__(self):
        return "<"+ str(self._coords) +'>'
        



        