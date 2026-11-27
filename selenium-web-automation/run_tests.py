"""Test runner for Project 04 — runs the unittest suite with per-test timings.

Usage (from selenium-web-automation/):
    ../venv/bin/python run_tests.py
Exit code 0 = all tests passed.
"""
import sys
import time
import unittest


class TimedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.durations = {}

    def startTest(self, test):
        self._t0 = time.time()
        super().startTest(test)

    def stopTest(self, test):
        self.durations[str(test)] = round(time.time() - self._t0, 1)
        super().stopTest(test)


if __name__ == "__main__":
    sys.path.insert(0, "tests")
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2, resultclass=TimedResult)
    started = time.time()
    result = runner.run(suite)
    print()
    print("Per-test durations (seconds):")
    for name, secs in result.durations.items():
        print(f"  {secs:>6}  {name}")
    print(f"Total suite time: {round(time.time() - started, 1)} s")
    print(
        f"Ran {result.testsRun} tests — "
        f"{len(result.failures)} failed, {len(result.errors)} errors, "
        f"{len(result.skipped)} skipped"
    )
    sys.exit(0 if result.wasSuccessful() else 1)
