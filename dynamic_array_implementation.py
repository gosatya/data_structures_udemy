import ctypes
import sys
from random import choice


class DynamicArray(object):

    def __init__(self):
        self.n = 0  # count actual elemetns. Default is zero.
        self.capacity = 1  # default capacity of array
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        RETURN NUMBER OF ELEMENTS SORTED IN ARRAY
        """
        return self.n

    def __getitem__(self, k):
        """
        RETURN ELEMENT AT INDEX k.
        """
        if not 0 <= k < self.n:
            return IndexError("K is out of bounds!")  # check if index k exists for array

        return self.A[k]  # Retrieve from array at index k

    def append(self, ele):
        """
        ADD ELEMENT AT THE END OF ARRAY
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # double capacity if not enough

        self.A[self.n] = ele  # set self.n index to element
        self.n += 1

    def _resize(self, new_cap):
        """
        RESIZE INTERNAL ARRAY TO CAPACITY new_cap
        """
        B = self.make_array(new_cap)  # new bigger array

        for k in range(self.n):
            B[k] = self.A[k]  # reference all existing values

        self.A = B  # call A the new bigger array
        self.capacity = new_cap  # reset the capacity

    def make_array(self, new_cap):
        """
        RETURNS A NEW ARRAY WITH new_cap CAPACITY
        """
        return (new_cap * ctypes.py_object)()

arr = DynamicArray()

arr.append('first')

print(f"The length array is {len(arr)} and the size of array is: {sys.getsizeof(arr)}")

for i in range(1000):
    arr.append(''.join([choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)') for i in range(32)]))

print(f"The length array is {len(arr)} and the size of array is: {sys.getsizeof(arr)}")
