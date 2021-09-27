from dhooks import Webhook

def notify(title, message, discord_url, retcode=None):
    """
    Required parameter:
        * ``discord_url`` - The Discord Wenhook URL

    Sends message over Discord using dhooks, title is username."""
    
    hook = Webhook(discord_url)
    hook.send(message,username=title)