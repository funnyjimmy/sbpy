# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
sbpy.data
---------

:author: Michael Mommert (mommermiscience@gmail.com)
"""


class Conf():

    # acceptable field names for DataClass
    fieldnames_info = [
        # General
        {'description': 'Target Identifier',
         'fieldnames': ['targetname', 'id', 'Object'],
         'provenance': ['orbit', 'ephem', 'obs', 'phys'],
         'dimension': None},
        {'description': 'Epoch',
         'fieldnames': ['epoch', 'datetime_jd', 'JD',
                        'Date', 'date', 'Time', 'time'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'time'},

        # Orbital Elements
        {'description': 'Semi-Major Axis',
         'fieldnames': ['a', 'sma'],
         'provenance': ['orbit'],
         'dimension': 'length'},
        {'description': 'Eccentricity',
         'fieldnames': ['e', 'ecc'],
         'provenance': ['orbit'],
         'dimension': None},
        {'description': 'Inclination',
         'fieldnames': ['i', 'inc', 'incl'],
         'provenance': ['orbit'],
         'dimension': 'angle'},
        {'description': 'Longitude of the Ascending Node',
         'fieldnames': ['Omega', 'longnode', 'node'],
         'provenance': ['orbit'],
         'dimension': 'angle'},
        {'description': 'Argument of the Periapsis',
         'fieldnames': ['w', 'argper'],
         'provenance': ['orbit'],
         'dimension': 'angle'},
        {'description': 'Mean Anomaly',
         'fieldnames': ['M', 'mean anom'],
         'provenance': ['orbit'],
         'dimension': 'angle'},
        {'description': 'True Anomaly',
         'fieldnames': ['v', 'true_anom'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'angle'},

        # Ephemerides properties
        {'description': 'Heliocentric Distance',
         'fieldnames': ['r', 'rh', 'r_hel', 'heldist'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'length'},
        {'description': 'Distance to the Observer',
         'fieldnames': ['delta', 'Delta', 'obsdist'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'length'},
        {'description': 'Right Ascension',
         'fieldnames': ['ra', 'RA'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Declination',
         'fieldnames': ['dec', 'DEC'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Right Ascension Rate',
         'fieldnames': ['ra_rate', 'RA_rate', 'ra_rates', 'RA_rates',
                        'dRA', 'dra'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angular velocity'},
        {'description': 'RA*cos(Dec) Rate',
         'fieldnames': ['RA*cos(Dec)_rate', 'dra cos(dec)',
                        'dRA cos(Dec)', 'dra*cos(dec)', 'dRA*cos(Dec)'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angular velocity'},
        {'description': 'Declination Rate',
         'fieldnames': ['dec_rate', 'DEC_rate', 'Dec_rate', 'dec_rates',
                        'DEC_rates', 'Dec_rates', 'dDec', 'dDEC', 'ddec'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angular velocity'},
        {'description': 'Proper Motion',
         'fieldnames': ['mu', 'Proper motion'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angular velocity'},
        {'description': 'Proper Motion Direction',
         'fieldnames': ['Direction', 'direction'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Solar Phase Angle',
         'fieldnames': ['alpha', 'phaseangle', 'Phase'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Solar Elongation Angle',
         'fieldnames': ['elong', 'solarelong',
                        'solarelongation', 'elongation', 'Elongation'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'V-band Magnitude',
         'fieldnames': ['V', 'Vmag'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'magnitude'},
        {'description': 'Heliocentric Ecliptic Longitude',
         'fieldnames': ['hlon', 'EclLon', 'ecllon', 'HelEclLon',
                        'helecllon'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Heliocentric Ecliptic Latitude',
         'fieldnames': ['hlat', 'EclLat', 'ecllat', 'HelEclLat',
                        'helecllat'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Horizontal Elevation',
         'fieldnames': ['el', 'EL', 'elevation', 'alt', 'altitude',
                        'Altitude'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Horizontal Azimuth',
         'fieldnames': ['az', 'AZ', 'azimuth'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'Lunar Elongation',
         'fieldnames': ['lunar_elong', 'elong_moon', 'elongation_moon',
                        'lunar_elongation', 'lunarelong'],
         'provenance': ['ephem', 'obs'],
         'dimension': 'angle'},
        {'description': 'X State Vector Component',
         'fieldnames': ['x', 'X', 'x_vec'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'length'},
        {'description': 'Y State Vector Component',
         'fieldnames': ['y', 'Y', 'y_vec'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'length'},
        {'description': 'Z State Vector Component',
         'fieldnames': ['z', 'Z', 'z_vec'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'length'},
        {'description': 'X Velocity Vector Component',
         'fieldnames': ['vx', 'dx', 'dx/dt'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'velocity'},
        {'description': 'Y Velocity Vector Component',
         'fieldnames': ['vy', 'dy', 'dy/dt'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'velocity'},
        {'description': 'Z Velocity Vector Component',
         'fieldnames': ['vz', 'dz', 'dz/dt'],
         'provenance': ['orbit', 'ephem', 'obs'],
         'dimension': 'velocity'},

        # Physical properties (dependent on other properties)
        {'description': 'Infrared Beaming Parameter',
         'fieldnames': ['eta', 'Eta'],
         'provenance': ['ephem', 'obs'],
         'dimension': None},
        {'description': 'Temperature',
         'fieldnames': ['temp', 'Temp', 'temperature', 'Temperature'],
         'provenance': ['phys', 'ephem', 'obs'],
         'dimension': 'temperature'},


        # Physical properties (static)
        {'description': 'Effective Diameter',
         'fieldnames': ['d', 'D', 'diam', 'diameter', 'Diameter'],
         'provenance': ['phys'],
         'dimension': 'length'},
        {'description': 'Effective Radius',
         'fieldnames': ['R', 'radius'],
         'provenance': ['phys'],
         'dimension': 'length'},
        {'description': 'Geometric Albedo',
         'fieldnames': ['pv', 'pV', 'p_v', 'p_V', 'geomalb'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Bond Albedo',
         'fieldnames': ['A', 'bondalbedo'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Emissivity',
         'fieldnames': ['emissivity', 'Emissivity'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Molecule Identifier',
         'fieldnames': ['mol_tag', 'mol_name'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Transition frequency',
         'fieldnames': ['t_freq'],
         'provenance': ['phys'],
         'dimension': 'frequency'},
        {'description': 'Integrated line intensity at 300 K',
         'fieldnames': ['lgint300'],
         'provenance': ['phys'],
         'dimension': 'intensity'},
        {'description': 'Integrated line intensity at designated Temperature',
         'fieldnames': ['intl', 'lgint'],
         'provenance': ['phys'],
         'dimension': 'intensity'},
        {'description': 'Partition function at 300 K',
         'fieldnames': ['partfn300'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Partition function at designated temperature',
         'fieldnames': ['partfn'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Upper state degeneracy',
         'fieldnames': ['dgup'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Upper level energy in Joules',
         'fieldnames': ['eup_j', 'eup_J'],
         'provenance': ['phys'],
         'dimension': 'energy'},
        {'description': 'Lower level energy in Joules',
         'fieldnames': ['elo_j', 'elo_J'],
         'provenance': ['phys'],
         'dimension': 'energy'},
        {'description': 'Degrees of freedom',
         'fieldnames': ['degfr', 'ndf', 'degfreedom'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Einstein Coefficient',
         'fieldnames': ['au', 'eincoeff'],
         'provenance': ['phys'],
         'dimension': None},
        {'description': 'Timescale * r^2',
         'fieldnames': ['beta', 'beta_factor'],
         'provenance': ['phys'],
         'dimension': 'time'},
        {'description': 'Total Number',
         'fieldnames': ['totnum', 'total_number_nocd'],
         'provenance': ['phys'],
         'dimension': None},
        # {'description': '',
        #  'fieldnames': [],
        #  'provenance': [],
        #  'dimension': None},
    ]

    # list of fieldnames; each element a list of alternatives
    fieldnames = [prop['fieldnames'] for prop in fieldnames_info]

    fieldname_idx = {}
    for idx, field in enumerate(fieldnames):
        for alt in field:
            fieldname_idx[alt] = idx

    # field equivalencies defining conversions
    # key defines target quantity; dict with source quantity and function
    # for conversion
    # conversions considered as part of DataClass._translate_columns
    field_eq = {'R': {'d': lambda r: r/2},
                # diameter to radius}
                'd': {'R': lambda d: d*2}
                }

    # definitions for use of pyoorb in Orbits
    oorb_timeScales = {'UTC': 1, 'UT1': 2, 'TT': 3, 'TAI': 4}
    oorb_elemType = {'CART': 1, 'COM': 2, 'KEP': 3, 'DEL': 4, 'EQX': 5}

    oorb_orbit_fields = {'COM': ['id', 'q', 'e', 'incl', 'Omega',
                                 'w', 'Tp_jd', 'orbtype', 'epoch',
                                 'epoch_scale', 'H', 'G'],
                         'KEP': ['id', 'a', 'e', 'incl', 'Omega', 'w', 'M',
                                 'orbtype', 'epoch', 'epoch_scale', 'H',
                                 'G'],
                         'CART': ['id', 'x', 'y', 'z', 'vx', 'vy', 'vz',
                                  'orbtype', 'epoch', 'epoch_scale', 'H',
                                  'G']}
    oorb_orbit_units = {'COM': [None, 'au', None, 'deg', 'deg',
                                'deg', 'd', None, 'd',
                                None, 'mag', None],
                        'KEP': [None, 'au', None, 'deg', 'deg', 'deg', 'deg',
                                None, 'd', None, 'mag', None],
                        'CART': [None, 'au', 'au', 'au', 'au/d', 'au/d',
                                 'au/d', None, 'd', None, 'mag', None]}

    oorb_ephem_fields = ['MJD', 'RA', 'DEC', 'RA*cos(Dec)_rate', 'DEC_rate',
                         'alpha', 'elong', 'r', 'Delta', 'V', 'pa', 'TopEclLon',
                         'TopEclLat', 'OppTopEclLon', 'OppTopEclLat',
                         'HelEclLon', 'HelEclLat', 'OppHelEclLon',
                         'OppHelEclLat', 'EL', 'ELsun', 'ELmoon',
                         'lunarphase', 'lunarelong', 'x', 'y', 'z',
                         'vx', 'vy', 'vz', 'obsx', 'obsy', 'obsz',
                         'trueanom']
    oorb_ephem_units = ['d', 'deg', 'deg', 'deg/d', 'deg/d', 'deg',
                        'deg', 'au', 'au', 'mag', 'deg', 'deg',
                        'deg', 'deg', 'deg',
                        'deg', 'deg', 'deg',
                        'deg', 'deg', 'deg', 'deg',
                        None, 'deg', 'au', 'au', 'au',
                        'au/d', 'au/d', 'au/d', 'au', 'au', 'au', 'deg']


conf = Conf()

from .core import DataClass, DataClassError
from .ephem import Ephem
from .orbit import Orbit
from .phys import Phys
from .obs import Obs
from .names import Names, natural_sort_key

__all__ = ['DataClass', 'Ephem', 'Obs', 'Orbit', 'Phys', 'Names',
           'conf', 'Conf', 'DataClassError']
