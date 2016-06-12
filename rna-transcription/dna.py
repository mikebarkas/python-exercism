# DNA RNA Transcription.
def to_rna(input):
    return input.translate(str.maketrans('GCTA','CGAU'))
