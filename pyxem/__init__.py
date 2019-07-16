# -*- coding: utf-8 -*-
# Copyright 2017-2019 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.


import glob
import logging
import os
import warnings

from hyperspy.io import load as hyperspyload
from hyperspy.api import roi
from pyxem.signals import push_metadata_through

import numpy as np

from natsort import natsorted

from .components.diffraction_component import ElectronDiffractionForwardModel

from .generators.diffraction_generator import DiffractionGenerator
from .generators.library_generator import DiffractionLibraryGenerator
from .generators.library_generator import VectorLibraryGenerator
from .generators.calibration_generator import CalibrationGenerator

from .signals.diffraction1D import Diffraction1D
from .signals.diffraction2D import Diffraction2D
from .signals.diffraction_profile import ElectronDiffraction1D
from .signals.electron_diffraction import ElectronDiffraction2D

from .signals.crystallographic_map import CrystallographicMap
from .signals.diffraction_simulation import DiffractionSimulation
from .signals.diffraction_vectors import DiffractionVectors
from .signals.indexation_results import TemplateMatchingResults
from .signals.vdf_image import VDFImage

from .io_plugins import io_plugins, default_write_ext
from .io_plugins import mib as mib_reader
from pyxem.utils.io_utils import load,load_mib


_logger = logging.getLogger(__name__)
