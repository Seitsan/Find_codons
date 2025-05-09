def find_codons(dna:str) -> dict:
    """
    Takes a DNA sequence and looks for a start- and stop-codons
    :param dna: DNA sequence as string
    :return: The dict with information about positions of start- and stop-codons
    """
    atg_position = []
    taa_position = []
    tag_position = []
    tga_position = []
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        if codon == 'ATG':
            atg_position.append(i)
        elif codon == 'TAA':
            taa_position.append(i)
        elif codon == 'TAG':
            tag_position.append(i)
        elif codon == 'TGA':
            tga_position.append(i)
    return {
        "start_codons": atg_position,
        "stop_codons": {
            "TAA": taa_position,
            "TAG": tag_position,
            "TGA": tga_position
        }
    }


def dna_verification(dna:str) -> bool:
    """
    Takes DNA sequence as input and check if all characters are nucleotides
    :param dna: A DNA sequence as string
    :return: True or False
    """
    return set(dna).issubset({'A', 'T', 'G', 'C'})


def main():
    sequence = input('Enter a DNA sequence: ')
    dna = sequence.upper()
    if dna_verification(dna):
        codon_data = find_codons(dna)
        print(f'Start codons found at positions: {codon_data["start_codons"]}')
        print('Stop codons found at positions:')
        for codon, positions in codon_data["stop_codons"].items():
            print(f'    {codon}:{positions}')
    else:
        print('This sequence is not a DNA sequence')


main()