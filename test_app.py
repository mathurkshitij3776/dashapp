# --- ADDED: Auto-install ChromeDriver ---
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  # This downloads the correct driver for your Chrome version
# ----------------------------------------

from app import app
from dash.testing.application_runners import import_app

def test_app_layout(dash_duo):
    
    # Start the app
    dash_duo.start_server(app)

    # Test 1: Verify Header
    try:
        dash_duo.wait_for_element("h1", timeout=4)
        print("\n[PASS] Header component found.")
    except Exception:
        print("\n[FAIL] Header component NOT found.")

    # Test 2: Verify Visualization
    try:
        dash_duo.wait_for_element("#sales-line-chart", timeout=4)
        print("[PASS] Visualization graph found.")
    except Exception:
        print("[FAIL] Visualization graph NOT found.")

    # Test 3: Verify Region Picker
    try:
        dash_duo.wait_for_element("#region-selector", timeout=4)
        print("[PASS] Region picker found.")
    except Exception:
        print("[FAIL] Region picker NOT found.")

    # Optional Assertion
    assert dash_duo.find_element("h1").text == "Soul Foods Sales Visualizer"