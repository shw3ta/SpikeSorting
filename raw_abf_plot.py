import pyabf
import matplotlib.pyplot as plt

f = pyabf.ABF("<filename>.abf")							#load file
fig = plt.figure(figsize = (8,6))						#to plot

#plotting multichannel abfs: 
#here, we have 2 channels (indexed from 0)

f.setSweep(sweepNumber = 0, channel = 0)				#channel 1
plt.plot(f.sweepX, f.sweepY, label = "Channel 1 [mV]")
f.setSweep(sweepNumber = 0, channel = 1)				#channel 2
plt.plot(f.sweepX, f.sweepY, label = "Channel 2 [V]")

plt.ylabel(f.sweepLabelY)
plt.xlabel(f.sweepLabelX)
plt.legend()
plt.show()												#shows final result
