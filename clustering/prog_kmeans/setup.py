import glob
from distutils.core import setup
import platform

if platform.system() == "Linux":
    label_reassignment_so = glob.glob("label_reassignment_cpp")[0]
else:
    label_reassignment_so = glob.glob('label_reassignment_cpp*.so')[0]

setup(
    name='prog_kmeans',
    version=0.1,
    packages=[''],
    package_dir={'': '.'},
    package_data={'': [label_reassignment_so]},
    py_modules=['label_reassignment_cpp', 'prog_kmeans'])
