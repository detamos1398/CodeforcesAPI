#!/bin/bash

INSTALL_DIR="$(pwd)"
CUR_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# check for install location, default to current location, i.e. pwd
if [[ "$#" -ne 1 ]];
then
	echo "No install location specified, going with current location : $INSTALL_DIR"
else
	if [[ ! -d $1 ]];
	then
		echo "Give install location doesn't exist : $1"
		exit 1
	fi
	INSTALL_DIR=$1
fi

echo "Cleaing up existing(if) $INSTALL_DIR/codeforces_api"
rm -rf $INSTALL_DIR/codeforces_api

echo "Making directory $INSTALL_DIR/codeforces_api"
mkdir -p $INSTALL_DIR/codeforces_api

INSTALL_DIR="$INSTALL_DIR/codeforces_api"

echo "Copying necessary files : "
for file in "codeforces" "codeforces_lib.py" "constants.yaml" "codeforces_types.py"
do
	echo "Copying $CUR_DIR/$file into $INSTALL_DIR"
	cp $CUR_DIR/$file $INSTALL_DIR/ 
done

EXEC="$INSTALL_DIR/codeforces"

echo "Assigning necesary permission to executable"
chmod 777 $EXEC

echo "DONE!!!"

