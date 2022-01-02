#!/bin/bash
for (( i=1; i<26; i++ )) ;
do
    touch "./puzzle_$i/__init__.py";
    touch "./puzzle_$i/part_1/__init__.py";
    touch "./puzzle_$i/part_2/__init__.py";
done