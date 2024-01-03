## Selenium IDE


An OpenSource extension, helps you record and playback test automation for the web.

[5 key points about using Selenium](./doc/5-key-points-selenium.md)

1. follow this [getting-started](https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started) to create your tests
2. save the project, it will create a `.side` file.

You have also a way to run the project in a CLI.
`npm install -g selenium-side-runner`
`npm install -g chromedriver`
`selenium-side-runner /path/to/your-project.side`



## Selenium With Pytest

in Selenium IDE, you can export code in the language of your choice (java, python, javascript, etc ..)

`python -m venv env`
`source env/bin/activate`
`pip install -r requirements.txt`
`pytest test_defaultSuite.py`


## Locust

An open source load testing tool in Python

`locust -f your_locust_file.py --users 100 --spawn-rate 10`

[Locust parameters](./doc/locust.md)

**launching with Docker**:

```bash
docker-compose up -d --build
docker-compose up -d --scale worker=4
docker-compose up -d --build --scale worker=4 --scale chrome-node=4
docker-compose down
```

locust interface : http://localhost:8089
selenium hub interface : http://localhost:4444

> in locust interface, start with users to 5 and spawn rate to 1, and increase it gradually. if you have resources, you can scale workers and chrome nodes.

> in locust interface, you can finally generate a report, here's an [example of report](./doc/report_1704247260.7615547.html)

---
## Source

- https://github.com/SvenskaSpel/locust-plugins/blob/master/examples/webdriver_ex.py
- https://docs.locust.io/en/stable/
- https://hub.docker.com/r/selenium/hub
- https://hub.docker.com/r/selenium/node-chrome
- https://medium.com/@betancourt.francisco/episode-4-testing-your-python-django-apps-performance-4661f5e78f85