# clang

https://clang.llvm.org/

an "LLVM native" C/C++/Objective-C compiler
a front end for the LLVM compiler back end [llvm.org](https://www.llvm.org)
 
$ cat t.c
#include <stdio.h>
int main(int argc, char **argv) { printf("hello world\n"); }
$ clang t.c
$ ./a.out
hello world