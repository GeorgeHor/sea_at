from pages.the_one_page import SetupInProgressPage


def test_not_active_user(not_active_user):
    page_the_one = SetupInProgressPage(not_active_user, SetupInProgressPage)
    page_the_one.setup_in_progress_page()
