import json
import requests
import os
import argparse

def check_health(url, headers):

    url = f"{url}/health"
    r = requests.get(url, headers=headers)
    print (f"Returned status code: {r.status_code}")
    if r.status_code == 200:
        print("Valid API Key and URL")
    else:
        print("Invalid API Key and/or URL")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Prefect Cloud Login Tester")
    parser.add_argument("--api_key", help="API KEY", required=True)
    parser.add_argument("--account_id", help="Account ID", required=True)
    parser.add_argument("--workspace_id", help="Workspace ID", required=True)
    args = parser.parse_args()

    url = f"https://api.prefect.cloud/api/accounts/{args.account_id}/workspaces/{args.workspace_id}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {args.api_key}'
    }

    check_health(url, headers)