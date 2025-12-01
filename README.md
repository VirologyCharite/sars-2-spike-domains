# SARS-CoV-2 S1 and S2 domains

Here is information about the location of the S1 and S2 domains in [the
SARS-CoV-2 reference sequence](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2/) based on sites
given in [this
paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8279943/). Specifically, they
refer to the S1 subunit (14–685 residues), and the S2 subunit (686-1273
residues).

## Available commands

```sh
$ uv run print-domains
Lengths:
  Initial:     39
  S1:        2016
  S2:        1764
  S (total): 3819

Python slicing offsets:
  S1: [21601: 23617]
  S2: [23617: 25381]
  S:  [21562: 25381]

1-based (inclusive) sites for a GenBank record:
  S1: 21602..23617
  S2: 23618..25381
```

```sh
uv run print-sequences
S1 (2016 nt): CAGTGTGTTAATCTTACAACCAGAACTCAATTACCCCCTG .. TAGTTATCAGACTCAGACTAATTCTCCTCGGCGGGCACGT
S2 (1764 nt): AGTGTAGCTAGTCAATCCATCATTGCCTACACTATGTCAC .. CTCTGAGCCAGTGCTCAAAGGAGTCAAATTACATTACACA
```

## Cutting the S1 domain out of an alignment

Assuming you have [the SARS-CoV-2 reference
sequence](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2/) in an alignment
and have [dark-matter](https://github.com/acorg/dark-matter) installed, try
this:

```sh
$ uv run msa-find-and-extract.py \
         --prefix CAGTGTGTTAATCTTACAACCAGAACTCAATTACCCCCTG \
         --suffix TAGTTATCAGACTCAGACTAATTCTCCTCGGCGGGCACGT \
         < HCoV-alignment.fasta > HCoV-S1-domain-alignment.fasta
```

and similarly for extracting the S2 domain of all sequences in an alignment.
