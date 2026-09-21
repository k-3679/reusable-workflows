import os
import re
import subprocess
import sys

CATEGORIES = ("Added", "Changed", "Deprecated", "Removed", "Fixed", "Security")
MIN_WORDS = 3

UNRELEASED = re.compile(r"^## \[Unreleased\]\n(.*?)(?=\n## |\Z)", re.DOTALL | re.MULTILINE)
CATEGORY = re.compile(r"^### (.+)$")
WORD = re.compile(r"\w")


def extract_unreleased(text):
    match = UNRELEASED.search(text)
    if not match:
        return None, 0
    return match.group(1), text.count("\n", 0, match.start()) + 1


def split_categories(body):
    sections = [{"line": 0, "name": None, "lines": []}]
    for offset, line in enumerate(body.split("\n")):
        if not line.strip():
            continue
        match = CATEGORY.match(line)
        if match:
            sections.append({"line": offset, "name": match.group(1), "lines": []})
        else:
            sections[-1]["lines"].append((offset, line))
    return sections


def validate_categories(sections):
    errors = []
    seen = set()
    for section in sections:
        name = section["name"]
        if name is None:
            errors += [(offset, "entry outside a category, add a '### <Category>' heading above it") for offset, _ in section["lines"]]
        elif name not in CATEGORIES:
            errors.append((section["line"], f"unknown category '### {name}', use one of: {', '.join(CATEGORIES)}"))
        elif name in seen:
            errors.append((section["line"], f"duplicate category '### {name}'"))
        elif not section["lines"]:
            errors.append((section["line"], f"empty category '### {name}'"))
        seen.add(name)
    if len(sections) == 1:
        errors.append((0, "no category, group entries under '### <Category>' headings"))
    return errors


def collect_entries(lines):
    entries = []
    errors = []
    for offset, line in lines:
        if line.startswith("- "):
            entries.append([offset, line[2:]])
        elif line[0].isspace() and entries:
            entries[-1][1] += " " + line.strip()
        elif line[:2] in ("* ", "+ "):
            errors.append((offset, "use '- ' for entries"))
        else:
            errors.append((offset, "not a bullet entry"))
    return entries, errors


def validate_entry(text):
    words = [word for word in text.split() if WORD.search(word)]
    if len(words) < MIN_WORDS:
        return f"entry too short, describe the change in at least {MIN_WORDS} words"
    return None


def validate_body(body):
    sections = split_categories(body)
    errors = validate_categories(sections)
    for section in sections:
        if section["name"] is None:
            continue
        entries, entry_errors = collect_entries(section["lines"])
        errors += entry_errors
        for offset, text in entries:
            message = validate_entry(text)
            if message:
                errors.append((offset, message))
    return sorted(errors)


def unreleased_at(base_sha, changelog_file):
    result = subprocess.run(["git", "show", f"{base_sha}:{changelog_file}"], capture_output=True, text=True)
    if result.returncode != 0:
        return ""
    body, _ = extract_unreleased(result.stdout)
    return body or ""


def error(changelog_file, line, message):
    print(f"::error file={changelog_file},line={line}::{message}")


def main():
    changelog_file = os.environ["CHANGELOG_FILE"]
    base_sha = os.environ.get("EFFECTIVE_BASE_SHA", "")

    with open(changelog_file, encoding="utf-8") as f:
        body, heading_line = extract_unreleased(f.read())

    if body is None:
        error(changelog_file, 1, "could not find an '## [Unreleased]' section")
        sys.exit(1)

    if not body.strip():
        error(changelog_file, heading_line, "the [Unreleased] section is empty, add an entry describing your change")
        sys.exit(1)

    errors = validate_body(body)
    for offset, message in errors:
        error(changelog_file, heading_line + 1 + offset, message)
    if errors:
        sys.exit(1)

    if base_sha and body.strip() == unreleased_at(base_sha, changelog_file).strip():
        error(changelog_file, heading_line, "the [Unreleased] section was not updated by this push, add an entry describing your change")
        sys.exit(1)


if __name__ == "__main__":
    main()
