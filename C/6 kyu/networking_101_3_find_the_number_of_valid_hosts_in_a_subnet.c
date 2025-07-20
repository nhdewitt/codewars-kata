/*
Introduction
An IPv4 subnet mask consist of 32 bits, divided into four octets. As an example, a subnet mask of 255.255.255.0 can be written as:

    11111111.11111111.11111111.00000000
      255   .  255   .  255   .   0    
The ones (1) represent the network/subnet part of the mask and the zeroes (0) represent the host part of the mask.

The zeroes tell us how many IP addresses there are in the network defined by the ones.

In the example subnet above there are 256 addresses available; more precisely 0-255.

The Assignment
Your task is to implement a function uint32_t hosts_in_subnet(const char* netmask) which takes in an IPv4 subnet mask netmask and returns a 32-bit unsigned integer uint32_t with the number of valid host addresses. Using the subnet mask netmask you can figure out how many usable host addresses there are in a network defined by that netmask.

Notes
The first and last address in a subnet are not valid host addresses; they are reserved for the network and broadcast addresses.

There are two special cases:

If all 32 bits are ones there is only one valid host address.
When the mask has 31 bits set to ones there are two valid host addresses (according to RFC 3021).
Testing
The tests will challenge you with valid netmasks in the range (128.0.0.0 - 255.255.255.255) and nothing else.


https://www.codewars.com/kata/6285147937ddcf3ac2b068ce/train/c
*/

#include <inttypes.h>
#include <arpa/inet.h>

uint32_t hosts_in_subnet(const char* netmask)
{
    uint32_t mask = inet_addr(netmask);
  
    mask = ntohl(mask);
  
    uint32_t total_addr = (~mask) + 1;
  
    return total_addr <= 2 ? total_addr : total_addr - 2;
}