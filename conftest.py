import pytest
from pathlib import Path
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    page.goto("https://www.saucedemo.com/")
    return LoginPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            screenshot_name = (
                item.nodeid
                .replace("::", "_")
                .replace("/", "_")
                .replace("\\", "_")
                .replace("[", "_")
                .replace("]", "_")
            )

            screenshot_path = screenshots_dir / f"{screenshot_name}.png"

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            pytest_html = item.config.pluginmanager.getplugin("html")

            if pytest_html:
                extra = getattr(report, "extras", [])
                extra.append(
                    pytest_html.extras.image(
                        str(screenshot_path)
                    )
                )
                report.extras = extra