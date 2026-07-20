"""
test_project.py

Sanity tests for the 2D Orbital Gravity Simulation.
Compatible with pytest.py runner (no arguments allowed).
"""

import importlib
import sys

MODULE_NAME = "project"   # rename your main file to this


# Load module once
try:
    sim = importlib.import_module(MODULE_NAME)
    print(f"[OK] Imported module '{MODULE_NAME}'")
except Exception as e:
    print(f"[FAIL] Could not import module '{MODULE_NAME}': {e}")
    sys.exit(1)


def test_presets_exist():
    print("Running test_presets_exist...")

    assert hasattr(sim, "PRESETS"), "PRESETS dict is missing"

    expected = {"Preset A", "Preset B", "Preset C", "Preset D", "Preset E", "Preset F"}
    actual = set(sim.PRESETS.keys())

    missing = expected - actual
    assert not missing, f"Missing presets: {missing}"

    print("[OK] All expected presets are present.")


def test_apply_preset_changes_globals():
    print("Running test_apply_preset_changes_globals...")

    name = "Preset A"
    sim.ApplyPreset(name)
    preset = sim.PRESETS[name]

    assert sim.Game_slowdown_percent == preset["Game_slowdown_percent"]
    assert sim.Obj_1_col == preset["Obj_1_col"]
    assert sim.Obj_1_radius == preset["Obj_1_radius"]
    assert sim.Obj_1_weight == preset["Obj_1_weight"]
    assert sim.Obj_1_coords == preset["Obj_1_coords"]
    assert sim.Velocity1 == preset["Velocity1"]

    assert sim.Obj_2_col == preset["Obj_2_col"]
    assert sim.Obj_2_radius == preset["Obj_2_radius"]
    assert sim.Obj_2_weight == preset["Obj_2_weight"]
    assert sim.Obj_2_coords == preset["Obj_2_coords"]
    assert sim.Velocity2 == preset["Velocity2"]

    print("[OK] ApplyPreset updates globals correctly.")


def test_color_map():
    print("Running test_color_map...")

    assert sim.get_color_name(sim.PINK) == "PINK"
    assert sim.get_color_name(sim.TEAL) == "TEAL"
    assert sim.get_color_name(sim.SILVER) == "SILVER"

    unknown = (123, 45, 67)
    assert sim.get_color_name(unknown) == "WHITE"

    print("[OK] get_color_name works correctly.")


def test_main_exists():
    print("Running test_main_exists...")

    assert hasattr(sim, "main"), "main() missing"
    assert callable(sim.main), "main is not callable"

    print("[OK] main() function exists.")
