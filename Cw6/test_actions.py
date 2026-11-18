"""ActionChains, keyboard, drag and drop, scrolling, Select."""
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from config import INTERNET_URL

FIGURES = (By.CLASS_NAME, "figure")
PARAGRAPHS = (By.CLASS_NAME, "jscroll-added")
LOADING = (By.CLASS_NAME, "jscroll-loading")

# HTML5 drag and drop simulated with JavaScript events (step 10)
JS_DRAG_AND_DROP = """
const [source, target] = arguments;
const dt = new DataTransfer();
const fire = (el, type) => el.dispatchEvent(new DragEvent(type,
    {bubbles: true, cancelable: true, dataTransfer: dt}));
fire(source, 'dragstart'); fire(target, 'dragenter');
fire(target, 'dragover'); fire(target, 'drop');
fire(source, 'dragend');
"""


def column_headers(driver):
    return [c.text for c in driver.find_elements(By.CLASS_NAME, "column")]


def loaded_paragraphs(driver):
    """Number of paragraphs; -1 while the last one is still loading."""
    if driver.find_elements(*LOADING):
        return -1
    return len(driver.find_elements(*PARAGRAPHS))


# --- step 8: hover -------------------------------------------------------
@pytest.mark.parametrize("number", [1, 2, 3])
def test_hover_shows_caption(driver, number):
    """Step 8: move_to_element(figure) -> caption visible."""
    driver.get(f"{INTERNET_URL}/hovers")
    wait = WebDriverWait(driver, 5)
    wait.until(lambda d: len(d.find_elements(*FIGURES)) == 3)   # page ready
    figure = driver.find_elements(*FIGURES)[number - 1]
    caption = figure.find_element(By.CLASS_NAME, "figcaption")
    assert not caption.is_displayed()
    ActionChains(driver).move_to_element(figure).perform()
    wait.until(EC.visibility_of(caption))
    assert caption.find_element(By.TAG_NAME, "h5").text == f"name: user{number}"


# --- step 9: keyboard and context menu ------------------------------------
# --- step 9: keyboard and context menu ------------------------------------
@pytest.mark.parametrize("key, name", [
    (Keys.TAB, "TAB"),
    (Keys.ESCAPE, "ESCAPE"),
    (Keys.SPACE, "SPACE"),
    ("a", "A"),
], ids=["tab", "esc", "space", "letter"])
def test_keys(driver, key, name):
    """Step 9: send_keys(key) to #target, check #result."""
    driver.get(f"{INTERNET_URL}/key_presses")
    driver.find_element(By.ID, "target").send_keys(key)
    assert driver.find_element(By.ID, "result").text == f"You entered: {name}"

def test_context_menu(driver):
    """Step 9: context_click(#hot-spot) -> alert."""
    driver.get(f"{INTERNET_URL}/context_menu")
    hot_spot = driver.find_element(By.ID, "hot-spot")
    ActionChains(driver).context_click(hot_spot).perform()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    assert alert.text == "You selected a context menu"
    alert.accept()


# --- step 10: drag and drop -----------------------------------------------
@pytest.mark.xfail(strict=False,
                   reason="HTML5 DnD: ActionChains works only "
                          "in some ChromeDriver versions")
def test_drag_and_drop_actionchains(driver):
    driver.get(f"{INTERNET_URL}/drag_and_drop")
    a = driver.find_element(By.ID, "column-a")
    b = driver.find_element(By.ID, "column-b")
    ActionChains(driver).drag_and_drop(a, b).perform()
    assert column_headers(driver) == ["B", "A"]


def test_drag_and_drop_javascript(driver):
    """Step 10: execute_script(JS_DRAG_AND_DROP, a, b)."""
    driver.get(f"{INTERNET_URL}/drag_and_drop")
    a = driver.find_element(By.ID, "column-a")
    b = driver.find_element(By.ID, "column-b")
    driver.execute_script(JS_DRAG_AND_DROP, a, b)
    assert column_headers(driver) == ["B", "A"]


# --- step 11: scrolling and Select ----------------------------------------
def test_scroll_to_footer(driver):
    driver.get(f"{INTERNET_URL}/infinite_scroll")
    wait = WebDriverWait(driver, 15)
    wait.until(lambda d: loaded_paragraphs(d) >= 1)

    def scroll_and_check(d):            # the condition scrolls itself
        footer = d.find_element(By.ID, "page-footer")
        ActionChains(d).scroll_to_element(footer).perform()
        return loaded_paragraphs(d) >= 2

    wait.until(scroll_and_check)


def test_dropdown(driver):
    driver.get(f"{INTERNET_URL}/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 2")
    assert dropdown.first_selected_option.get_attribute("value") == "2"
    dropdown.select_by_value("1")
    assert dropdown.first_selected_option.text == "Option 1"



# --- step 12: element screenshot ------------------------------------------
def test_element_screenshot(driver, tmp_path):
    driver.get(f"{INTERNET_URL}/drag_and_drop")
    file = tmp_path / "column_a.png"
    driver.find_element(By.ID, "column-a").screenshot(str(file))
    assert file.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"