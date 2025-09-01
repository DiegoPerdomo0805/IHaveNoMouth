from music import *    # import music library

 
phrase_counter = 0
phrase_length = 4 * 4 # 2 compases de duración de 4

def new_phrase():
    global phrase_counter
    temp = phrase_counter * phrase_length
    phrase_counter += 1
    return float(temp)

def current_phrase():
    global phrase_counter
    temp = (phrase_counter - 1) * phrase_length
    # phrase_counter += 1
    return float(temp)


def createPhrase(phrase_list, notes, durations, position):
    p = Phrase(position)
    p.addNoteList(notes, durations)
    phrase_list.append(p)


def populatePart(part, phrase_list):
    for e in phrase_list:
        part.addPhrase(e)


#### Partes
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

### NOTAS Y DURACIONES

##### BATERÍA

# 4 compases
bassPitches   = [BDR, BDR, BDR, BDR] * 4
bassDurations = [QN, QN, QN, QN] * 4
# 4 compases
snarePitches   = [REST, SNR, REST, SNR, SNR, REST, REST, SNR, REST, SNR, REST, SNR] * 2
snareDurations = [QN, QN, QN, SN, SN, EN, QN, QN, SN, SN, EN, QN] * 2
# 4 compases
hiHatPitchesIntro   = [CHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, CHH, OHH, CHH, OHH, CHH, CHH, OHH, CHH] * 4
hiHatDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4
# 1 compas
hiHatPitchesVerse   = [CHH] * 16
hiHatDurationsVerse = [SN] * 16
# 4 compases
hiHatPitchesChorus   = [CHH, OHH] * 4 * 4
hiHatDurationsChorus = [EN, EN] * 4 * 4



##### SINTETIZADOR

# Synth line pattern intro
# 4 COMPASES
SynthPitchesIntro   = [F2, REST, REST, F2, REST, REST, F2, REST, REST, F2, REST, REST, F2, REST, 42 ,REST] * 4  # Patrón del synth para intro y outro
SynthDurationsIntro = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN] * 4

# Synth line pattern verse
# 2 COMPASES
SynthPitches1 = [F2, F2, F2, F2, F2, F2, 44, 44] * 4         # Patrón del synth para versos
SynthDurations1 = [SN, SN, SN, SN, SN, SN, SN, SN] * 4

# 2 COMPASES
SynthPitches2 = [G2, G2, G2, G2, G2, G2, 46, 46] * 4
SynthDurations2 = [SN, SN, SN, SN, SN, SN, SN, SN] * 4




##### GUITARRA

# Guitar line pattern verse
# 4 COMPASES
GuitarPitches1 = [F2, F2, 44, G2, E2, E2, REST, E2, E2] * 2
GuitarDurations1 = [WN, WN, WN, HN, QN, EN, SN, SN/2,SN/2] * 2

# 4 COMPASES
GuitarPitches2 = [F2, F2, F2, F2, F2, F2, F2, F2, 44, 44, 44, 44, 44, 44, 44, 44, G2, G2, G2, G2, G2, G2, G2, G2, E2, E2, E2, E2, E2, E2, E2, E2 ] * 2 #* 4         # Patrón de guitarra para coros
GuitarDurations2 = [SN] * 32 * 2




######  ENSAMBLE

hiHatList = []
snareList = []
kickList = []
synthList = []
guitarList = []



# INTRO


# VERSO 1 


# CORO 1


# VERSO 2


# PUENTE


# CORO 2


# OUTRO