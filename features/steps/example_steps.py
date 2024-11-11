from behave import given, when, then
from src.pages.example_page import ExamplePage

@given('I am on the Google homepage')
def step_impl(context):
    context.page = ExamplePage(context.driver)
    context.page.open()

@when('I search for "{query}"')
def step_impl(context, query):
    context.page.search(query)

@then('I should see search results')
def step_impl(context):
    results_stats = context.page.get_results_stats()
    assert "results" in results_stats.lower()
