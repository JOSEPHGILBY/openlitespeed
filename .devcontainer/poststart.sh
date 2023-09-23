#!/bin/sh
if [ ! -f "/INSTALL_DONE" ]; then
    exit 0
fi
/entrypoint.sh

