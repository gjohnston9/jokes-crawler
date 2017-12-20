### Jokes-crawler

This crawler pulls the latest submissions from r/Jokes and saves them to a Postgres table. These are the jokes used in the [Humor Genome Project website](https://github.com/greg9381/humor-genome-website).

Before running, create a `credentials.json` file with the following format. If you don't have a client ID or secret, create a new application [here](https://www.reddit.com/prefs/apps).
```
{
	"db" : {
		"user": "postgres username (default: postgres)",
		"password": "postgres password"
	},
	"reddit" : {
		"reddit_username": "your Reddit username (used as part of PRAW user agent)",
		"client_id": "your client id",
		"client_secret": "your client secret"
	}
}
```