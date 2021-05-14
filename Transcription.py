#Project1 Part3 of Sequence Analysis- "Transcription"


My_strDNA = "3’-TACTCTCGTTCTTGCAGCTTGTCAGTACTTTCAGAATCATGGTGTGCATGGTAGAATGACTCTTATAACGAACTTCGACATGGCAATAACCCCCCGATT-5’"

result=""

for x in My_strDNA:
	if x== "T":
		x="U"

	result=result+x
print(result)