'''
sorts one raw file at a time
will implement threshold selection after further discussion
'''

import matplotlib.pyplot as plt 
import numpy as np 
import neo
import spikeinterface.extractors as se
import spikeinterface.sorters as ss 
import spikeinterface.toolkit as st 
import spikeinterface.widgets as sw
import warnings
warnings.filterwarnings("ignore")


print("This program spike sorts and plots a signal that has been sorted with 4 different amplitude thresholds.\n")
filename = str(input("Enter filename below : "))

if '.abf' in filename:
	print("Convert file error; Make sure file is in '.raw' format.")
	exit()


r = neo.io.RawBinarySignalIO(filename, dtype = 'float32')
sampling_rate = r.get_signal_sampling_rate()
units = r.header['signal_channels']['units']

#useful details
seg 			= r.read_block().segments[0]
asig 			= seg.analogsignals[0] 					#only channel with neural signal
times 			= asig.times.rescale('s').magnitude
signal 			= asig.magnitude
n_chan 			= 2										#ch0 - 'mV'; ch1 - 'V'
duration 		= len(times)/sampling_rate
n_timepoints 	= len(times)

data = np.array(asig.T)
recording = se.NumpyRecordingExtractor(timeseries = data, sampling_frequency = sampling_rate)

#bandpass filtering
recording_bpf =  st.preprocessing.bandpass_filter(recording = recording, freq_min = 300, freq_max = 2000)


default_params_sorter = ss.Mountainsort4Sorter.default_params()
default_params_sorter['curation'] = False

fig = plt.figure()
sort_list, wf_list = [],[]
threshold = [4,5,6,7]
for i in range(4):
	
	default_params_sorter['detect_threshold'] = i+4
	sorting = ss.run_mountainsort4(recording= recording_bpf, **default_params_sorter)
	sort_list.append(sorting)
	wf = st.postprocessing.get_unit_waveforms(recording_bpf, 
											  sorting, 
											  unit_ids = 1, 
											  channel_ids = 0, 
											  save_as_features = True, 
											  verbose = True)

	wf_list.append(wf)

for i in range(8):
	if i == 0:
		ax = fig.add_subplot(4,2,i+1)
		ax.eventplot(sort_list.pop(0).get_unit_spike_train(1), linelengths=0.2,colors = f'C{i}', label = f'thr: {threshold.pop(0)}' )
	elif i == 1:
		ax_ = fig.add_subplot(4,2,i+1)
		ax_.plot(wf_list.pop(0)[0][:, 0, :].T, color='b', lw=0.3)


	else:
		if i%2 ==0:
			ax1 = fig.add_subplot(4,2,i+1,sharex = ax)
			ax1.eventplot(sort_list.pop(0).get_unit_spike_train(1), linelengths=0.2,colors = f'C{i}', label = f'thr: {threshold.pop(0)}' )
		else:
			ax1 = fig.add_subplot(4,2,i+1, sharex = ax_)
			ax1.plot(wf_list.pop(0)[0][:, 0, :].T, color='b', lw=0.3)


fig.legend()
plt.show()