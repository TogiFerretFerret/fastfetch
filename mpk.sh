#!/bin/bash

PLAYER_STATUS=$(playerctl status 2>/dev/null)

if [ "$PLAYER_STATUS" = "Playing" ] || [ "$PLAYER_STATUS" = "Paused" ]; then
    # Output the current track info
    echo "$(playerctl metadata title) - $(playerctl metadata artist)"
else
    # Output custom text when nothing is playing/active
    echo "■ No media playing"
fi

