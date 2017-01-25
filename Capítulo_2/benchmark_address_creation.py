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

import bitcoin
import datetime as dt

start = dt.datetime.now()
print start

gens = {}

for e in range(1000):
    key = bitcoin.random_key()
    gens[bitcoin.privtoaddr(key)] = key

with open("generadas.txt", "w") as oF:
    for e in gens.keys():
        oF.write(e + "\t" + gens[e])

end = dt.datetime.now()
print end
