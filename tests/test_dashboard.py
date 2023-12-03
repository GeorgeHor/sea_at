from pages.dashboard_page import DashboardPage


def test_dashboard_element_and_links(active_user):
    page_dashboard = DashboardPage(active_user, DashboardPage)
    page_dashboard.should_be_dashboard_link()

