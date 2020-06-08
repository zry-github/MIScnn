#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2020 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
#External libraries
import unittest
import tempfile
import numpy as np
import nibabel as nib
#Internal libraries
from miscnn.data_loading.interfaces import NIFTI_interface

#-----------------------------------------------------#
#             Unittest: Data IO Interfaces            #
#-----------------------------------------------------#
class IO_interfaces(unittest.TestCase):
    # Create random imaging and segmentation data
    @classmethod
    def setUpClass(self):
        # Create image and segmentation
        np.random.seed(1234)
        data = np.random.rand(16, 16, 16) * 255
        data = data.astype(int)
        # Initialize temporary directory
        self.tmp_dir = tempfile.TemporaryDirectory() as tmpdirname
        self.tmp_nifti = tempfile.NamedTemporaryFile(prefix="tmp.miscnn.",
                                                     suffix=".nii")
        # Write image and segmentation to temporary files
        nib.save(nib.Nifti1Image(data, None), self.tmp_nifti.name)

    #-------------------------------------------------#
    #                 NIfTI Interface                 #
    #-------------------------------------------------#
    # Class Creation
    def test_NIFTI_creation(self):
        interface = NIFTI_interface()
    # Initialization
    def test_NIFTI_initialize(self):
        interface = NIFTI_interface()
        sample_list = interface.initialize(".")
    # Loading Images and Segmentations
    def test_NIFTI_loading(self):
        interface = NIFTI_interface()
    # NIFTI_interface - Loading and Storage of Predictions
    def test_NIFTI_predictionhandling(self):
        interface = NIFTI_interface()

    # Initialize Data IO interface: NIFTI_interface
    def test_debug(self):
        self.assertEqual(0 % 2, 0)


    # Delete all temporary files
    @classmethod
    def tearDownClass(self):
        self.tmp_nifti.close()


# # Initialize Data IO Interface for NIfTI data
# interface = NIFTI_interface(channels=1, classes=3)
#
# # Create Data IO object to load and write samples in the file structure
# data_io = Data_IO(interface, path_data, delete_batchDir=True)
#
# # Access all available samples in our file structure
# sample_list = data_io.get_indiceslist()
# sample_list.sort()
#
# # Print out the sample list
# print("Sample list:", sample_list)
#
# # Now let's load each sample and obtain collect diverse information from them
# sample_data = {}
# for index in tqdm(sample_list):
#     # Sample loading
#     sample = data_io.sample_loader(index, load_seg=True)
#     # Create an empty list for the current asmple in our data dictionary
#     sample_data[index] = []
#     # Store the volume shape
#     sample_data[index].append(sample.img_data.shape)
#     # Identify minimum and maximum volume intensity
#     sample_data[index].append(sample.img_data.min())
#     sample_data[index].append(sample.img_data.max())
#     # Store voxel spacing
#     sample_data[index].append(sample.details["spacing"])
#     # Identify and store class distribution
#     unique_data, unique_counts = np.unique(sample.seg_data, return_counts=True)
#     class_freq = unique_counts / np.sum(unique_counts)
#     class_freq = np.around(class_freq, decimals=6)
#     sample_data[index].append(tuple(class_freq))

    #

if __name__ == '__main__':
    unittest.main()
