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
bassPitches   = [BDR, BDR, BDR, BDR] * 32          # El bombo nunca cambia
bassDurations = [QN, QN, QN, QN] * 32
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

# snare drum pattern  
snarePitches   = [REST, SNR, REST, SNR, SNR, REST, REST, SNR, REST, SNR, REST, SNR] * 2
snareDurations = [QN, QN, QN, SN, SN, EN, QN, QN, SN, SN, EN, QN] * 2
snareDrumPhrase.addNoteList(snarePitches, snareDurations)

# Compases individuales del patrón anterior de redoblante, por si se necesitara 

# snare drum pattern
#snarePitches   = [REST, SNR, REST, SNR, SNR, REST] * 4  
#snareDurations = [QN,   QN, QN, SN, SN, EN] * 4
#snareDrumPhrase.addNoteList(snarePitches, snareDurations)

# snare drum pattern 2
#snarePitches2   = [REST, SNR, REST, SNR, REST, SNR] * 4
#snareDurations2 = [QN, QN, SN, SN, EN, QN] * 4
#snareDrumPhrase.addNoteList(snarePitches2, snareDurations2)

# hi-hat pattern intro                           # Patrón de hihat para 4 compases introductorios con solo bombo y hihat
hiHatPitchesIntro   = [CHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, OHH, CHH, CHH, OHH, CHH] * 16
hiHatDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 16
hiHatPhrase.addNoteList(hiHatPitchesIntro, hiHatDurationsIntro) 

# hi-hat pattern
hiHatPitches   = [CHH] * 64                  # Patrón de hihat para versos
hiHatDurations = [SN] * 64
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

# hi-hat pattern 2                           # Patrón de hihat para coro
hiHatPitches   = [CHH, OHH] * 16
hiHatDurations = [EN, EN] * 16
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

Play.midi(score)
print('REPRODUCIENDO SCORE')