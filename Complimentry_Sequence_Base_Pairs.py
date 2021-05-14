#Project1 Part2 of Sequence Analysis- "Complementary Base pair"

My_strDNA = "3’-TACTCTCGTTCTTGCAGCTTGTCAGTACTTTCAGAATCATGGTGTGCATGGTAGAATGACTCTTATAACGAACTTCGACATGGCAATAACCCCCCGATT-5’"

result=""
for x in My_strDNA:
    if x=="T":
        x="A"
    elif x=="A":
        x="T"
    elif x=="C":
        x="G"
    elif x=="G":
        x="C"
    elif x=="3":
        x="5"
    elif x=="5":
        x="3"
    result=result+x
print(result)
