from sars_2_spike_domains.spike_numbers import (
    s_len,
    s_start_offset,
    s_stop_offset,
    s1_len,
    s1_aa_start_site,
    s1_start_offset,
    s1_stop_offset,
    s2_len,
    s2_start_offset,
    s2_stop_offset,
)


def main():
    initial = (s1_aa_start_site - 1) * 3
    assert initial + s1_len + s2_len == s_len
    print("Lengths:")
    print(f"  Initial:     {initial}")
    print(f"  S1:        {s1_len}")
    print(f"  S2:        {s2_len}")
    print(f"  S (total): {s_len}")

    print("\nPython slicing offsets:")
    print(f"  S1: [{s1_start_offset}: {s1_stop_offset}]")
    print(f"  S2: [{s2_start_offset}: {s2_stop_offset}]")
    print(f"  S:  [{s_start_offset}: {s_stop_offset}]")

    print("\n1-based (inclusive) sites for a GenBank record:")
    print(f"  S1: {s1_start_offset + 1}..{s1_stop_offset}")
    print(f"  S2: {s2_start_offset + 1}..{s2_stop_offset}")
