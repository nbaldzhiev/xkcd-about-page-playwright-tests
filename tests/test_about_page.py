""""""

from playwright.sync_api import expect

from ui import AboutPage, MainPage


class TestAboutPageFunctional:
    """This class contains functional tests for the about page"""

    ABOUT_PAGE_TITLE = "xkcd - A webcomic"

    def test_about_link_is_present_on_main_page(self, xkcd_main_page: MainPage):
        """Verifies that the main page contains the About link."""
        assert (
            "About" in xkcd_main_page.navigation_menu_link_names
        ), "The About link is not present on the left-hand side menu on the main page!"

    def test_about_link_can_be_opened(self, xkcd_main_page: MainPage):
        """Verifies that the About page can be opened via the main page's left-hand side menu."""
        xkcd_main_page.get_link_by_name("About").click()
        expect(xkcd_main_page.page).to_have_title(
            TestAboutPageFunctional.ABOUT_PAGE_TITLE
        )

    def test_about_page_content(self, xkcd_about_page: AboutPage):
        """Verifies that the content of the About page is correct and as expected."""
        xkcd_about_page.assert_that.all_sections_are_visible()
