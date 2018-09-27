import pandas as pd
import os 

def get_yields(datacard, signal_1, signal_2, backgrounds, skiprows):
    data = pd.read_csv(datacard, skiprows=skiprows, nrows=2, header=0, delim_whitespace=True, index_col=0)
    return data.loc['rate'][signal_1].sum(), data.loc['rate'][signal_2].sum(), data.loc['rate'][backgrounds].sum() 
        
datacards_folder = os.path.join("/Users/dominik/cernbox/www/plots_archive/2018_08_25/2018-08-25_FULL_mela3D_new_outputs_JECgroupings/")

signal_ggH = ['ggHsm_htt', 'ggH_htt']
signal_qqH = ['qqHsm_htt125','ZH_htt125','WH_htt125' ]
backgrounds = ['ZTT', 'ZL', 'ZJ', 'TTJ', 'TTT', 'VVJ', 'W', 'QCD', 'EWKZ']

skiprows_dict = {
"em_1": 14,
"em_2": 14,
"em_3": 16,
"em_4": 16,
"et_1": 14,
"et_2": 14,
"et_3": 16,
"et_4": 16,
"mt_1": 14,
"mt_2": 14,
"mt_3": 16,
"mt_4": 16,
"tt_1": 14,
"tt_2": 14,
"tt_3": 16,
"tt_4": 16
}
channel_dict = {
"em": "e\mu",
"et": "e\tau_\mathrm{h}",
"mt": "\mu\tau_\mathrm{h}",
"tt": "\tau\mathrm{h}\tau_\mathrm{h}"
}
category_dict = {
"1": "0-jet",
"2": "boosted",
"3": "dijet lowboost",
"4": "dijet boosted"
}

df = pd.DataFrame(index = ["e\mu","e\tau_\mathrm{h}","\mu\tau_\mathrm{h}","\tau_\mathrm{h}\tau_\mathrm{h}"], columns=["0-jet","boosted", "dijet lowboost", "dijet boosted"])

for channel in ["em", "et", "mt","tt"]:
    for bin in ["1", "2", "3", "4"]:
        datacard_path = os.path.join(datacards_folder, 'htt_{CH}_{BIN}_13TeV.txt'.format(CH=channel,BIN=bin))
        ggH, qqH, bkg = get_yields(datacard_path, signal_ggH, signal_qqH, backgrounds, skiprows=skiprows_dict[str(channel)+"_"+str(bin)])
        # print("Signal_ggH: {SIG_ggH}%\t Signal_qqH: {SIG_qqH}%\t Background: {BKG}%".format(SIG_ggH=100*yield_signal_ggH/(yield_signal_ggH+yield_signal_qqH+yield_background), SIG_qqH=100*yield_signal_qqH/(yield_signal_ggH+yield_signal_qqH+yield_background), BKG=100*yield_background/(yield_signal_ggH+yield_signal_qqH+yield_background)))        
        df.loc[channel_dict[channel], category_dict[bin]] = "{GGH:.{N}f}%, {QQH:.{N}f}%, {BKG:.{N}f}%".format(GGH=100*ggH/(bkg+ggH+qqH), QQH=100*qqH/(bkg+ggH+qqH),BKG=100*bkg/(bkg+ggH+qqH), N=2) 

with open('category_purities.tex', 'w') as tf:
     tf.write(df.to_latex())
