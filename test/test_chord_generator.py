import pytest
from ..chord_generator import pick_random_chord

chords = {
    # Accords mineurs
    'Cmin': [48, 51, 55],   # C, Eb, G
    'C#min': [49, 52, 56],  # C#, E, G#
    'Dbmin': [49, 52, 56],  # Db, E, Ab
    'Dmin': [50, 53, 57],   # D, F, A
    'D#min': [51, 54, 58],  # D#, F#, A#
    'Ebmin': [51, 54, 58],  # Eb, Gb, Bb=
    'Emin': [52, 55, 59],   # E, G, B
    'Fmin': [53, 56, 60],   # F, Ab, C
    'F#min': [54, 57, 61],  # F#, A, C#
    'Gbmin': [54, 57, 61],  # Gb, A, Db
    'Gmin': [55, 58, 62],   # G, Bb, D
    'G#min': [56, 59, 63],  # G#, B, D#
    'Abmin': [56, 59, 63],  # Ab, B, Eb
    'Amin': [57, 60, 64],   # A, C, E
    'A#min': [58, 61, 65],  # A#, C#, F
    'Bbmin': [58, 61, 65],  # Bb, Db, F
    'Bmin': [59, 62, 66],   # B, D, F#

    # Accords majeurs
    'Cmaj': [48, 52, 55],   # C, E, G
    'C#maj': [49, 53, 56],  # C#, F, G#
    'Dbmaj': [49, 53, 56],  # Db, F, Ab
    'Dmaj': [50, 54, 57],   # D, F#, A
    'D#maj': [51, 55, 58],  # D#, G, A#
    'Ebmaj': [51, 55, 58],  # Eb, G, Bb
    'Emaj': [52, 56, 59],   # E, G#, B
    'Fmaj': [53, 57, 60],   # F, A, C
    'F#maj': [54, 58, 61],  # F#, A#, C#
    'Gbmaj': [54, 58, 61],  # Gb, Bb, Db
    'Gmaj': [55, 59, 62],   # G, B, D
    'G#maj': [56, 60, 63],  # G#, C, D#
    'Abmaj': [56, 60, 63],  # Ab, C, Eb
    'Amaj': [57, 61, 64],   # A, C#, E
    'A#maj': [58, 62, 65],  # A#, D, F
    'Bbmaj': [58, 62, 65],  # Bb, D, F
    'Bmaj': [59, 63, 66],   # B, D#, F#

    # Accords de septième
    'C7': [48, 52, 55, 58],     # C, E, G, Bb
    'C#7': [49, 53, 56, 59],    # C#, F, G#, B
    'Db7': [49, 53, 56, 59],    # Db, F, Ab, B
    'D7': [50, 54, 57, 60],     # D, F#, A, C
    'D#7': [51, 55, 58, 61],    # D#, G, A#, C#
    'Eb7': [51, 55, 58, 61],    # Eb, G, Bb, Db
    'E7': [52, 56, 59, 62],     # E, G#, B, D
    'F7': [53, 57, 60, 63],     # F, A, C, Eb
    'F#7': [54, 58, 61, 64],    # F#, A#, C#, E
    'Gb7': [54, 58, 61, 64],    # Gb, Bb, Db, E
    'G7': [55, 59, 62, 65],     # G, B, D, F
    'G#7': [56, 60, 63, 66],    # G#, C, D#, F#
    'Ab7': [56, 60, 63, 66],    # Ab, C, Eb, Gb
    'A7': [57, 61, 64, 67],     # A, C#, E, G
    'A#7': [58, 62, 65, 68],    # A#, D, F, G#
    'Bb7': [58, 62, 65, 68],    # Bb, D, F, Ab
    'B7': [59, 63, 66, 69],     # B, D#, F#, A

    # Accords mineurs de septième
    'Cm7': [48, 51, 55, 58],    # C, Eb, G, Bb
    'C#m7': [49, 52, 56, 59],   # C#, E, G#, B
    'Dbm7': [49, 52, 56, 59],   # Db, E, Ab, B
    'Dm7': [50, 53, 57, 60],    # D, F, A, C
    'D#m7': [51, 54, 58, 61],   # D#, F#, A#, C#
    'Ebm7': [51, 54, 58, 61],   # Eb, Gb, Bb, Db
    'Em7': [52, 55, 59, 62],    # E, G, B, D
    'Fm7': [53, 56, 60, 63],    # F, Ab, C, Eb
    'F#m7': [54, 57, 61, 64],   # F#, A, C#, E
    'Gbm7': [54, 57, 61, 64],   # Gb, A, Db, E
    'Gm7': [55, 58, 62, 65],    # G, Bb, D, F
    'G#m7': [56, 59, 63, 66],   # G#, B, D#, F#
    'Abm7': [56, 59, 63, 66],   # Ab, B, Eb, Gb
    'Am7': [57, 60, 64, 67],    # A, C, E, G
    'A#m7': [58, 61, 65, 68],   # A#, C#, F, G#
    'Bbm7': [58, 61, 65, 68],   # Bb, Db, F, Ab
    'Bm7': [59, 62, 66, 69],    # B, D, F#, A

    # Accords de neuvième
    'C9': [48, 52, 55, 58, 62],     # C, E, G, Bb, D
    'C#9': [49, 53, 56, 59, 63],    # C#, F, G#, B, D#
    'Db9': [49, 53, 56, 59, 63],    # Db, F, Ab, B, Eb
    'D9': [50, 54, 57, 60, 64],     # D, F#, A, C, E
    'D#9': [51, 55, 58, 61, 65],    # D#, G, A#, C#, F
    'Eb9': [51, 55, 58, 61, 65],    # Eb, G, Bb, Db, F
    'E9': [52, 56, 59, 62, 66],     # E, G#, B, D, F#
    'F9': [53, 57, 60, 63, 67],     # F, A, C, Eb, G
    'F#9': [54, 58, 61, 64, 68],    # F#, A#, C#, E, G#
    'Gb9': [54, 58, 61, 64, 68],    # Gb, Bb, Db, E, Ab
    'G9': [55, 59, 62, 65, 69],     # G, B, D, F, A
    'G#9': [56, 60, 63, 66, 70],    # G#, C, D#, F#, A#
    'Ab9': [56, 60, 63, 66, 70],    # Ab, C, Eb, Gb, Bb
    'A9': [57, 61, 64, 67, 71],     # A, C#, E, G, B
    'A#9': [58, 62, 65, 68, 72],    # A#, D, F, G#, C
    'Bb9': [58, 62, 65, 68, 72],    # Bb, D, F, Ab, C
    'B9': [59, 63, 66, 69, 73],     # B, D#, F#, A, C#

    # Accords mineurs de neuvième
    'Cm9': [48, 51, 55, 58, 62],    # C, Eb, G, Bb, D
    'C#m9': [49, 52, 56, 59, 63],   # C#, E, G#, B, D#
    'Dbm9': [49, 52, 56, 59, 63],   # Db, E, Ab, B, Eb
    'Dm9': [50, 53, 57, 60, 64],    # D, F, A, C, E
    'D#m9': [51, 54, 58, 61, 65],   # D#, F#, A#, C#, F
    'Ebm9': [51, 54, 58, 61, 65],   # Eb, Gb, Bb, Db, F
    'Em9': [52, 55, 59, 62, 66],    # E, G, B, D, F#
    'Fm9': [53, 56, 60, 63, 67],    # F, Ab, C, Eb, G
    'F#m9': [54, 57, 61, 64, 68],   # F#, A, C#, E, G#
    'Gbm9': [54, 57, 61, 64, 68],   # Gb, A, Db, E, Ab
    'Gm9': [55, 58, 62, 65, 69],    # G, Bb, D, F, A
    'G#m9': [56, 59, 63, 66, 70],   # G#, B, D#, F#, A#
    'Abm9': [56, 59, 63, 66, 70],   # Ab, B, Eb, Gb, Bb
    'Am9': [57, 60, 64, 67, 71],    # A, C, E, G, B
    'A#m9': [58, 61, 65, 68, 72],   # A#, C#, F, G#, C
    'Bbm9': [58, 61, 65, 68, 72],   # Bb, Db, F, Ab, C
    'Bm9': [59, 62, 66, 69, 73],    # B, D, F#, A, C#

    'Cmaj7': [48, 52, 55, 59],   # C, E, G, B
    'C#maj7': [49, 53, 56, 60],  # C#, F, G#, C
    'Dbmaj7': [49, 53, 56, 60],  # Db, F, Ab, C
    'Dmaj7': [50, 54, 57, 61],   # D, F#, A, C#
    'D#maj7': [51, 55, 58, 62],  # D#, G, A#, D
    'Ebmaj7': [51, 55, 58, 62],  # Eb, G, Bb, D
    'Emaj7': [52, 56, 59, 63],   # E, G#, B, D#
    'Fmaj7': [53, 57, 60, 64],   # F, A, C, E
    'F#maj7': [54, 58, 61, 65],  # F#, A#, C#, E#
    'Gbmaj7': [54, 58, 61, 65],  # Gb, Bb, Db, F
    'Gmaj7': [55, 59, 62, 66],   # G, B, D, F#
    'G#maj7': [56, 60, 63, 67],  # G#, C, D#, G
    'Abmaj7': [56, 60, 63, 67],  # Ab, C, Eb, G
    'Amaj7': [57, 61, 64, 68],   # A, C#, E, G#
    'A#maj7': [58, 62, 65, 69],  # A#, D, F, A
    'Bbmaj7': [58, 62, 65, 69],  # Bb, D, F, A
    'Bmaj7': [59, 63, 66, 70],   # B, D#, F#, A#
    'Cbmaj7': [59, 63, 66, 70],
    'Fbmaj7': [64, 68, 59, 63],

    #Diminué 
    'Cdim': [48, 51, 54],       # C, Eb, Gb
    'C#dim': [49, 52, 55],      # C#, E, G
    'Ddim': [50, 53, 56],       # D, F, Ab
    'D#dim': [51, 54, 57],      # D#, F#, A
    'Edim': [52, 55, 58],       # E, G, Bb
    'Fdim': [53, 56, 59],       # F, Ab, B
    'F#dim': [54, 57, 60],      # F#, A, C
    'Gdim': [55, 58, 61],       # G, Bb, Db
    'G#dim': [56, 59, 62],      # G#, B, D
    'Adim': [57, 60, 63],       # A, C, Eb
    'A#dim': [58, 61, 64],      # A#, C#, E
    'Bdim': [59, 62, 65],       # B, D, F
    'Cbdim': [59, 62, 65],      # Cb, D, F

    #Dim 7
    'Cdim7': [48, 51, 54, 57],    # C, Eb, Gb, Bbb (A)
    'C#dim7': [49, 52, 55, 58],   # C#, E, G, Bb
    'Ddim7': [50, 53, 56, 59],    # D, F, Ab, Cb (B)
    'D#dim7': [51, 54, 57, 60],   # D#, F#, A, C
    'Edim7': [52, 55, 58, 61],    # E, G, Bb, Db
    'Fdim7': [53, 56, 59, 62],    # F, Ab, B, D
    'F#dim7': [54, 57, 60, 63],   # F#, A, C, Eb
    'Gdim7': [55, 58, 61, 64],    # G, Bb, Db, E
    'G#dim7': [56, 59, 62, 65],   # G#, B, D, F
    'Adim7': [57, 60, 63, 66],    # A, C, Eb, Gb
    'A#dim7': [58, 61, 64, 67],   # A#, C#, E, G
    'Bdim7': [59, 62, 65, 68],    # B, D, F, Ab
    'Cbdim7': [59, 62, 65, 68],   # Cb, D, F, Ab

}

def test_pick_random_chord():
    chord = pick_random_chord()
    assert chord in chords


def test_pick_not_in_random_chord():
    not_chord = 'Cmin42'
    assert not_chord not in chords
