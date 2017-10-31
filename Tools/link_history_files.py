#!/usr/bin/env python

import os

# link the b.e20.BHIST.f09_g17.20thC.216_01 lnd monthly history files
for year in ['1860','1861','1862','1863','1864','1865','1866','1867','1868','1869','1870']:
    for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        
        srcdir = '/glade/p/cesm0005/archive/b.e20.BHIST.f09_g17.20thC.216_01/lnd/hist'
        linkdir = '/glade/scratch/aliceb/b.e20.BHIST.f09_g17.20thC.216_01/lnd/hist'

        if not os.path.exists(linkdir):
            os.makedirs(linkdir)

        casename = 'b.e20.BHIST.f09_g17.20thC.216_01.clm2.h0'
        filename = '{0}.{1}-{2}.nc'.format(casename,year,month)
        os.symlink(os.path.join(srcdir, filename), os.path.join(linkdir, filename))

# link the b.e20.BHIST.f09_g17.20thC.216_01 rof monthly history files
for year in ['1860','1861','1862','1863','1864','1865','1866','1867','1868','1869','1870']:
    for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        
        srcdir = '/glade/p/cesm0005/archive/b.e20.BHIST.f09_g17.20thC.216_01/rof/hist'
        linkdir = '/glade/scratch/aliceb/b.e20.BHIST.f09_g17.20thC.216_01/rof/hist'

        if not os.path.exists(linkdir):
            os.makedirs(linkdir)

        casename = 'b.e20.BHIST.f09_g17.20thC.216_01.mosart.h0'
        filename = '{0}.{1}-{2}.nc'.format(casename,year,month)
        os.symlink(os.path.join(srcdir, filename), os.path.join(linkdir, filename))

