from sars_2_spike_domains.sequences import S1_PREFIX, S1_SUFFIX, S2_PREFIX, S2_SUFFIX
from sars_2_spike_domains.spike_numbers import s1_len, s2_len


def main():
    print(f"S1 ({s1_len} nt): {S1_PREFIX} .. {S1_SUFFIX}")
    print(f"S2 ({s2_len} nt): {S2_PREFIX} .. {S2_SUFFIX}")
