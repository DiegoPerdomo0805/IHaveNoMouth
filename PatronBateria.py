# Patrón de batería
# Composición original para AI Song Contest

from music import *
 
repetitions = 4      # times to repeat drum pattern
 
##### define the data structure
score = Score("Rhythm Section Pattern", 80.0) # tempo is 80 bpm
 
# Drum Part (Channel 9)
drumsPart = Part("Drums", 0, 9)
bassDrumPhrase = Phrase(0.0)
snareDrumPhrase = Phrase(0.0)
hiHatPhrase = Phrase(0.0)

##### create musical data
 
# bass drum pattern
bassPitches   = [BDR, BDR, BDR, BDR] * 32
bassDurations = [QN, QN, SN, SN] * 32
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

bassPitches2   = [BDR, BDR, BDR, BDR] * 16
bassDurations2 = [0.125, 0.125, 0.125, 0.125] * 16
bassDrumPhrase.addNoteList(bassPitches2, bassDurations2)
 
# snare drum pattern
snarePitches   = [SNR, SNR] * 8
snareDurations = [QN,   QN] * 8
snareDrumPhrase.addNoteList(snarePitches, snareDurations)

snarePitches2   = [SNR, SNR, SNR, SNR] * 4
snareDurations2 = [EN, EN, EN, EN] * 4
snareDrumPhrase.addNoteList(snarePitches2, snareDurations2)

snarePitches3 = [REST, SNR, REST] * 4
snareDurations3 = [HN, QN,QN] * 4
snareDrumPhrase.addNoteList(snarePitches3, snareDurations3)
 
# hi-hat pattern
hiHatPitches   = [CHH] * 64
hiHatDurations = [EN] * 64
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

##### repeat material as needed
Mod.repeat(bassDrumPhrase, repetitions)
Mod.repeat(snareDrumPhrase, repetitions)
Mod.repeat(hiHatPhrase, repetitions+1)

##### combine musical material
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(snareDrumPhrase)
drumsPart.addPhrase(hiHatPhrase)

score.addPart(drumsPart)

diegocervantescc@gmail.com