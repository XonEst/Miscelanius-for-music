from midiutil import MIDIFile

# Parámetros generales
bpm = 80
beats_per_measure = 4
track = 0
channel = 0
volume = 100
duration = 2 
repeats = 2

# Crear archivo MIDI
midi = MIDIFile(1)
midi.addTempo(track, 0, bpm)

# Diccionario de acordes (notas MIDI)
chords = {
    "F": [53, 57, 60],           # F3-A3-C4
    "Cm": [48, 51, 55],          # C3-Eb3-G3
    "Ebmaj7": [51, 55, 58, 62],  # Eb3-G3-Bb3-D4
    "Dm": [50, 53, 57],          # D3-F3-A3
    "Gm": [43, 46, 50],          # G2-Bb2-D3
    "Bb": [46, 50, 53],          # Bb2-D3-F3
    "Abmaj7": [44, 48, 51, 55],  # Ab2-C3-Eb3-G3
    "Cm7": [48, 51, 58],         # C3-Eb3-Bb3
}

# Progresión
progression = ["F", "Cm", "Ebmaj7", "Dm", "F", "Cm", "Ebmaj7", "Dm", 
               
               "F", "Cm", "Ebmaj7", "Dm", "F", "Cm", "Ebmaj7", "Dm", 
               
               "Gm", "Bb", "Abmaj7", "Cm7","Gm", "Bb", "Abmaj7", "Cm7",
               
               "F", "Cm", "Ebmaj7", "Dm","F", "Cm", "Ebmaj7", "Dm",]

# Agregar acordes al MIDI
time = 0
for _ in range(repeats):
    for chord_name in progression:
        for _ in range(2):  # dos blancas por compás
            for note in chords[chord_name]:
                midi.addNote(track, channel, note, time, duration, volume)
            time += duration  # avanzar 2 beats (una blanca)


# Guardar archivo
with open("backing_track_modal_cm.mid", "wb") as f:
    midi.writeFile(f)

print("Archivo backing_track_modal_cm.mid creado.")
