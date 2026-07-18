import os
import sys
import traceback
import importlib

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
sys.path.append(os.path.dirname(__file__))
def run_test_file(path):
    module_name = os.path.splitext(os.path.basename(path))[0]
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"{RED}ERROR importing {module_name}: {e}{RESET}")
        return

    tests_run = 0
    tests_failed = 0

    for name in dir(module):
        if name.startswith("test_"):
            func = getattr(module, name)
            if callable(func):
                tests_run += 1
                try:
                    func()
                    print(f"{GREEN}PASS{RESET} {module_name}.{name}")
                except Exception:
                    tests_failed += 1
                    print(f"{RED}FAIL{RESET} {module_name}.{name}")
                    traceback.print_exc()

    return tests_run, tests_failed


def main():
    test_files = [f for f in os.listdir() if f.startswith("test_") and f.endswith(".py")]

    if not test_files:
        print("No test_*.py files found.")
        return

    total_run = 0
    total_failed = 0

    for tf in test_files:
        print(f"\nRunning {tf}...")
        run, fail = run_test_file(tf)
        total_run += run
        total_failed += fail

    print("\n====================")
    print(f"Tests run: {total_run}")
    print(f"Tests failed: {total_failed}")
    print("====================")

    sys.exit(1 if total_failed else 0)


if __name__ == "__main__":
    main()
