import json
import argparse
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

def load_or_create_config():
    config_path = 'config.json'
    if not os.path.exists(config_path):
        default_config = {
            "api_id": "",
            "api_hash": "",
            "string_session": ""
        }
        with open(config_path, 'w') as config_file:
            json.dump(default_config, config_file, indent=4)
        print("Default config.json created. Please fill in the required fields.")
        exit(1)

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
        if not config.get("api_id") or not config.get("api_hash") or not config.get("string_session"):
            print("Error: config.json contains empty fields. Please fill them in before running the script.")
            exit(1)
        return config

def main():
    config = load_or_create_config()
    API_ID = config.get('api_id')
    API_HASH = config.get('api_hash')
    STRING_SESSION = config.get('string_session')

    parser = argparse.ArgumentParser(description="Telegram CLI Tool")
    parser.add_argument('-p', '--private', type=int, help="User ID for private chat")
    parser.add_argument('-g', '--group', type=int, help="Group ID")
    parser.add_argument('-c', '--channel', type=int, help="Channel ID")
    parser.add_argument('-t', '--text', type=str, help="Text message to send")
    parser.add_argument('-F', '--file', type=str, help="File path to send")
    parser.add_argument('-d', '--description', type=str, help="Description for the file")
    args = parser.parse_args()

    target_id = args.private or args.group or args.channel
    if not target_id:
        print("Error: You must specify a target using -p, -g, or -c or --help for help")
        exit(1)

    if not (args.text or args.file):
        print("Error: You must specify an event type (-t for text or -F for file).")
        exit(1)

    client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

    async def send_event():
        try:
            await client.start()
            # Attempt to get the entity to ensure it's cached
            try:
                if args.private:
                    entity = await client.get_entity(PeerUser(target_id))
                elif args.group:
                    entity = target_id
                elif args.channel:
                    entity = target_id
            except ValueError:
                print("Entity not found in cache. Fetching dialogs to update cache...")
                await client.get_dialogs()
                # Retry getting the entity after updating the cache
                if args.private:
                    entity = await client.get_entity(PeerUser(target_id))
                elif args.group:
                    entity = target_id
                elif args.channel:
                    entity = target_id

            if args.text:
                await client.send_message(entity, args.text)
                print("Text message sent successfully.")
            elif args.file:
                description = args.description or ""
                await client.send_file(entity, args.file, caption=description)
                print("File sent successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await client.disconnect()

    import asyncio
    asyncio.run(send_event())

if __name__ == "__main__":
    main()
