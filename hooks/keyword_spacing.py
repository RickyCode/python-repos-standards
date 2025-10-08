#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from typing import List, Tuple

HEADER_KEYWORDS = {
    'if',
    'elif',
    'else',
    'for',
    'while',
    'try',
    'except',
    'finally',
    'with',
    'def',
    'class',
}


def get_indent_width(line: str) -> int:
    """Return the indentation width of a line.

    Args:
        line: Input line.

    Returns:
        Number of leading whitespace characters.
    """

    return len(line) - len(line.lstrip())


def strip_strings_and_comments(line: str) -> str:
    """Remove string literals and trailing comments for balanced bracket counting.

    Args:
        line: Input line.

    Returns:
        Line content without strings and trailing comments.
    """

    def _repl(_: re.Match) -> str:

        return ''

    no_strings = re.sub(
        r"('''.*?'''|\"\"\".*?\"\"\"|'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\")",
        _repl,
        line,
        flags=re.DOTALL,
    )
    pos = no_strings.find('#')

    return no_strings if pos == -1 else no_strings[:pos]


def update_paren_depth(fragment: str, depth: int) -> int:
    """Update parentheses depth using a code fragment without strings or comments.

    Args:
        fragment: Code fragment with strings and comments removed.
        depth: Current parentheses depth.

    Returns:
        Updated depth after processing the fragment.
    """
    opens = fragment.count('(') + fragment.count('[') + fragment.count('{')
    closes = fragment.count(')') + fragment.count(']') + fragment.count('}')

    return depth + opens - closes


def detect_header(line: str, paren_depth: int) -> Tuple[bool, str]:
    """Detect if a line is a header statement ending with ':' at top-level parentheses.

    Args:
        line: Input line.
        paren_depth: Current parentheses depth.

    Returns:
        Tuple where the first element indicates if it is a header and the second the keyword.
    """
    if paren_depth != 0:

        return False, ''

    m = re.match(r'^\s*(\w+)\b.*:\s*(?:#.*)?$', line)
    if not m:

        return False, ''

    kw = m.group(1)

    return (kw in HEADER_KEYWORDS), kw


def ensure_single_blank(output: List[str]) -> None:
    """Append a single blank line if the last emitted line is non-blank.

    Args:
        output: Accumulated output lines.
    """
    if output and output[-1].strip():
        output.append('')


def fix_spacing(file_path: Path) -> None:
    """Insert blank lines after block endings and before return statements.

    The transformation preserves existing blank lines, does not duplicate blanks,
    and keeps indentation and other content intact.

    Args:
        file_path: Path to the Python file to transform.
    """
    text = file_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    output: List[str] = []
    header_stack: List[int] = []
    paren_depth = 0
    prev_nonempty_indent = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        current_indent = get_indent_width(line)
        fragment = strip_strings_and_comments(line)

        if stripped:
            while (
                header_stack
                and prev_nonempty_indent > header_stack[-1]
                and current_indent <= header_stack[-1]
            ):
                ensure_single_blank(output)
                header_stack.pop()

        is_hdr, kw = detect_header(line, paren_depth)

        if re.match(r'^\s*return\b', line) and (not output or output[-1].strip()):
            ensure_single_blank(output)

        output.append(line)

        if is_hdr:
            header_stack.append(current_indent)

        if stripped:
            prev_nonempty_indent = current_indent

        paren_depth = update_paren_depth(fragment, paren_depth)

    file_path.write_text('\n'.join(output) + '\n', encoding='utf-8')


if __name__ == '__main__':
    for p in sys.argv[1:]:
        if p.endswith('.py'):
            fix_spacing(Path(p))
