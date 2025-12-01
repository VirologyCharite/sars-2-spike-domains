# In the below, variables with "site" in the name are 1-based, and those with "offset"
# are 0-based.

# From https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2/ S runs from
# 21563 to 25384 (1-based inclusive sites).
#
# From https://pmc.ncbi.nlm.nih.gov/articles/PMC8279943/,
# "the S1 subunit (14–685 residues), and the S2 subunit (686-1273 residues)".
# These are 1-based AA sites.

s_start_site = 21563
# The -3 in the following is due to the fact that the nt offsets in the GenBank
# reference include the stop codon. However, the AA sequence in the GenBank file is 1273
# not 1274 because it omits the stop codon.
s_stop_site = 25384 - 3

s1_aa_start_site = 14
s1_aa_stop_site = 685

s2_aa_start_site = 686
s2_aa_stop_site = 1273

################################## S ##################################

s_start_offset = s_start_site - 1
s_stop_offset = s_stop_site

s_len = s_stop_offset - s_start_offset

############################### S1 domain #############################

s1_start_site = s_start_site + ((s1_aa_start_site - 1) * 3)
s1_stop_site = s1_start_site + (s1_aa_stop_site - s1_aa_start_site + 1) * 3 - 1

s1_start_offset = s1_start_site - 1
s1_stop_offset = s1_stop_site

s1_len = s1_stop_offset - s1_start_offset

############################## S2 domain ##############################

s2_start_site = s_start_site + ((s2_aa_start_site - 1) * 3)
s2_stop_site = s2_start_site + (s2_aa_stop_site - s2_aa_start_site + 1) * 3 - 1

s2_start_offset = s2_start_site - 1
s2_stop_offset = s2_stop_site

s2_len = s2_stop_offset - s2_start_offset

################################ TOTAL ################################

s_len_computed = (s1_aa_start_site - 1) * 3 + s1_len + s2_len
