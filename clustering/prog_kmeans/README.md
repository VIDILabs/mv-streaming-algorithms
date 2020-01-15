## C++ Library and Python Module for Progressive MiniBatchKMeans for Visualization with Streaming time-series clustering

Progressive version of https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html.

-----

Requirements
-----
* C++11 compiler, Python3, Pybind11, Numpy

* Note: Tested on macOS Mojave and Ubuntu 18.0.4 LTS.

Setup
-----
#### Mac OS with Homebrew
* Install libraries

    `brew install python3`

    `brew install pybind11`

    `pip3 install numpy`

* Build with cmake

    `mv /path/to/directory-of-CmakeLists.txt`

    `cmake .`

    `make`

* This generates a shared library, "prog_kmeans_cpp.xxxx.so" (e.g., prog_kmeans_cpp.cpython-37m-darwin.so).

* If you want to run sample.py in this directory. You need to install additional libraries.

    `pip3 install matplotlib`

    `pip3 install pandas`

#### Linux (tested on Ubuntu 18.0.4 LTS)
* Install libraries

    `sudo apt update`

    `sudo apt install python3-pip python3-dev`

    `pip3 install pybind11`

    `pip3 install numpy`

* Move to 'prog_kmeans' directory then compile with:

    ``c++ -O3 -Wall -mtune=native -march=native -shared -std=c++11 -I../core/ -fPIC `python3 -m pybind11 --includes` ../core/core.cpp prog_kmeans.cpp prog_kmeans_wrap.cpp -o prog_kmeans_cpp`python3-config --extension-suffix` ``

* This generates a shared library, "prog_kmeans_cpp.xxxx.so" (e.g., prog_kmeans_cpp.cpython-37m-x86_64-linux-gnu.so).

* If you want to run sample.py in this directory. You need to install additional libraries.

    `sudo apt install python3-tk`

    `pip3 install matplotlib`

    `pip3 install pandas`

Usage
-----
* Place prog_kmeans_cpp.xxxx.so and prog_kmeans.py in the same directory.

* Import "prog_kmeans" from python. See prog_kmeans.py or docs/index.html for detailed usage examples.
