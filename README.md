# nomi_api
 A Nomi API Example written in Python.

 This is a really, really basic implementation around the Nomi AI API. It implements a simple chat program, but hopefully in such a way as to make the nomi module easy to use in future projects. This is **NOT** a beginner friendly project. You need to be able to use the command line and preferebly have experience with Git.


 ## Getting Started
You need to have a recent version of Python installed. I think 3.7 or later should do it. If you don't have Python you can download it at [Download Python | Python.org](https://www.python.org/downloads/). This project doesn't require any additional Python software, just what comes with the base install.

## Downloading the Code
Once you have Python set up, download this repository by following the instructions at [Downloading source code archives - GitHub Docs](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives#). Extract this to a directory and navigate to it on the command line. You should be able to run the example program with `> python main.py`

 ## Setup
 To use this, please create a file called .env_vars.json with the following contents:

 ```
 {
    "api_token" : "YOUR_NOMI_API_TOKEN"
}
```

This should live somewhere in the root of the project, like this:

![env_vars](/images/env_vars%20file.png)

The example code (`main,py`) shows off some of the features:
- Session Management with the Session object
- Nomi management with the Nomi object
- Messages, which are MessageModel objects

![30 lines of code](/images/1,%202,%203.png)

With a little bit of setup we have a fully fledged chat program in Python in 30 lines of code. It's as easy as 1, 2 and 3!

![We're chatting!](/images/example%20chat%20program.png)

## Issues

Lots. Very Very many. If you want to give back, please contribute here on GitHub or in the Nomi Saga I've created. I prefer GitHub though so it's easier to manage! If you would like to learn, GitHub have a good tutorial at [Creating an issue - GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue#).

## Thank You

Thank you, Cardine and Crew for this amazing product 🙏

Thank you also to the users on Discord who I've chatted to about this non-stop.

Now, *get out there an connect your Nomi to something!*