# Sintetizador

# SE INCLUYE SECCIÓN DE PERCUSIÓN PARA ACOMPAÑAR MIENTRAS SE COMPONE

from music import *
 
repetitions = 4     

 
##### define the data structure
score = Score("Rhythm Section Pattern", 90.0)
 
# Drum Part (Channel 9)
drumsPart = Part("Drums", 0, 9)
bassDrumPhrase = Phrase(0.0)
snareDrumPhrase = Phrase(0.0)
hiHatPhrase = Phrase(0.0)

# Bass Part (Channel 1, Acoustic Bass)
bassPart = Part("Synth", SYNTH_BRASS2, 1)
bassPhrase = Phrase(0.0)
 
##### create musical data
 
# bass drum pattern
bassPitches   = [BDR, BDR, BDR, BDR] * 8          # El bombo nunca cambia
bassDurations = [QN, QN, QN, QN] * 8
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

 #hi-hat pattern 2                           # Patrón de hihat para coro
hiHatPitchesIntro   = [CHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, OHH, CHH, CHH, OHH, CHH] * 4
hiHatDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
hiHatPhrase.addNoteList(hiHatPitchesIntro, hiHatDurationsIntro)

# hi-hat pattern
hiHatPitches   = [CHH] * 16                  # Patrón de hihat para versos
hiHatDurations = [SN] * 16
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

# Synth line pattern intro
SynthPitchesIntro   = [F2, REST, REST, F2, REST, REST, F2, REST, REST, F2, REST, REST, F2, REST, 44 ,REST] * 4  # Patrón del synth para intro y outro
SynthDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
bassPhrase.addNoteList(SynthPitchesIntro, SynthDurationsIntro)

# Synth line pattern verse
SynthPitches1 = [F2, F2, F2, F2, F2, F2, 44, 44] * 4         # Patrón del synth para versos
SynthDurations1 = [SN, SN, SN, SN, SN, SN, SN, SN] * 4
bassPhrase.addNoteList(SynthPitches1, SynthDurations1) 

SynthPitches2 = [G2, G2, G2, G2, G2, G2, 46, 46] * 4
SynthDurations2 = [SN, SN, SN, SN, SN, SN, SN, SN] * 4
bassPhrase.addNoteList(SynthPitches2, SynthDurations2) 

##### repeat material as needed
Mod.repeat(bassDrumPhrase, repetitions)
Mod.repeat(hiHatPhrase, repetitions)
Mod.repeat(bassPhrase, repetitions)
 
##### combine musical material
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(hiHatPhrase)

bassPart.addPhrase(bassPhrase)

score.addPart(drumsPart)
score.addPart(bassPart)
 
##### view, play, and write to file
# View.sketch(score)
Play.midi(score)
# Write.midi(score, "mi_beat.mid")