#!/bin/python
import struct

def extract():
        f = open('flag.png', 'rb')
        bytes = f.read()
        end = bytes.find(b'\x49\x45\x4e\x44\xae\x42\x60\x82')
        if end:
           out = open('out', 'wb')
           out.write( bytes[end+len(b'\x49\x45\x4e\x44\xae\x42\x60\x82'):] )
           out.close()         
extract()
         