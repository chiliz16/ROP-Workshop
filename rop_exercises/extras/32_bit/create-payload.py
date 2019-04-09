#!/usr/bin/python2
from pwn import *

#STEP 1: find the right amount of bytes to overflow the buffer up to the saved return address 
FILLBUF = XXX

# STEP 2: determine base address of libc and extract offsets to 'system' and '/bin/sh' 
libcbase = XXX
OFFSET_SYSTEM = XXX
OFFSET_BIN_SH = XXX 

# STEP 3: calculate addresses of 'system' and '/bin/sh'
address_system = XXX 
address_bin_sh = XXX

# STEP 4: Build ROP-Chain
payload = "A" * FILLBUF 
payload += XXX 
payload += XXX 
payload += XXX 

print payload
