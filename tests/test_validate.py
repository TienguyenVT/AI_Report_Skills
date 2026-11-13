"""Exercise failure detection using isolated copies, without changing the package."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_validator", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "package"
        shutil.copytree(ROOT, self.repo,
                        ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv", "venv"))

    def test_current_package(self):
        self.assertEqual(validator.validate(self.repo), [])

    def test_missing_docx_reference_is_detected(self):
        (self.repo / "skills/ai-report-formatting/references/docx-preservation.md").unlink()
        self.assertTrue(any("broken link" in x for x in validator.validate(self.repo)))

    def test_marketplace_version_drift_is_detected(self):
        file = self.repo / ".claude-plugin/marketplace.json"
        data = json.loads(file.read_text(encoding="utf-8"))
        data["plugins"][0]["version"] = "99.0.0"
        file.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("version mismatch" in x for x in validator.validate(self.repo)))

    def test_source_outside_package_is_rejected(self):
        file = self.repo / ".agents/plugins/marketplace.json"
        data = json.loads(file.read_text(encoding="utf-8"))
        data["plugins"][0]["source"]["path"] = "../"
        file.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("escapes package" in x for x in validator.validate(self.repo)))

    def test_private_report_is_detected(self):
        (self.repo / "unpublished.docx").write_bytes(b"synthetic test content")
        self.assertTrue(any("Private artifact" in x for x in validator.validate(self.repo)))


if __name__ == "__main__":
    unittest.main()
