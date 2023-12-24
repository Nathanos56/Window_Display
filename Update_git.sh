#!/bin/bash
cd /Home/Window_Display/
git fetch
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})
if [ $LOCAL != $REMOTE ]; then
    git pull
fi



*/5 * * * * /path/to/your/script.sh
chmod +x /path/to/your/script.sh