"""This module contains a class abstraction of xkcd's About page. Note that the current
implementation is restricted only to the elements needed by the existing auto tests."""
from typing import List

from playwright.sync_api import Locator, Page

from ui.main_page import XKCD_MAIN_PAGE_URL

XKCD_ABOUT_PAGE_URL = XKCD_MAIN_PAGE_URL + "about/"


class AboutPageVerifications:
    """This class contains common assertions within the About page."""

    def __init__(self, about_page):
        self.about_page = about_page

    def all_sections_are_visible(self):
        """Verifies that all sections on the About page are visible."""
        assert all(
            [
                self.about_page.main_page_link.is_visible(),
                self.about_page.who_are_you_section.is_visible(),
                self.about_page.what_do_you_do_section.is_visible(),
                self.about_page.back_to_main_link.is_visible(),
            ]
        ), "Some section on the About page is missing!"


class AboutPage:
    """This class serves a page object for the xkcd About page."""

    def __init__(self, page: Page):
        self.page = page
        self.main_page_link = page.locator(f'center a[href="{XKCD_MAIN_PAGE_URL}"]')
        self.who_are_you_section = page.get_by_text("Who are you?")
        self.what_do_you_do_section = page.get_by_text("What else do you do?")
        # You get the idea, so I won't add all section headers
        self.back_to_main_link = page.locator('center > a[href="/"]')

    def navigate(self):
        """Navigates to the about page via the URL."""
        self.page.goto(XKCD_ABOUT_PAGE_URL)

    @property
    def assert_that(self) -> AboutPageVerifications:
        """Returns an instance of the AboutPageVerifications to allow for assertion invocations
        common for the About page."""
        return AboutPageVerifications(about_page=self)
