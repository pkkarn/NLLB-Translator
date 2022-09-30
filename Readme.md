# NLLB 200 Translator.

Steps to setup.

- Install Python and `pipenv` for virtual environment
- Clone this package.
- Inside /NLLB-Translator, install all dependencies using `pipenv install -r requirements. txt`.

Once your package is installed.
- Run server using `python manage.py runserver` e.g http://localhost:8000

Test your endpoint at http://localhost:8000/ed

```
method: 'POST',

body: {
    "input": "how are you",
    "src": "eng_Latn",
    "tgt": "hin_Deva"
}

response: "आप कैसे हैं"
```