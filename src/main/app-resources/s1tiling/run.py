#!/opt/anaconda/bin/python

import sys
import os
import lxml.etree as et
import shutil
import tarfile
import atexit
import fnmatch
import glob 
import numpy as np
from string import Template

filein = open( 'S1Processor.template' )
#read it
src = Template( filein.read() )

path_to_srtm = '/pippo/lixo/SRTM'
path_to_geoid = ''
calibration = ''
spatial_resolution = ''
tiles_shapefile = ''
srtmshapefile = ''
grid_spacing = ''
border_threshold = ''
tiles = ''
overlap_ratio = ''
log_level = ''
processes = ''
ram_process = ''
filtering = ''
window_radius = ''

d = { 'path_to_srtm':path_to_srtm,
      'path_to_geoid':path_to_geoid,
      'calibration': calibration,
      'spatial_resolution':spatial_resolution,
      'tiles_shapefile': tiles_shapefile,
      'srtmshapefile': srtmshapefile,
      'grid_spacing': grid_spacing,
      'border_threshold': border_threshold,
      'tiles': tiles,
      'overlap_ratio': overlap_ratio,
      'log_level': log_level,
      'processes': processes,
      'ram_process': ram_process,
      'filtering': filtering,
      'window_radius': window_radius }

result = src.substitute(d)

text_file = open("Output.txt", "w")
text_file.write(result)
text_file.close()
