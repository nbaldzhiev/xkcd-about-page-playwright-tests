# xkcd About page automated UI tests

The repository contains a small project in Python and Playwright for creating a few automated tests for the About page of the xkcd website.

## Usage

```
$ git clone git@github.com:nbaldzhiev/xkcd-about-page-playwright-tests.git && cd xkcd-about-page-playwright-tests
$ python3.8 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
$ pytest
```

This would execute all tests within the directory using the default Playwright settings for the Pytest plugin, i.e. headless mode, Chromium browser.

## Notable external packages used

* [Playwright](https://playwright.dev/python/) - providing Playwright bindings for Python;
* [pytest](https://docs.pytest.org/) - pytest.
