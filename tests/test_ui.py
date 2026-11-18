from playwright.sync_api import Page, expect

def test_add_and_search_employee(page: Page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_label("Full name").fill("Jamie Taylor")
    page.get_by_label("Email address").fill("jamie@example.com")
    page.get_by_label("Department").fill("Engineering")
    page.get_by_role("button", name="Save employee").click()
    expect(page.get_by_role("cell", name="Jamie Taylor")).to_be_visible()
    page.get_by_role("searchbox", name="Search employees").fill("Jamie")
    expect(page.get_by_role("cell", name="Jamie Taylor")).to_be_visible()
