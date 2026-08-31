#!/usr/bin/env bash
set -u

# Simple terminal rain effect. Stop with Ctrl+C.
trap 'printf "\033[0m\033[?25h\n"; exit 0' INT TERM EXIT
printf '\033[?25l'

chars='01ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%&*+'
cols=$(tput cols 2>/dev/null || echo 80)
rows=$(tput lines 2>/dev/null || echo 24)

while true; do
    x=$((RANDOM % cols))
    length=$((RANDOM % 10 + 3))
    start=$((RANDOM % rows))

    for ((i=0; i<length; i++)); do
        y=$((start + i))
        [ "$y" -ge "$rows" ] && break
        char=${chars:RANDOM%${#chars}:1}
        printf '\033[%d;%dH%s' "$((y+1))" "$((x+1))" "$char"
    done

    sleep 0.03
done
