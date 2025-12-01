from sars_2_spike_domains.spike_numbers import (
    s_len,
    s_len_computed,
    s_start_site,
    s_stop_site,
    s1_len,
    s1_aa_start_site,
    s1_aa_stop_site,
    s1_start_site,
    s1_stop_site,
    s1_start_offset,
    s1_stop_offset,
    s2_len,
    s2_aa_start_site,
    s2_aa_stop_site,
    s2_start_site,
    s2_stop_site,
    s2_start_offset,
    s2_stop_offset,
)


def test_s_len():
    assert s_len == s_stop_site - s_start_site + 1
    assert s_len == s2_aa_stop_site * 3
    assert s_len == 3819


def test_s1_offsets():
    assert s1_start_site == 21602
    assert s1_stop_offset == 23617
    assert s1_start_offset == s1_start_site - 1
    assert s1_start_offset + s1_len == s1_stop_offset
    assert (s1_stop_site - s1_start_site + 1) == s1_stop_offset - s1_start_offset


def test_s1_len():
    assert s1_len == (s1_aa_stop_site - s1_aa_start_site + 1) * 3
    assert s1_len == s1_stop_site - s1_start_site + 1
    assert s1_len == s1_stop_offset - s1_start_offset
    assert s1_len == 2016


def test_s2_offsets():
    assert s2_start_site == 23618
    assert s2_start_offset == s2_start_site - 1
    assert s2_start_offset + s2_len == s2_stop_offset
    assert s2_stop_offset == 25381
    assert (s2_stop_site - s2_start_site + 1) == s2_stop_offset - s2_start_offset


def test_s2_len():
    assert s2_len == (s2_aa_stop_site - s2_aa_start_site + 1) * 3
    assert s2_len == s2_stop_site - s2_start_site + 1
    assert s2_len == s2_stop_offset - s2_start_offset
    assert s2_len == 1764


def test_s2_starts_immediately_after_s1():
    assert s2_start_site == s1_stop_site + 1
    assert s2_start_offset == s1_stop_offset


def test_computed_len():
    assert s_len == s_len_computed
