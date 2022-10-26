"""This module serves as the conftest for the tests/ package."""
import pytest
from playwright.sync_api import Page

from ui import AboutPage, MainPage


@pytest.fixture
def xkcd_main_page(page: Page) -> MainPage:
    """Opens the xkcd main page and returns it as MainPage object."""
    main_page = MainPage(page=page)
    main_page.navigate()
    return main_page


@pytest.fixture
def xkcd_about_page(page: Page) -> AboutPage:
    """Opens the xkcd About page and returns it as a AboutPage."""
    about_page = AboutPage(page=page)
    about_page.navigate()
    return about_page
