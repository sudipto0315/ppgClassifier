import matplotlib.pyplot as plt

def visualize(segId, df, parsedSignals, processor):
    raw=parsedSignals[segId]
    filt=processor.bandpassFilter(raw)
    label=df[df['id']==segId]['label'].values[0]
    plt.figure(figsize=(10,4))
    plt.plot(raw,label='Raw Signal',alpha=0.5,color='gray')
    plt.plot(filt,label='Filtered Signal (0.5-8Hz)',color='red',linewidth=1.5)
    plt.title(f"ID:{segId} Label:{label}")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()