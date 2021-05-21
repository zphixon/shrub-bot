#/bin/zsh

if [ -z "$(pgrep python)" ]; then
    /home/zack/shrub_bot/shrub_bot.py &> /home/zack/shrub_bot/bot.log &!
fi

