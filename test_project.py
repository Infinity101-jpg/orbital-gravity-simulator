import unittest
import project  # your main file

class TestProject(unittest.TestCase):

    def setUp(self):
        # Reset to default before each test
        project.ApplyPreset("Preset A")

    def test_apply_preset_changes_values(self):
        """Preset A should correctly update global variables."""
        project.ApplyPreset("Preset A")

        self.assertEqual(project.Obj_1_col, "PINK")
        self.assertEqual(project.Obj_2_col, "TEAL")
        self.assertEqual(project.Obj_1_radius, 10)
        self.assertEqual(project.Obj_2_radius, 30)

        self.assertEqual(project.Obj_1_coords, [-150.0, 100.0])
        self.assertEqual(project.Velocity1, [.5, .9])

    def test_apply_preset_B(self):
        """Preset B should load correct values."""
        project.ApplyPreset("Preset B")

        self.assertEqual(project.Obj_1_col, "BLUE")
        self.assertEqual(project.Obj_2_col, "RED")
        self.assertEqual(project.Obj_1_radius, 10)
        self.assertEqual(project.Obj_2_radius, 30)

        self.assertEqual(project.Obj_1_coords, [-150.0, 0.0])
        self.assertEqual(project.Velocity1, [0, .5])

    def test_update_coords_and_vel_runs(self):
        """Ensure physics update runs without crashing."""
        old_pos1 = project.Obj_1_coords.copy()
        old_pos2 = project.Obj_2_coords.copy()

        project.Update_coords_and_vel()

        # Object 1 should always move at least a tiny bit
        self.assertNotEqual(old_pos1, project.Obj_1_coords)

        # Object 2 may or may not move depending on preset
        self.assertEqual(len(project.Obj_2_coords), 2)

    def test_velocity_changes(self):
        """Velocity should change after update."""
        old_v1 = project.Velocity1.copy()
        old_v2 = project.Velocity2.copy()

        project.Update_coords_and_vel()

        self.assertNotEqual(old_v1, project.Velocity1)
        self.assertNotEqual(old_v2, project.Velocity2)

    def test_all_presets_load(self):
        """Ensure every preset loads without errors."""
        for name in project.PRESETS.keys():
            project.ApplyPreset(name)
            self.assertEqual(project.Obj_1_col, project.PRESETS[name]["Obj_1_col"])
            self.assertEqual(project.Obj_2_col, project.PRESETS[name]["Obj_2_col"])

if __name__ == "__main__":
    unittest.main()
