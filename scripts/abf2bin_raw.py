import numpy as np 
import neo

for i in range(1, 27):
	#names of i/o files
	f_in = str(i)+".abf"
	f_out = str(i)+".raw"

	reader = neo.io.AxonIO(filename = f_in)
	writer = neo.io.RawBinarySignalIO(f_out, dtype = 'float32', sampling_rate = 10000.0, nb_channel = 2)

	block = reader.read_block(lazy = False)
	writer.write(block)
	
