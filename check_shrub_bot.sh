#/bin/zsh

if [ -z "$(pgrep python)" ]; then
    /home/pi/shrub_bot/shrub_bot.py &> /home/pi/shrub_bot/bot.log &!
fi

