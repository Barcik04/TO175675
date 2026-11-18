"""Browser fixture and an automatic screenshot when a test fails."""
import os
import re
from pathlib import Path

import pytest
from selenium import webdriver

SCREENSHOT_DIR = Path(__file__).parent / "screenshots"


@pytest.fixture
def driver():
    """A new Chrome browser for each test."""
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS") == "1":        # no browser window
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(0)          # explicit waits only
    yield drv
    drv.quit()


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    """After a failed test saves a screenshot to screenshots/."""
    report = yield
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            SCREENSHOT_DIR.mkdir(exist_ok=True)
            name = re.sub(r"[^\w.-]", "_", item.name) + ".png"
            try:
                drv.save_screenshot(str(SCREENSHOT_DIR / name))
            except Exception:   # e.g. an open alert – the report
                pass            # matters more than the screenshot
    return report
