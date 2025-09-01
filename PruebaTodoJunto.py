from music import *
 
repetitions = 4      # times to repeat drum pattern
 
##### define the data structure
score = Score("Rhythm Section Pattern", 90.0) # tempo is 80 bpm
 
# Drum Part (Channel 9)
drumsPart = Part("Drums", 0, 9)
bassDrumPhrase = Phrase(0.0)
snareDrumPhrase = Phrase(0.0)
hiHatPhrase = Phrase(0.0)

# Synth Part (Channel 1, Bass Lead )
SynthPart = Part("Synth", 87, 1)
SynthPhrase = Phrase(0.0)

# Guitar Part (Channel 2, Electric Guitar)
GuitarPart = Part("Guitar", 30, 1)
GuitarPhrase = Phrase(8.0)

##### create musical data
 
# bass drum pattern
# 32 compases
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
hiHatPitchesIntro   = [CHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, OHH, CHH, CHH, OHH, CHH] * 4
hiHatDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
hiHatPhrase.addNoteList(hiHatPitchesIntro, hiHatDurationsIntro) 

# hi-hat pattern
hiHatPitches   = [CHH] * 16                  # Patrón de hihat para versos
hiHatDurations = [SN] * 16
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

# hi-hat pattern 2                           # Patrón de hihat para coro
hiHatPitches   = [CHH, OHH] * 16
hiHatDurations = [EN, EN] * 16
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

# Synth line pattern intro
SynthPitchesIntro   = [F2, REST, REST, F2, REST, REST, F2, REST, REST, F2, REST, REST, F2, REST, 42 ,REST] * 4  # Patrón del synth para intro y outro
SynthDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
SynthPhrase.addNoteList(SynthPitchesIntro, SynthDurationsIntro)

# Synth line pattern verse
SynthPitches1 = [F2, F2, F2, F2, F2, F2, 44, 44] * 4         # Patrón del synth para versos
SynthDurations1 = [SN, SN, SN, SN, SN, SN, SN, SN] * 4
SynthPhrase.addNoteList(SynthPitches1, SynthDurations1) 

SynthPitches2 = [G2, G2, G2, G2, G2, G2, 46, 46] * 4
SynthDurations2 = [SN, SN, SN, SN, SN, SN, SN, SN] * 4
SynthPhrase.addNoteList(SynthPitches2, SynthDurations2) 

# Guitar line pattern verse
GuitarPitches1 = [F2, F2, 44, G2, E2, E2, REST, E2, E2] * 2
GuitarDurations1 = [WN, WN, WN, HN, QN, EN, SN, 0.125,0.125] * 2
GuitarPhrase.addNoteList(GuitarPitches1, GuitarDurations1) 

GuitarPitches2 = [F2, F2, F2, F2, F2, F2, F2, F2, 44, 44, 44, 44, 44, 44, 44, 44, G2, G2, G2, G2, G2, G2, G2, G2, E2, E2, E2, E2, E2, E2, E2, E2 ] * 4         # Patrón de guitarra para coros
GuitarDurations2 = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
GuitarPhrase.addNoteList(GuitarPitches2, GuitarDurations2) 

##### repeat material as needed
Mod.repeat(bassDrumPhrase, repetitions)
Mod.repeat(snareDrumPhrase, repetitions)
Mod.repeat(hiHatPhrase, repetitions+1)

Mod.repeat(SynthPhrase, repetitions)

##### combine musical material
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(snareDrumPhrase)
drumsPart.addPhrase(hiHatPhrase)

SynthPart.addPhrase(SynthPhrase)
GuitarPart.addPhrase(GuitarPhrase)

score.addPart(drumsPart)
score.addPart(SynthPart)
score.addPart(GuitarPart)


Play.midi(score)
print('REPRODUCIENDO SCORE')