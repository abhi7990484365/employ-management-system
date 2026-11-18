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


def _add(page: Page, name: str, email: str):
    page.goto("http://127.0.0.1:8000")
    page.get_by_label("Full name").fill(name)
    page.get_by_label("Email address").fill(email)
    page.get_by_label("Department").fill("Engineering")
    page.get_by_role("button", name="Save employee").click()
    expect(page.get_by_role("cell", name=name)).to_be_visible()


def test_delete_cancelled_keeps_employee(page: Page):
    _add(page, "Cancel Case", "cancel.case@example.com")
    requests = []
    page.on("request", lambda r: requests.append(r) if r.method == "DELETE" else None)
    page.once("dialog", lambda d: d.dismiss())
    page.get_by_role("row", name="Cancel Case").get_by_role("button", name="Delete").click()
    expect(page.get_by_role("cell", name="Cancel Case")).to_be_visible()
    assert requests == []


def test_delete_confirmed_removes_employee(page: Page):
    _add(page, "Confirm Case", "confirm.case@example.com")
    page.once("dialog", lambda d: d.accept())
    page.get_by_role("row", name="Confirm Case").get_by_role("button", name="Delete").click()
    expect(page.get_by_role("cell", name="Confirm Case")).to_have_count(0)
