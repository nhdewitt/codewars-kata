"""
Take the following IPv4 address: 128.32.10.1. This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.

Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.

Example
"128.32.10.1" => 2149583361

https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/train/python
"""

def ip_to_int32(ip):
    octets = [bin(int(i))[2:].zfill(8) for i in ip.split(".")]
    thirty_two_bit = octets[0] + octets[1] + octets[2] + octets[3]
    
    conversion = 0
    for i in range(-1, -33, -1):
        conversion += int(thirty_two_bit[i]) * (2 ** (abs(i) - 1))
    
    return conversion    