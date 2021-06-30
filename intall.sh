#!/bin/bash
for arg; do
    cd "/home/toni/.cache/yay/$arg"
    makepkg -fi
done
