#!/bin/bash

systemctl stop shrub-bot

cp shrub-bot.service /etc/systemd/system/

systemctl start shrub-bot
systemctl enable shrub-bot

systemctl daemon-reload
