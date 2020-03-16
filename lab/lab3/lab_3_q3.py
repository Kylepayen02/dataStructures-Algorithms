class UnsignedBinaryInteger:
    def __init__(self, bin_num_str):
        self.data = bin_num_str
    def __add__(self, other):
        ''' Creates and returns an UnsignedBinaryInteger object
        that represent the sum of self and other (also of
        type UnsignedBinaryInteger) the result also shouldn’t have
        excess leading 0’s'''
    def decimal(self):
        ''' returns the decimal value of the binary integer'''
    def __lt__(self, other):
        ''' returns True if self is less than other, or False
        otherwise'''
    def __gt__(self, other):
        ''' returns True if self is greater than other, or False
        otherwise'''
    def __eq__(self, other):
        ''' returns True if self is equal to other, or False
        otherwise'''