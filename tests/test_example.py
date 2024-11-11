from src.pages.example_page import ExamplePage

def test_google_search(driver):
    page = ExamplePage(driver)
    page.open()
    page.search("Selenium with Python")
    assert "results" in page.get_results_stats().lower()
