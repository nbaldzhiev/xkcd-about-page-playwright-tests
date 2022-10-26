"""This module contains a class abstraction of xkcd's main page. Note that the current
implementation is restricted only to the elements needed by the existing auto tests."""
from typing import List

from playwright.sync_api import Locator, Page

XKCD_MAIN_PAGE_URL = "https://xkcd.com/"


class MainPage:
    """This class serves a page object for the xkcd main page."""

    def __init__(self, page: Page):
        self.page = page
        self.nav_menu_links = page.locator("#topContainer > #topLeft li > a")

    def navigate(self):
        """Navigates to the main page via the URL."""
        self.page.goto(XKCD_MAIN_PAGE_URL)

    @property
    def navigation_menu_link_names(self) -> List[str]:
        """Returns the available links in the navigation menu as a list of strings where each
        element is a link name."""
        return [
            self.nav_menu_links.nth(i).text_content()
            for i in range(self.nav_menu_links.count())
        ]

    def get_link_by_name(self, link_name: str) -> Locator:
        """Gets and returns a given link as a Locator object, specified by link_name, i.e. 'About'
        would return the <a> tag for the About link as a Locator object."""
        assert link_name.lower() in [
            name.lower() for name in self.navigation_menu_link_names
        ], f"No link found with name {link_name}!"
        return list(
            filter(
                lambda link: link.text_content().lower() == link_name.lower(),
                [
                    self.nav_menu_links.nth(i)
                    for i in range(self.nav_menu_links.count())
                ],
            )
        )[0]
