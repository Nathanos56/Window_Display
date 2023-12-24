#!/bin/bash
cd /Home/Window_Display/
git fetch origin main
LOCAL=$(git rev-parse main)
REMOTE=$(git rev-parse origin/main)
if [ $LOCAL != $REMOTE ]; then
    git pull origin main
fi