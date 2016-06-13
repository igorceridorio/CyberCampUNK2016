#!/bin/bash

#using some special variables
echo
echo "User executing the script: $USER"
echo
echo "Files before executing command:"

ls
mkdir $1 $2

echo
echo "Files after executing command:"

ls

echo