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

import sha
import sys

def calculateToken(challenge = "Bitcoin", numZeros = 2):
    """
        Calculating the token that matches the proof of work. 
        Sample values by default: "Bitcoin" and 2 consecutive zeroes.
    """

    # Building the sequence of zeroes
    strZeros = ''
    for k in range(numZeros): strZeros += '0'

    index = 0

    while True:
        value = sha.new( challenge + str(index) ).hexdigest()
        print value
        if value[:numZeros] == strZeros:
                print
                print "Match found: " + challenge + str(index)
                print "\tChallenge --> " + challenge
                print "\tToken     --> " + str(index)
                print "\tHash      --> " + value
                break
        else:
                index+=1

def show_usage():
    print("Usage: hashcash_sample.py <CHALLENGE> <NUMBER_ZEROS>")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        calculateToken(sys.argv[1], int(sys.argv[2]))
    else:
        print("Hey! Two parameters are required.")
        show_usage()