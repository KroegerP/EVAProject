#!/bin/bash


MEDS_DIR="EXPOFILES/database/meds"
DRUG_INFO_IMAGES="EXPOFILES/assets/drugInfoImages"
GENERATED_IMAGES="EXPOFILES/assets/generatedImages"

if [ -d "$MEDS_DIR" ];
then
	echo "meds dir already exists"
else
	echo "Creating meds dir."
	mkdir "$MEDS_DIR"
fi

if [ -d "$DRUG_INFO_IMAGES" ];
then
	echo "drug info dir already exists"
else
	echo "Creating drug info  dir."
	mkdir "$DRUG_INFO_IMAGES"
fi

if [ -d "$GENERATED_IMAGES" ];
then
	echo "generated images dir already exists"
else
	echo "Creating generated images dir."
	mkdir "$GENERATED_IMAGES"
fi
