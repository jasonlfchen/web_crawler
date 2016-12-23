# web_crawler
This uses python3
Set up virtual enviroment for project:

```
pip install virtualenv
```

Create a simple virtual environmenet for project:

```
cd ..
virtualenv venv
```

Start virtual environment:

```
source venv/bin/activate
```

Go back to src folder and install dependencies:

```
cd web_crawler
pip install -r requirements.txt
```

To run scraper:

```
scrapy runspider scraper.py
```
