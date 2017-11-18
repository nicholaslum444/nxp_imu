#!/usr/bin/env python

from __future__ import division, print_function
from nxp_imu import IMU
import time

imu = IMU(gs=4, dps=2000, verbose=True)
header = 67
print('-'*header)
print("| {:17} | {:20} | {:20} |".format("Accels [g's]", " Magnet [uT]", "Gyros [dps]"))
print('-'*header)
for _ in range(10000):
        a, m, g = imu.get()
        print('| {:>5.2f} {:>5.2f} {:>5.2f} | {:>6.1f} {:>6.1f} {:>6.1f} | {:>6.1f} {:>6.1f} {:>6.1f} |'.format(a[0], a[1], a[2], m[0], m[1], m[2], g[0], g[1], g[2]))
	r, p, y = imu.getOrientation(accel=a, mag=m)
#	print('| {:>5.2f} {:>5.2f} {:>5.2f} {:>5.2f}|'.format(y, p, r, y))
        time.sleep(0.10)
print('-'*header)
print(' uT: micro Tesla')
print('  g: gravity')
print('dps: degrees per second')
print('')
