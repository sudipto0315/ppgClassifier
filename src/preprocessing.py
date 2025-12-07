import numpy as np
import scipy.signal as signal

class PPGProcessor:
    def __init__(self,fs=100):
        self.fs=fs
    def parseSignal(self,sigStr):
        try:
            if isinstance(sigStr,str):
                return np.array([float(x) for x in sigStr.strip().split()])
            return np.zeros(800)
        except:
            return np.zeros(800)

    def bandpassFilter(self,data,lowcut=0.5,highcut=8.0,order=3):
        nyquist=0.5*self.fs
        low=lowcut/nyquist
        high=highcut/nyquist
        b,a=signal.butter(order,[low, high],btype='band')
        y=signal.filtfilt(b,a,data)
        return y

    def featureExtractor(self,cleanSig):
        features={}
        features['mean']=np.mean(cleanSig)
        features['std']=np.std(cleanSig)
        features['max']=np.max(cleanSig)
        features['min']=np.min(cleanSig)
        features['p2p']=np.ptp(cleanSig)
        features['rms']=np.sqrt(np.mean(cleanSig**2))
        features['complexity']=np.std(np.diff(cleanSig))
        return features