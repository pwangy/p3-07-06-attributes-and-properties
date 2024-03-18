#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Snoopy', breed='Beagle'):
        self.name = name
        self.breed = breed

    # @property
    # def name(self):
    def get_name(self):
        return self._name

    # @name.setter
    # def name(self, name):
    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if not breed in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    breed = property(get_breed, set_breed)
