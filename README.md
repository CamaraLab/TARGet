# TARGet

TARGet is a light-weight application for reconstructing non-vertical 
evolutionary histories from sampled genetic sequences. It makes use 
of persistent homology, a tool from topological data analisys, 
to infer information about the minimal set of reticulate events 
(recombination, re-assortment, etc) that are needed to explain a 
sequence alignment, under the assumption of no convergent evolution. 

It requires the following free software in the system:

- Python 2.7 (Python 3 is currently not supported.)

- CMake

- Boost C++ libraries, including Boost.Python

- NetworkX package for Python.

For optimal visualization results it is recommended to have Graphviz 
tools and PyGraphviz installed, although they are not strictly required.

Once the above dependences are installed in the system, unpack and 
build TARGet by typing the following commands in a terminal:

`tar -xvzf TARGet.tar.gz`

`cd TARGet`

`mkdir build`

`cd build`

`cmake ..`

`make`

* On Mac OSX, CMake often has issues finding the correct python path. 
If that is the case, uncomment the following three lines in file 
`CMakeLists.txt`, replacing the directories for the appropriate ones 
in your system,

`set        (PYTHON_EXECUTABLE /usr/local/bin/python2.6)`

`set        (PYTHON_INCLUDE_DIR /usr/local/include/python2.6)`

`set        (PYTHON_PATH /usr/local/lib/libpython2.6.dylib)`

and run cmake and make again.

* Some compiler versions may raise the following error:

`error: unrecognized command line option "-ftemplate-depth=256"`

If that is the case, replace the following line in `CMakeList.txt`,

`add_definitions             (-ftemplate-depth=256)`

by,

`add_definitions             (-ftemplate-depth-256)`

and run cmake and make again.

* It is important to run TARGet using the same version of Python that 
was used to compile TARGet and Boost libraries.

TARGet executable is in directory TARGet. You can check that TARGet 
has been correctly installed by running it on any of the test or the 
example FASTA files that come with the distribution, e.g.:

`./TARGet test.fa`

or

`python TARGet test.fa`

A detailed description of TARGet is found in the file `docs/Manual.pdf`.

TARGet is distributed under the GNU General Public License (GPL v3). A
copy of license is included in the file `Copying.txt`. 

This program heavily relies on [Dmitriy Morozov's Dionysus C++ library](http://www.mrzv.org/software/dionysus/) for persistent homology 
computations, the relevant parts of which are distributed together 
with TARGet also under the terms of GPLv3 license.

If you use TARGet in your research, please include in your reference 
list the following publication:

##### Camara, P.G., Levine, A.J. and Rabadan, R. (2015), "Inference of ancestral recombination graphs through topological data analysis". _In preparation_.
