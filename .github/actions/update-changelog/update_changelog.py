import os
import re
import sys

changelog_file = os.environ["CHANGELOG_FILE"]
new_version = os.environ["NEW_VERSION"]
new_tag = os.environ["NEW_TAG"]
release_date = os.environ["RELEASE_DATE"]
repo_url = os.environ["REPO_URL"]
fail_on_empty = os.environ["FAIL_ON_EMPTY"].strip().lower() == "true"


def find_unreleased_section(text):
    pattern = re.compile(r"(## \[Unreleased\]\n)(.*?)(?=\n## \[|\Z)", re.DOTALL)
    return pattern.search(text)


with open(changelog_file, "r", encoding="utf-8") as f:
    content = f.read()

match = find_unreleased_section(content)
if not match:
    print(f"::warning::Could not find an '## [Unreleased]' section in {changelog_file}, skipping changelog update", file=sys.stderr)
    print("false")
    sys.exit(0)

# group(2) because we have two (...) capturing groups in the pattern.
# In this case, it returns the body of the [Unreleased] section.
unreleased_body = match.group(2).strip("\n")

if not unreleased_body:
    if fail_on_empty:
        print(f"::error::[Unreleased] section in {changelog_file} is empty, aborting {new_tag} release", file=sys.stderr)
        print("false")
        sys.exit(1)
    print(f"::warning::[Unreleased] section in {changelog_file} is empty, releasing {new_tag} with no changelog entries", file=sys.stderr)

new_section = f"## [Unreleased]\n\n## [{new_version}] - {release_date}\n"
if unreleased_body:
    new_section += f"\n{unreleased_body}\n"

content = content[:match.start()] + new_section + content[match.end():]

prev_tag_match = re.search(r"^\[unreleased\]: .*/compare/(v[\w.\-]+)\.\.\.HEAD", content, re.MULTILINE)
prev_tag = prev_tag_match.group(1) if prev_tag_match else None

new_links = f"[unreleased]: {repo_url}/compare/{new_tag}...HEAD\n"
if prev_tag:
    new_links += f"[{new_version}]: {repo_url}/compare/{prev_tag}...{new_tag}\n"
else:
    new_links += f"[{new_version}]: {repo_url}/releases/tag/{new_tag}\n"

if prev_tag_match:
    content = content[:prev_tag_match.start()] + new_links + content[prev_tag_match.end():]
else:
    content = content.rstrip("\n") + "\n\n" + new_links

with open(changelog_file, "w", encoding="utf-8") as f:
    f.write(content)

print("true")
