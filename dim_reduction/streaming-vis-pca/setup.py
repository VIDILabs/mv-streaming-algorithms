import glob
from distutils.core import setup
import platform

if len(glob.glob('inc_pca_cpp*.so')) == 0:
    raise ValueError(
        'inc_pca_cpp*.so is not found. You have not finished \
        compiling related cpp hpp files or \'python3-config --extension-suffix\'\
        command does not work properly in your environment')
inc_pca_cpp_so = glob.glob('inc_pca_cpp*.so')[0]

setup(
    name='inc-pca',
    version=0.1,
    packages=[''],
    package_dir={'': '.'},
    package_data={'': [inc_pca_cpp_so]},
    py_modules = ['inc_pca_cpp', 'inc_pca']
)
