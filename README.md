# CrescendoTest
Create a basic line bot with command below:
 - My name: reply to this user’s LINE profile name
 - Last engaged: the last time this user sent a message to this bot (in time format)
 - Count: returns how many messages this user has sent to this bot so far

All commands above are case insensitive, and the bot will echo the message if receiving other input.

I deploy my bot on heroku, take a try by following "@016qqjmv".

To build your own LINE BOT, follow steps below:
 1. Create a LINE developer account and build your own bot at https://developers.line.biz/en/services/messaging-api/. Choose "Create a Messaging API channel" on https://developers.line.biz/console/provider/_id. Once the bot is built, you can get `Channel secret` under "Basic settings" and `Channel access token` under "Messaging API", we will need them later.
 2. Create a heroku account if you don't have one on https://devcenter.heroku.com/. Take a look on https://devcenter.heroku.com/articles/getting-started-with-python will help if you never use heroku before. Remember to install heroku CLI on your pc and login with command `heroku login`.
 3. Clone the repo to your local. Install git first if you don't have it on your pc.
 4. Move into the dir of project by `cd /your_path/CrescendoTest`.
 5. Start a heroku app with command `heroku create`.
 6. Lets set up environment parameters on heroku first. Use<br/>`heroku config:set CHANNEL_SECRET=<YOUR CHANNEL SECRET>`<br/>`heroku config:set CHANNEL_ACCESS_TOKEN=<YOUR CHANNEL ACCESS TOKEN>`<br/>
 The values of parameters are what we got when create the LINE bot.
 7. It's time to run our bot on heroku. Type<br/>`git push heroku main`<br/> in your cmd tool, it will take a few seconds to build the app.
 8. Open our app on web by `heroku open`. Here we can get our domain name. Add `/hello-world` on the url and we should see "Hello" on the browser. If everything is fine, paste your domain name to "Webhook URL" under https://developers.line.biz/console/channel/_id/messaging-api and add `/api/v1/line-bot-webhook`, turn on "Use webhook" button and disable "Auto-reply messages" below. Now we have our LINE BOT connected.
 9. Time to take a try. You can follow the bot we just create on https://developers.line.biz/console/channel/_id/messaging-api.
