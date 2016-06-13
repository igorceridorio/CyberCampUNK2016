#!/bin/bash

echo "User executing the script: $USER"
echo "Host executing the script: $HOSTNAME"
echo

echo "Creating directory with name passed as first argument..."
mkdir $1
cd $1

echo "Searching for user passed as second argument."
grep -i $2 /etc/passwd > searchOne.txt
echo "Result saved in searchOne.txt"

echo
echo "Content of searchOne.txt:"
cat searchOne.txt
echo

echo "Reverting the search passed as second argument."
grep -i -v $2 /etc/passwd > searchTwo.txt
echo "Result saved in searchTwo.txt"

echo
echo "Concatenating the searches."
cat searchOne.txt searchTwo.txt > concatenated.txt

echo
echo "Concatenated file:"
cat concatenated.txt