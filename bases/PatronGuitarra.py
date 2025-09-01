# Patrón guitarra eléctrica

# Composición original para AI Song Contest

# SE INCLUYE SECCIÓN DE PERCUSIÓN PARA ACOMPAÑAR MIENTRAS SE COMPONE - BORRAR ANTES DE UNIR

from music import *
 
repetitions = 4     

##### define the data structure
score = Score("Rhythm Section Pattern", 90.0)
 
# Drum Part (Channel 9)
drumsPart = Part("Drums", 0, 9)
bassDrumPhrase = Phrase(0.0)
snareDrumPhrase = Phrase(0.0)
hiHatPhrase = Phrase(0.0)

# Guitar Part (Channel 2, Electric Guitar)
GuitarPart = Part("Guitar", 30, 1)
GuitarPhrase = Phrase(0.0)

# bass drum pattern
bassPitches   = [BDR, BDR, BDR, BDR] * 8          # El bombo nunca cambia
bassDurations = [QN, QN, QN, QN] * 8
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

# hi-hat pattern 2                           # Patrón de hihat para coro
hiHatPitches   = [CHH, OHH] * 16
hiHatDurations = [EN, EN] * 16
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

# hi-hat pattern
hiHatPitches   = [CHH] * 16                  # Patrón de hihat para versos
hiHatDurations = [SN] * 16
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

# Guitar line pattern verse
GuitarPitches1 = [F2, F2, 44, G2, E2, E2, REST, E2, E2] * 2
GuitarDurations1 = [WN, WN, WN, HN, QN, EN, SN, 0.125,0.125] * 2
GuitarPhrase.addNoteList(GuitarPitches1, GuitarDurations1) 

GuitarPitches2 = [F2, F2, F2, F2, F2, F2, F2, F2, 44, 44, 44, 44, 44, 44, 44, 44, G2, G2, G2, G2, G2, G2, G2, G2, E2, E2, E2, E2, E2, E2, E2, E2 ] * 4         # Patrón de guitarra para coros
GuitarDurations2 = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
GuitarPhrase.addNoteList(GuitarPitches2, GuitarDurations2) 

##### repeat material as needed
Mod.repeat(bassDrumPhrase, repetitions)
Mod.repeat(hiHatPhrase, repetitions)
Mod.repeat(GuitarPhrase, repetitions)
 
##### combine musical material
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(hiHatPhrase)

GuitarPart.addPhrase(GuitarPhrase)

# score.addPart(drumsPart)
score.addPart(GuitarPart)

 
##### view, play, and write to file
# View.sketch(score)
Play.midi(score)
# Write.midi(score, "mi_beat.mid")