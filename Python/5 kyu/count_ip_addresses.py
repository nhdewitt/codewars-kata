"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246

https://www.codewars.com/kata/526989a41034285187000de4/python
"""

def ips_between(start, end):
    SLASH_8 = 16777216
    SLASH_16 = 65536
    SLASH_24 = 256
    ip_start = start.split(".")
    ip_end = end.split(".")
    octet_diffs = [int(end) - int(start) for start, end in zip(ip_start, ip_end)]
    o_1, o_2, o_3, o_4 = octet_diffs
    return o_1 * SLASH_8 + o_2 * SLASH_16 + o_3 * SLASH_24 + o_4