
### Go to command line
```
cd heroku-telegram-bot
heroku login
heroku create --region eu appname # create app in eu region, common regions: eu, us
heroku addons:create heroku-redis:hobby-dev -a appname # (Optionaly) installing redis
heroku buildpacks:set heroku/python # set python buildpack
git push heroku master # deploy app to heroku
heroku config:set TELEGRAM_TOKEN=123456789:AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLL # set config vars, insert your own
heroku config:set SOME_API_TOKEN=qwertyuiop1234567890
                ...
heroku ps:scale bot=1 # start bot dyno
heroku logs --tail # If for some reason it’s not working, check the logs
heroku ps:stop bot #stop bot dyno
```


