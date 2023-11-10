# frontegg - Sync your email templates between environments

1) Download python script
2) Install requests - pip3 install requests
3) Create your from and to JWT keys - https://docs.frontegg.com/reference/authenticate_vendor
     - Your from should be the source environment. For example, development
     - Your to should be the release environment (where you want the templates to reside). For example, stage
5) Replace {YOUR_FROM_ENV_VENDOR_JWT} and {YOUR_TO_ENV_VENDOR_JWT} with your from and to token generated in step 3.
6) Run script!
