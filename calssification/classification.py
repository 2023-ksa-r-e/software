import time
import matplotlib
matplotlib.use('TkAgg')
import mne as mne

raw_data = mne.io.read_raw_brainvision("./test_2.vhdr")
ch_names = raw_data.ch_names
print(ch_names)
easycap_montage = mne.channels.make_standard_montage('easycap-M10')
easycap_montage.plot()