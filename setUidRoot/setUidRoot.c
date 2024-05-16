// This program allows users to execute any command with root privileges using execvp.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv) {
    if (setuid(0)) { // Set UID to 0 (root)
        perror("Failed to set UID to root");
        return 1;
    }

    if (argc < 2) {
        printf("Usage: %s <command> [args...]\n", argv[0]);
        return 1;
    }

    // Execute the input command and its arguments
    if (execvp(argv[1], &argv[1]) == -1) {
        perror("Failed to execute command");
        return 1;
    }

    return 0; // This line is not reached if execvp is successful
}

/*
gcc -o setuid-root setUidRoot.c
sudo chown root:root setuid-root
sudo chmod 4755 setuid-root
*/
