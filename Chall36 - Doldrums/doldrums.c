//
// This file was generated by the Retargetable Decompiler
// Website: https://retdec.com
//

#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// ------------------------ Structures ------------------------

struct _IO_FILE {
    int32_t e0;
};

// ------------------- Function Prototypes --------------------

int32_t entry_point(int32_t a1);
int32_t function_80483f0(void);
int32_t function_8048430(char * format, ...);
char * function_8048440(char * s);
void function_8048450(int32_t status);
void (*function_8048460(int32_t sig, void (*handler)(int32_t)))(int32_t);
int32_t function_8048470(int32_t seconds);
int32_t function_8048480(char * s);
int32_t function_8048490(char * command);
int32_t function_80484a0(int32_t main, int32_t argc, char ** ubp_av, void (*init)(), void (*fini)(), void (*rtld_fini)());
int32_t function_80484b0(struct _IO_FILE * stream, char * buf, int32_t modes, int32_t n);
void function_80484c0(void);
int32_t function_8048503(int32_t a1);
int32_t function_8048510(void);
int32_t function_8048520(int32_t a1);
int32_t function_8048530(void);
int32_t function_8048570(void);
int32_t function_80485b0(void);
int32_t function_80485e0(void);
int32_t function_80485e6(void);
int32_t function_80486bc(void);
int32_t function_80486cb(int32_t a1);
int32_t function_80486cd(void);
int32_t function_80486d0(void);
int32_t function_80486d3(void);
int32_t function_80486d7(int32_t a1);
int32_t function_80486d9(void);
int32_t function_8048733(int32_t a1);
int32_t function_8048764(void);
int32_t function_8048794(int32_t result);
int32_t function_80487a0(int32_t a1);
int32_t function_8048800(void);
int32_t function_8048804(void);

// --------------------- Global Variables ---------------------

int32_t g1; // 0x804a60a
int32_t g2;

// ------------------------ Functions -------------------------

// Address range: 0x80483f0 - 0x8048413
int32_t function_80483f0(void) {
    // 0x80483f0
    int32_t v1; // 0x80483f0
    function_8048520(v1);
    int32_t result = 0; // 0x8048407
    if (*(int32_t *)(v1 + 0x1bfb) != 0) {
        // 0x8048409
        __gmon_start__();
        result = &g2;
    }
    // 0x804840e
    return result;
}

// Address range: 0x8048430 - 0x8048436
int32_t function_8048430(char * format, ...) {
    // 0x8048430
    return printf(format);
}

// Address range: 0x8048440 - 0x8048446
char * function_8048440(char * s) {
    // 0x8048440
    return gets(s);
}

// Address range: 0x8048450 - 0x8048456
void function_8048450(int32_t status) {
    // 0x8048450
    _exit(status);
}

// Address range: 0x8048460 - 0x8048466
void (*function_8048460(int32_t sig, void (*handler)(int32_t)))(int32_t) {
    // 0x8048460
    return signal(sig, handler);
}

// Address range: 0x8048470 - 0x8048476
int32_t function_8048470(int32_t seconds) {
    // 0x8048470
    return alarm(seconds);
}

// Address range: 0x8048480 - 0x8048486
int32_t function_8048480(char * s) {
    // 0x8048480
    return puts(s);
}

// Address range: 0x8048490 - 0x8048496
int32_t function_8048490(char * command) {
    // 0x8048490
    return system(command);
}

// Address range: 0x80484a0 - 0x80484a6
int32_t function_80484a0(int32_t main, int32_t argc, char ** ubp_av, void (*init)(), void (*fini)(), void (*rtld_fini)()) {
    // 0x80484a0
    return __libc_start_main(main, argc, ubp_av, init, fini, rtld_fini);
}

// Address range: 0x80484b0 - 0x80484b6
int32_t function_80484b0(struct _IO_FILE * stream, char * buf, int32_t modes, int32_t n) {
    // 0x80484b0
    return setvbuf(stream, buf, modes, n);
}

// Address range: 0x80484c0 - 0x80484c6
void function_80484c0(void) {
    // 0x80484c0
    __gmon_start__();
}

// Address range: 0x80484d0 - 0x8048503
int32_t entry_point(int32_t a1) {
    // 0x80484d0
    int32_t v1; // 0x80484d0
    int32_t v2 = v1;
    function_8048503(v1);
    int32_t v3; // 0x80484d0
    __libc_start_main(0x80485e6, a1, (char **)&v3, (void (*)())(v2 + 704), (void (*)())(v2 + 800), (void (*)())&g2);
    __asm_hlt();
    // UNREACHABLE
}

// Address range: 0x8048503 - 0x8048507
int32_t function_8048503(int32_t a1) {
    // 0x8048503
    int32_t result; // 0x8048503
    return result;
}

// Address range: 0x8048510 - 0x8048512
int32_t function_8048510(void) {
    // 0x8048510
    int32_t result; // 0x8048510
    return result;
}

// Address range: 0x8048520 - 0x8048524
int32_t function_8048520(int32_t a1) {
    // 0x8048520
    int32_t result; // 0x8048520
    return result;
}

// Address range: 0x8048530 - 0x8048562
int32_t function_8048530(void) {
    // 0x8048530
    return 0x804a60c;
}

// Address range: 0x8048570 - 0x80485aa
int32_t function_8048570(void) {
    // 0x8048570
    return 0;
}

// Address range: 0x80485b0 - 0x80485d2
int32_t function_80485b0(void) {
    // 0x80485b0
    if (*(char *)0x804a60a != 0) {
        // 0x80485d0
        int32_t result; // 0x80485b0
        return result;
    }
    int32_t result2 = function_8048530(); // 0x80485bf
    *(char *)&g1 = 1;
    return result2;
}

// Address range: 0x80485e0 - 0x80485e6
int32_t function_80485e0(void) {
    // 0x80485e0
    return function_8048570();
}

// Address range: 0x80485e6 - 0x80486bc
int32_t function_80485e6(void) {
    // 0x80485e6
    int32_t v1; // 0x80485e6
    function_8048520(v1);
    int32_t str = *(int32_t *)(v1 + 766); // bp-13, 0x80485fe
    function_80486d9();
    function_8048764();
    puts((char *)(v1 + 558));
    puts((char *)(v1 + 634));
    gets((char *)&str);
    system((char *)(v1 + 667));
    puts((char *)(v1 + 686));
    printf((char *)(v1 + 742));
    return 0;
}

// Address range: 0x80486bc - 0x80486cb
int32_t function_80486bc(void) {
    // 0x80486bc
    int32_t v1; // 0x80486bc
    return function_8048794(v1) + 0x193c;
}

// Address range: 0x80486cb - 0x80486cd
int32_t function_80486cb(int32_t a1) {
    // 0x80486cb
    int32_t result; // 0x80486cb
    return result;
}

// Address range: 0x80486cd - 0x80486d0
int32_t function_80486cd(void) {
    // 0x80486cd
    return 0;
}

// Address range: 0x80486d0 - 0x80486d3
int32_t function_80486d0(void) {
    // 0x80486d0
    int32_t result; // 0x80486d0
    return result;
}

// Address range: 0x80486d3 - 0x80486d6
int32_t function_80486d3(void) {
    // 0x80486d3
    int32_t result; // 0x80486d3
    return result;
}

// Address range: 0x80486d7 - 0x80486d9
int32_t function_80486d7(int32_t a1) {
    // 0x80486d7
    int32_t result; // 0x80486d7
    return result;
}

// Address range: 0x80486d9 - 0x8048733
int32_t function_80486d9(void) {
    // 0x80486d9
    int32_t v1; // 0x80486d9
    function_8048520(v1);
    setvbuf((struct _IO_FILE *)*(int32_t *)*(int32_t *)(v1 + 0x191a), NULL, 2, 0);
    setvbuf((struct _IO_FILE *)*(int32_t *)*(int32_t *)(v1 + 0x1916), NULL, 2, 0);
    return setvbuf((struct _IO_FILE *)*(int32_t *)*(int32_t *)(v1 + 0x190e), NULL, 2, 0);
}

// Address range: 0x8048733 - 0x8048764
int32_t function_8048733(int32_t a1) {
    // 0x8048733
    int32_t v1; // 0x8048733
    int32_t result = function_8048520(v1); // 0x8048737
    if (a1 != 14) {
        // 0x804875e
        return result;
    }
    // 0x8048748
    printf((char *)(v1 + 444));
    _exit(0);
    // UNREACHABLE
}

// Address range: 0x8048764 - 0x8048794
int32_t function_8048764(void) {
    // 0x8048764
    int32_t v1; // 0x8048764
    function_8048520(v1);
    signal(SIGALARM, (void (*)(int32_t))(v1 - 58));
    return alarm(60);
}

// Address range: 0x8048794 - 0x8048798
int32_t function_8048794(int32_t result) {
    // 0x8048794
    return result;
}

// Address range: 0x80487a0 - 0x80487fd
int32_t function_80487a0(int32_t a1) {
    // 0x80487f5
    int32_t v1; // 0x80487a0
    function_8048520(v1);
    int32_t v2; // bp-28, 0x80487a0
    int32_t v3 = &v2; // 0x80487af
    function_80483f0();
    *(int32_t *)(v3 - 8) = a1;
    *(int32_t *)(v3 - 12) = *(int32_t *)(v3 + 36);
    *(int32_t *)(v3 - 16) = *(int32_t *)(v3 + 32);
    return v1 + 0x1757;
}

// Address range: 0x8048800 - 0x8048802
int32_t function_8048800(void) {
    // 0x8048800
    int32_t result; // 0x8048800
    return result;
}

// Address range: 0x8048804 - 0x8048818
int32_t function_8048804(void) {
    // 0x8048804
    int32_t v1; // 0x8048804
    return function_8048520(v1);
}

// --------------- Dynamically Linked Functions ---------------

// void __gmon_start__(void);
// int __libc_start_main(int *(main)(int, char **, char **), int argc, char ** ubp_av, void(* init)(void), void(* fini)(void), void(* rtld_fini)(void), void(* stack_end));
// void _exit(int status);
// unsigned int alarm(unsigned int seconds);
// char * gets(char * s);
// int printf(const char * restrict format, ...);
// int puts(const char * s);
// int setvbuf(FILE * restrict stream, char * restrict buf, int modes, size_t n);
// __sighandler_t signal(int sig, __sighandler_t handler);
// int system(const char * command);

// --------------------- Meta-Information ---------------------

// Detected compiler/packer: gcc (7.5.0)
// Detected functions: 33
