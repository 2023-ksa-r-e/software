import time
import matplotlib

import mne

raw_data = mne.io.read_raw_brainvision("./test_2.vhdr")
print(raw_data.info)

plotted = raw_data.plot(duration=200, n_channels=31)
plotted.savefig('fig.png')
