# -*- coding: utf-8 -*-
# Copyright (C) 2016,  Félix Brezo @febrezo and Yaiza Rubio @yrubiosec
# 
#  This program is free software: you can redistribute it and/or modify# 
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Adapted to work in Python 2 from <https://rosettacode.org/wiki/Bitcoin/address_validation#Python>

__version__ = "1.0"
__author__ = "@febrezo and @yrubiosec"

from hashlib import sha256
import sys

# Base58Check
DIGITS58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def to_bytes_py2(n, length, endianess='big'):
    """
        Needed to be defined to match to_bytes function in Python 3.
    """
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]
 
def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + DIGITS58.index(char)
        
    # prints whether python is version 3 or not
    python_version = sys.version_info.major
    if python_version == 3:
        # Python 3
        return n.to_bytes(length, 'big')
    else:
        # Python 2, adapted to do the same job
        return to_bytes_py2(n, length, 'big')

def check_bc(bc):
    bcbytes = decode_base58(bc, 25)
    return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]

def show_usage():
    print("Usage: address_validator.py <ADDRESS> [<ADDRESS> ...]")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        for address in sys.argv[1:]:
            print(address + ": " + str(check_bc(address)))
    else:
        print("Hey! At least one address is required.")
        show_usage()