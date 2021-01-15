# mspdebug 0.25

The mspdebug tool has been compiled on Fedora and Windows 10 to create these binaries. You can find more info on mspdebug [here](https://dlbeer.co.nz/mspdebug/) & you can get the source [here](https://github.com/dlbeer/mspdebug).

To compile it in linux I executed `make` command in the source directory. To compile it in Windows 10 before running `make` I had to edit some things in Makefile, find more info [here](https://github.com/dlbeer/mspdebug/issues/101#issuecomment-760713289).

# rom-bsl.exe

This executable is a renamed `BSLDEMO-2.01c.exe` found [here](https://github.com/gbhug5a/MSP430-BSL/tree/master/BSLDEMO-2.01c/Executable), Source for the same can be found [here](https://github.com/gbhug5a/MSP430-BSL/tree/master/BSLDEMO-2.01c/Source). I compiled it in Windows 10 using [lcc](https://lcc-win32.services.net/) compiler. 

After installing lcc, execute the command below to get the executable.

`lc .\bsldemo.c .\bslcomm.c .\TI_TXT_Files.c -o BSLDEMO-2.01c`


#### Notice: Respective entities owns the source and has all the rights reserved that are mentioned in their source code License agreement. Upside Down Labs (MIT) license for msptool does not convey anything otherwise that might effect the entity in any way possible. Their has been no deliberate action taken that might cause any damage to the entity. Please contact myupsidedownlab@gmail.com if you find any discrepancy in the notice and the way Upside Down Labs uses the executable(s).
