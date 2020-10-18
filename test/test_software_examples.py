import c3d
import importlib
import io
import os
import unittest
import numpy as np
from test.base import Base
from test.zipload import Zipload

class SoftwareExampleReadTest():
    ''' Base class testing if a set of pre-defined files can be read with plausible values.
    '''

    def test_a_read(self):

        print('----------------------------')
        print(type(self))
        print('----------------------------')

        for folder, files in self.zip_files:

            print('{} | Validating...'.format(folder))

            for file in files:
                file_path = '{}/{}'.format(folder, file)
                reader = c3d.Reader(Zipload._get(self.ZIP, file_path))
                self._log(reader)

                Base.check_data_in_range(reader, file_path, -1e6, 1e6)

            print('{} | READ: OK'.format(folder))



class Sample00(SoftwareExampleReadTest, Base):
    ZIP = 'sample00.zip'


    zip_files = \
            [
             ('Advanced Realtime Tracking GmbH', ['arthuman-sample.c3d', 'arthuman-sample-fingers.c3d']),
             ('Codamotion', ['codamotion_gaitwands_19970212.c3d', 'codamotion_gaitwands_20150204.c3d']),
             ('Cometa Systems', ['EMG Data Cometa.c3d']),
             ('Innovative Sports Training', ['Gait with EMG.c3d', 'Static Pose.c3d']),
             ('Motion Analysis Corporation', ['Sample_Jump2.c3d', 'Walk1.c3d']),
             ('NexGen Ergonomics', ['test1.c3d']),
             ('Vicon Motion Systems', ['TableTennis.c3d']),
             # Vicon files are weird, uses non-standard encodings. Walking01.c3d contain nan values and is not tested.
             #('Vicon Motion Systems', ['pyCGM2 lower limb CGM24 Walking01.c3d', 'TableTennis.c3d']),
            ]


if __name__ == '__main__':
    unittest.main()
