import argparse
import json
import os
import sys
import requests

def command(shell):
    stream = os.popen(shell)
    return stream.read().strip()


def main():
    parser = argparse.ArgumentParser(description='NewRelic Deplyment')
    parser.add_argument('--key', '-k')
    parser.add_argument('--app', '-a')
    args = parser.parse_args()

    if args.key and args.app:
        last_revision=command('git rev-parse HEAD')
        last_changes=command("git log -1 | sed '1,/Date/d' | sed '/^[[:space:]]*$/d' | sed 's/^ *//'")
        author=command("git log -1 | grep Author | awk -F: '{print $2}'")

        payload = {
            'deployment': {
                'revision': last_revision,
                'changelog': last_changes,
                'description': last_changes,
                'user': author
            }
        }

        endpoint = f'https://api.newrelic.com/v2/applications/{args.app}/deployments.json'

        headers = {
            'X-Api-Key': args.key,
            'Content-Type': 'application/json'
        }
        try:
            r = requests.post(endpoint, headers=headers, data=payload)
            r.raise_for_status()
            print('NewRelic Deployment successfully notified')
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
    else:
        print('Invalid --key and --app is required')
