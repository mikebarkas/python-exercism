# DNA RNA Transcription.
def to_rna(input):
    translate_table = str.maketrans('GCTA','CGAU')
    return input.translate(translate_table)
