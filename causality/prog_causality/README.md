## Python Module for Causality Analysis

### Offline and Progressive Causality Analysis

Here, several popular offline causality analysis methods are implemented in causality.py.
- vector autoregression (VAR): modeling multivariate time-series to use analysis methods below
- Granger causality test: testing Granger causality between variables
- impulse response function: measure how sensitively respond other variables when one variable causes changes
- variance decomposition: measure how sensitively respond other variables when one variable causes unexpected changes

In addition to the methods above, for streaming or progressive analysis, a progressive usage of VAR modeling is also supported.
- adaptive, progressive VAR: VAR using only a limited number of time points which can be finished calculation around an indicated latency.   

-----

Requirements
-----
* Python3, Numpy, statsmodels

* Note: Tested on macOS Mojave and Ubuntu 18.0.4 LTS.

Setup
-----
#### Mac OS with Homebrew
* Install libraries

    `brew install python3`

    `pip3 install numpy`

    `pip3 install statsmodels`

* If you want to run sample.py in this directory. You need to install additional libraries.

    `pip3 install pandas`

    Also, ProgIncPCA needs to be setup. See ../dim_reduction/ProgIncPCA/README.md for this procedure. Place prog_inc_pca.py and shared library (prog_inc_pca_cpp.xxx.so) in the same directory with sample.py.

* Install the modules with pip3.

    `pip3 install .`

#### Linux (tested on Ubuntu 18.0.4 LTS)
* Install libraries

    `sudo apt update`

    `sudo apt install python3-pip python3-dev`

    `pip3 install numpy`

* If you want to run sample.py in this directory. You need to install additional libraries.

    `pip3 install pandas`

    Also, ProgIncPCA needs to be setup. See ../dim_reduction/ProgIncPCA/README.md for this procedure. Place prog_inc_pca.py and shared library (prog_inc_pca_cpp.xxx.so) in the same directory with sample.py.

* Install the modules with pip3.

    `pip3 install .`


Usage
-----
* With Python3
    * Import the installed module from python (e.g., `from prog_causality import ProgCausality`). See sample.py for examples.

******

## How to Cite
Please, cite:    
Suraj P. Kesavan, Takanori Fujiwara, Jianping Kelvin Li, Caitlin Ross, Misbah Mubarak, Christopher D. Carothers, Robert B. Ross, and Kwan-Liu Ma, "A Visual Analytics Framework for Reviewing Streaming Performance Data".
In Proceedings of of IEEE Pacific Visualization Symposium (PacificVis), forthcoming.
