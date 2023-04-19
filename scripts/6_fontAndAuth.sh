#!/bin/bash

# Any other things that may need to be installed

# This script adds the EVA font to your local env to it works
FONT_DIRECTORY=~/.fonts/
FONT_FILE=EXPOFILES/assets/fonts/Inter-VariableFont_slnt,wght.ttf
CERT_DIRECTORY=EXPOFILES/certs
CERT_FILE=eva2_service_data.json
CERT_URL=https://console.firebase.google.com/u/0/project/elderly-virtual-assistant-2/settings/cloudmessaging

if [ ! -d "$FONT_DIRECTORY" ]; then
    mkdir "$FONT_DIRECTORY"
    sudo cp "$FONT_FILE" "$FONT_DIRECTORY"
else
    echo "$FONT_DIRECTORY already exists, skipping directory creation"
fi

# if [ ! -d "$CERT_DIRECTORY" ]; then
#     mkdir "$CERT_DIRECTORY"
#     sudo cp "$FONT_FILE" "$CERT_DIRECTORY"
# else
#     echo "$CERT_DIRECTORY already exists, skipping directory creation"
# fi

echo "$CERT_FILE must be located in $CERT_DIRECTORY, and must be downloaded from the google project at $CERT_URL"

export GOOGLE_APPLICATION_CREDENTIALS="$CERT_DIRECTORY"/"$CERT_NAME"