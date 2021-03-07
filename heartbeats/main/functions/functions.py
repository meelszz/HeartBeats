from music21 import tempo, note, stream
import pandas as pd

def handle_uploaded_file(file):
    #df = file.read()
    df = pd.read_csv(file)
    heart_rate = df["Heart Rate"].tolist()
    heart_rate_sample = heart_rate[:5]
    min = 0
    max = 500
    period = 50
    s = stream.Stream()
    for i in heart_rate_sample:
    #scalar = (math.sin(i * (math.pi*2) / period) + 1) * .5
    #n = ((max-min) * scalar) + min
        s.append(tempo.MetronomeMark(number=i))
        s.append(note.Note('c'))
    #s.show('midi')
 
    #mf1 = music21.midi.translate.streamToMidiFile(sBach)
    fp = s.write('midi', fp='heartbeats\main\static\hbeats.mid')

    
