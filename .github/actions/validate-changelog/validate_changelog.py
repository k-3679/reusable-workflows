import os
import re
import subprocess
import sys

changelog_file = os.environ["CHANGELOG_FILE"]
base_sha = os.environ.get("EFFECTIVE_BASE_SHA", "")


def extract_unreleased(text):
    pattern = re.compile(r"## \[Unreleased\]\n(.*?)(?=\n## \[|\Z)", re.DOTALL)
    match = pattern.search(text)
    # group(1) because we have one (...) capturing group in the pattern.
    # In this case, it returns the body of the [Unreleased] section.
    return match.group(1).strip("\n") if match else None


with open(changelog_file, "r", encoding="utf-8") as f:
    head_content = f.read()

head_unreleased = extract_unreleased(head_content)
if head_unreleased is None:
    print(f"::error::Could not find an '## [Unreleased]' section in {changelog_file}", file=sys.stderr)
    sys.exit(1)

if not head_unreleased.strip():
    print(f"::error::The [Unreleased] section in {changelog_file} is empty. Add an entry describing your change", file=sys.stderr)
    sys.exit(1)

base_unreleased = ""
if base_sha:
    result = subprocess.run(
        ["git", "show", f"{base_sha}:{changelog_file}"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        base_unreleased = extract_unreleased(result.stdout) or ""

if head_unreleased.strip() == base_unreleased.strip():
    print(
        f"::error::The [Unreleased] section in {changelog_file} was not updated by this push. "
        " add an entry describing your change",
        file=sys.stderr,
    )
    sys.exit(1)
