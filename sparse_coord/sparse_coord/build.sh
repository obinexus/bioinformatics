#!/usr/bin/env bash
set -e
gcc -Wall -O2 -fPIC -shared plp128.c -lm -o plp128.so
echo "plp128.so built successfully"
