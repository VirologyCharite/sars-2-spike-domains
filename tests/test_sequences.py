from pathlib import Path

import sars_2_spike_domains
from sars_2_spike_domains.spike_numbers import (
    s1_start_offset,
    s1_stop_offset,
    s2_start_offset,
    s2_stop_offset,
)
from sars_2_spike_domains.sequences import S1_PREFIX, S1_SUFFIX, S2_PREFIX, S2_SUFFIX

from dark.fasta import FastaReads

REFERENCE = (
    Path(sars_2_spike_domains.__file__).parent.parent.parent / "NC_045512.2.fasta"
)

(SARS2,) = list(FastaReads(REFERENCE))


def test_ref_exists():
    assert REFERENCE.exists()


def test_sars2_length():
    assert len(SARS2) == 29903


def test_find_s1_prefix():
    assert SARS2.sequence.find(S1_PREFIX) == s1_start_offset


def test_find_s1_suffix():
    assert SARS2.sequence.find(S1_SUFFIX) + len(S1_SUFFIX) == s1_stop_offset


def test_find_s2_prefix():
    assert SARS2.sequence.find(S2_PREFIX) == s2_start_offset


def test_find_s2_suffix():
    assert SARS2.sequence.find(S2_SUFFIX) + len(S2_SUFFIX) == s2_stop_offset
