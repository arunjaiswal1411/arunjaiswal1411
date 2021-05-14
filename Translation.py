#Project1 Part4 of Sequence Analysis- "Translation"

My_dictionary = {
"UUU": "F", "UUC": "F", "UUA": "F", "UUG": "F", "UCU": "S",
"UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
"UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*",
"UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
"CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
"CGA": "R", "CGG": "R", "AUU": "L", "AUC": "L", "AUA": "L",
"AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
"AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
"AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
"GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
"GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
"GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

My_strDNA = "AUGAGAGCAAGAACGUCGAACAGUCAUGAAAGUCUUAGUACCACACGUACCAUCUUACUGAGAAUAUUGCUUGAAGCUGUACCGUUAUUGGGGGGCUAA"
result = ""
i = 0
while i < len(My_strDNA)-2:
    x = My_strDNA[i: i+3]
    for key,value in My_dictionary.items():
        if x == key:
            x = value
    result = result+x
    i = i+3
print(result)
