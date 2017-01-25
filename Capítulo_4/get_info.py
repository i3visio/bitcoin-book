# -*- coding: utf-8 -*-
# Copyright (C) 2016,  Félix Brezo @febrezo and Yaiza Rubio @yrubiosec
# 
#  This program is free software: you can redistribute it and/or modify# 
#  it under the terms of the Affero GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the Affero GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib2
import json
import sys

BASEURL = "http://localhost:3001/insight-api/addr/"

def getInfo(addresses)
    results = []
    for addr in addresses:
        url = BASEURL + addr
        response = json.loads(urllib2.urlopen(url).read())
        print(addr + ":\t" + str(response["balance"]))
        results.append(response)
    return results
        

def showUsage():
    print "Usage:   python get_info.py <ADDRESS> [<ADDRESS> ...]"

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "The program needs at least one address."
        showUsage()
        sys.exit()
    addresses = sys.argv[1:]
    # Launching the process...
    getInfo(addresses)   
     