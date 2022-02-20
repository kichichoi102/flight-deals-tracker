# flight-deals-tracker

Leverages `Tequila Search API` to search for cheap flights to chosen destinations!

If a user writes the destination cities and their starting city, this app does the rest and sends you sms/email notifications if a cheap flight is available!

## Setup Sheety
1. Create a new sheet on Google Sheets
2. Create two tables, similar to [this](https://docs.google.com/spreadsheets/d/1o3EmMlISDeuvhoOdPRDkIv2RROZ0eNWy1RWQjHWrEiE/edit?usp=sharing)
3. Connect Google Sheet to [Sheety](https://sheety.co/)
4. Get share link from Google Sheet and paste to Sheety new project
5. Allow `GET` and `POST`
6. Copy `POST URL` and add to `SHEET_ENDPOINT` in `.env`
7. Create a new Token (Authentication -> Bearer).
8. Paste `{Authorization: Bearer <your token>}` into `.env`

## Setup Twilio
Twilio supports HTTP Basic authentication. This allows you to protect the URLs on your web server so that only you and Twilio can access them.
1. Go to [Twilio Console](https://console.twilio.com)
2. Create a trial account
3. Get the `Account SID` and the `Auth Token`.
4. Write these to `ACCOUNT_SID` and `AUTH_TOKEN` respectively in the `.env` file.
5. Create a new number and write to `FROM_NUMBER` in `.env`
6. Write any phone number you want to write sms to in `TO_NUMBER`

## Setup SMTP
1. Create a new (or your own) gmail account
2. In your Google/Gmail account, go to Settings
3. Select the `Forwarding and POP/IMAP` settings
4. Under the `IMAP access` section, toggle on the option to `Enable IMAP`.
5. Go to `Google Account`
6. `Security` -> `Less secure app access` -> `Turn on access`
7. Write `email` and `password` to .env `SOURCE_MAIL_ADDRESS` and `PASSWORD` respectively in `.env`
`NOTE: Please only do this if you feel safe with giving unsecure access to the app`

## Setup Tequila API
1. Go to [Tequila Login](https://tequila.kiwi.com/portal/login) and create a new account
2. Allow `Meta Search`
3. Go to [Search API], get the `search endpoint` and paste this into `SEARCH_KEY` in `.env`

## Additional info
In `.env` write `START_LOCATION` and `START_CITY`

Thats it!
