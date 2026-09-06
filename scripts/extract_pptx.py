#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract all text from a PPTX (slides, groups, tables) to a plain-text file.

Usage:
    python3 extract_pptx.py <input.pptx> <output.txt>

Needs python-pptx (PEP 668 hosts: create a venv first, see SKILL.md §4).
"""
import sys
sys.path  # noqa — clarity only; script is run as __main__

try:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
except ImportError:
    sys.stderr.write("python-pptx not installed.\n")
    sys.exit(2)

MODES = {
    "5.1": "PowerShell 5.1 detected — UTF-8 byte mode required (see ima skill rules).",
}


def walk(shapes, lines, depth=0):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            walk(sh.shapes, lines, depth + 1)
            continue
        if sh.has_text_frame:
            txt = "\n".join(p.text for p in sh.text_frame.paragraphs if p.text.strip())
            if txt.strip():
                lines.append(("  " * depth) + txt)
        if sh.shape_type == MSO_SHAPE_TYPE.TABLE:
            try:
                for row in sh.table.rows:
                    lines.append(" | ".join(c.text.strip() for c in row.cells))
            except Exception:
                pass
        if getattr(sh, "has_table", False) and sh.has_table:
            try:
                for row in sh.table.rows:
                    lines.append(" | ".join(c.text.strip() for c in row.cells))
            except Exception:
                pass


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python3 extract_pptx.py <input.pptx> <output.txt>\n")
        sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    try:
        prs = Presentation(src)
    except Exception as e:
        sys.stderr.write(f"Failed to open {src}: {e}\n")
        sys.exit(1)

    lines = []
    for idx, slide in enumerate(prs.slides, 1):
        lines.append(f"\n===== SLIDE {idx} =====")
        walk(slide.shapes, lines)

    text = "\n".join(lines)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extracted {len(lines)} lines, {len(text)} chars -> {out}")


if __name__ == "__main__":
    main()