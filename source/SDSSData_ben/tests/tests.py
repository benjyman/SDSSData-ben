#!/usr/bin/env python3

#print the RA from a spectrum

from SDSSData_ben.spectrum import Spectrum

s = Spectrum(filepath="../../../data/spec-10000-57346-0002.fits")
ra = s.ra
dec = s.dec
name = s.name

#print(f'The spectrum named {name} is at RA {ra} degrees, DEC {dec}')
#
#data = s.data
#print(data.shape)

#s.plot_spectrum()
