#Project1 Part1 of Sequence Analysis- "Counting Base Pairs"

My_strDNA = "TACTCTCGTTCTTGCAGCTTGTCAGTACTTTCAGAATCATGGTGTGCATGGTAGAATGACTCTTATAACGAACTTCGACATGGCAATAACCCCCCGAT"

def Count_Alphabet(My_strDNA):
    Mydict={'A':0,'C':0,'T':0,'G':0}
    for x in My_strDNA:
        for key,value in Mydict.items():
            if x==key:
                Mydict[key]=Mydict[key]+1
    Mydict2={'A':0,'C':0,'T':0,'G':0}
    for x in My_strDNA:
        for key,value in Mydict.items():
            if x==key:
                Mydict2[key]=(Mydict2[key]+1/.99)
    return Mydict, Mydict2

Mydict, Mydict2 = Count_Alphabet(My_strDNA)
print(Mydict)
print(Mydict2)
