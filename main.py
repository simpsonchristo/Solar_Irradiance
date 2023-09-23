"""Python 3.9
   Simpson Aerospace (c) 2023
   Dr. Christopher R. Simpson: christopher.r.simpson@simpsonaerospace.com"""

import numpy as np

def irrad(low_wav, high_wav, T_bb):
    #IRRAD calculate radiant flux of the blackbody over some wavelength interval
    h = 6.63E-34 #J-s, Planck's constant
    k = 1.38E-23 #J/K, Boltzmann's constant
    c = 299790000 #m/s, speed of light
    dwav = (high_wav - low_wav)/50
    E_wav = []
    current_wav = low_wav
    for i in range(50):
        E_wav.append(dwav*(2 * np.pi * h * c ** 2) / ((current_wav**5)*(np.exp(h*c/(current_wav*k*T_bb))-1)))
        current_wav = low_wav + i*dwav
    return np.trapz(E_wav)


if __name__ == '__main__':
    # print_hi('PyCharm')
    E_rad_sun = irrad(400E-9, 1100E-9, 5738)
    r_eq_sun = 696000000 #m, equatorial radius of sun
    r_AU = 149597870700 #m, exact def of 1 AU
    E_irrad = E_rad_sun*(r_eq_sun**2 / r_AU**2)

