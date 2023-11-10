import requests
import json

# API endpoints
get_templates_url = "https://api.frontegg.com/identity/resources/mail/v1/configs/templates"
update_template_url = "https://api.frontegg.com/identity/resources/mail/v1/configs/templates"

# API tokens
fromEnvVendorJWT = "{YOUR_FROM_ENV_VENDOR_JWT}"
toEnvVendorJWT = "{YOUR_TO_ENV_VENDOR_JWT}"

# Headers for the GET request
get_headers = {
    "Authorization": f"Bearer {fromEnvVendorJWT}"
}

# Headers for the POST request
post_headers = {
    "Authorization": f"Bearer {toEnvVendorJWT}",
    "Content-Type": "application/json"
}

# GET request to retrieve all templates
response = requests.get(get_templates_url, headers=get_headers)

# Check if the GET request was successful
if response.status_code == 200:
    templates = response.json()

    for template in templates:
        # Extract the necessary fields
        data_to_update = {
            "type": template["type"],
            "redirectURL": template["redirectURL"],
            "senderEmail": template["senderEmail"],
            "htmlTemplate": template["htmlTemplate"],
            "subject": template["subject"],
            "fromName": template["fromName"],
            "active": template["active"],
            "successRedirectUrl": template["successRedirectUrl"],
            "redirectUrlPattern": template["redirectURLPattern"],
            "successRedirectUrlPattern": template["successRedirectUrlPattern"]
        }

        update_response = requests.post(
            url=update_template_url,
            headers=post_headers,
            data=json.dumps(data_to_update)
        )

        if update_response.status_code == 201:
            print(f"Template '{template['type']}' updated successfully.")
        else:
            print(f"Failed to update template '{template['type']}'. Status code: {update_response.status_code}")
else:
    print("Failed to retrieve templates. Status code:", response.status_code)
