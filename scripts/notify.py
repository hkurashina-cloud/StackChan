import os
import discord
from embeds import build_embed

webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
event_name = os.environ["GITHUB_EVENT_NAME"]  # "push" or "pull_request"
actor = os.environ["GITHUB_ACTOR"]
branch = os.environ["GITHUB_REF_NAME"]

webhook = discord.SyncWebhook.from_url(webhook_url)

if event_name == "push":
    embed = build_embed(
        title="📦 Push通知",
        description=f"{actor} さんが {branch} にpushしました",
        kind="info",
    )
else:
    title = os.environ.get("PR_TITLE", "")
    url = os.environ.get("PR_URL", "")
    action = os.environ.get("PR_ACTION", "")
    merged = os.environ.get("PR_MERGED") == "true"
    if action == "closed":
        label = "マージしました" if merged else "クローズしました"
        kind = "done" if merged else "info"
    else:
        label = "PRを作成しました"
        kind = "wip"
    embed = build_embed(
        title="🔀 PR通知",
        description=f"{actor} さんが {label}\n**{title}**\n{url}",
        kind=kind,
    )

webhook.send(embed=embed)
