#!/usr/bin/python2
from pwn import *

# STEP 1: find the right amount of bytes to overflow the buffer up to the saved return address
FILLBUF = XXX

# STEP 2: determine base address of libc and extract offsets to 'system' and '/bin/sh' 
LIBC_BASE = XXX 
OFFSET_SYSTEM = XXX
OFFSET_BIN_SH = XXX 

# STEP 3: find ROP-Gadget to load a value into RDI and ROPNOP (RET) gadget to adjust for stack
#         alignment if needed
POP_RDI = XXX
RET 	= XXX

# STEP 4: calculate the addresses of 'system' and '/bin/sh'
address_system = XXX
address_bin_sh = XXX

# STEP 5: build the ROP-chain
payload =  XXX
payload += XXX
payload += XXX
payload += XXX
payload += XXX


print payload
