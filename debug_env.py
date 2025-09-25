#!/usr/bin/env python3
import os

print("Environment variables:")
print(f"GH_TOKEN: {os.getenv('GH_TOKEN')}")
print(f"DISCORD_WEBHOOK_URL: {os.getenv('DISCORD_WEBHOOK_URL')}")

# Test the DiscordNotifier class
from ai_tracker import DiscordNotifier

notifier = DiscordNotifier()
print(f"Notifier webhook_url: {notifier.webhook_url}")