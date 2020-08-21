# SpikeSorting
## Table of contents
* [General](#general)
* [Packages Used](#packages-used)
* [Independent Files](#independent-files)
* [Useful Resources](#useful-resources)

## General:
This repository contains everything we used to spikesort and analyse 2 channel ephys data recorded from bushcrickets.
	
## Folders
# /raw:
Folder containing raw files in Axon Binary Format, converted to Raw Binary Format, and prelimnay plots of the raw files. The plots show both --  recording and stimulus channels.
* Folder ```May-29``` : has subfolders ```recordings``` , ```rec_raw``` & ```unpanned plots``` 
* Folder ```July-19```: has subfolders ```recordings```, ```rec_raw``` and ```unpanned plots```

# /scripts:
Folder containing scripts used for file format conversion and sorting. 
	
## Packages used:
* [Spikeinterface (Henning Lab)](https://spikeinterface.readthedocs.io/)
* [MountainSort (Flatiron Institute)](https://github.com/flatironinstitute/mountainsort)
* [Neo (Neural Ensemble)](https://github.com/NeuralEnsemble/python-neo)
* [pyABF](https://swharden.com/pyabf)
* [matplotlib](https://matplotlib.org/)


## Useful Resources:
* [Naming scheme for raw files](https://docs.google.com/spreadsheets/d/1r-4rFreTUCHqioMG2dXIZKBZa0XNR_jEsXBSWfY0yk8/edit?usp=sharing)
* [pyABF tutorial](https://swharden.com/pyabf/tutorial#plot-a-sweep-with-matplotlib)
* [Spikeinterface documentation](https://spikeinterface.readthedocs.io/en/latest/)
* [Installing Anaconda for macOS](https://docs.anaconda.com/anaconda/install/mac-os/) Useful environment plus loads of free tools available!
