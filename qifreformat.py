#!/usr/bin/python
#-*- coding: utf-8 -*-
#
#       QifReformat
#
#       Copyright 2012 Francesco Mondello <faster3ck_[AT]_gmail.com>
#      
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#      
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#      
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#      

import os
import sys

def main():
  if len(sys.argv) != 3:
    print "Warning: this program accepts only 2 arguments."
    print "Usage:\npython qifreformat.py file_in.qif file_out.py"
    sys.exit(0)
  else:
    fileIn = sys.argv[1]
    fileOut = sys.argv[2]
      
    read(fileIn, fileOut)

def read(fileIn, fileOut):
  f = open(fileIn, "r")
  lines = f.readlines()
  
  myQifData = process(lines)
  
  if len(myQifData) != 0:
    writeFile(myQifData, fileOut)
  else:
    sys.stderr("Error: the input file seems empty")

def process(lines):
  firstLine = lines[0]
  if firstLine[0:6] != "!Type:":
    print "The input file doesn't seem a QIF file"
    sys.exit(0)
  
  myQifData = ""
  
  for item in lines:
    if item[0] == 'D' and len(item) == 12:
      line = item
      line = line.replace("D", "")
      
      splDate = line.split("-")
      
      corrDate = "D%s-%s-%s" % (splDate[2], splDate[1], splDate[0])
      corrDate = corrDate.replace("\n", "")
      
      myQifData += corrDate
      myQifData += "\n"
    else:
      myQifData += item
      
  return myQifData
      
      
def writeFile(myQifData, fileName):
  try:
    saveData = open(fileName,  "w")
    saveData.write(myQifData)
    
    print "File %s scritto correttamente!" % (fileName)
  except:
    sys.stderr("Errore: impossibile scrivere il file")
    
if __name__ == '__main__':
   main()
