# Sintetizador

# SECCIÓN AÚN NO TERMINADA

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
bassPitches   = [BDR, BDR, BDR, BDR] * 32          # El bombo nunca cambia
bassDurations = [QN, QN, QN, QN] * 32
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

# hi-hat pattern 2                           # Patrón de hihat para coro
#hiHatPitchesIntro   = [CHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, OHH, CHH, CHH, OHH, CHH] * 4
#hiHatDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
#hiHatPhrase.addNoteList(hiHatPitchesIntro, hiHatDurationsIntro)

# hi-hat pattern
hiHatPitches   = [CHH] * 64                  # Patrón de hihat para versos
hiHatDurations = [SN] * 64
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

# bass line pattern (follows the kick drum for now)
bassLinePitches   = [B1, B1] * 8
bassLineDurations = [SN, SN] * 8
bassPhrase.addNoteList(bassLinePitches, bassLineDurations)

# bass line pattern 2
bassLinePitches2   = [G1, G1] * 8
bassLineDurations2 = [SN, SN] * 8
bassPhrase.addNoteList(bassLinePitches2, bassLineDurations2) 

bassLinePitches3   = [E1, E1] * 8
bassLineDurations3 = [SN, SN] * 8
bassPhrase.addNoteList(bassLinePitches3, bassLineDurations3) 

bassLinePitches5 = [C2, C2, C2, C2, C2, C2, B1, B1] * 8
bassLineDurations5 = [SN, SN, SN, SN, SN, SN, SN, SN] * 8
bassPhrase.addNoteList(bassLinePitches5, bassLineDurations5) 

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