#!/usr/bin/env python3
"""Render the bilingual policy with the existing, dependency-free page design."""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parent


def inline(value):
    value = html.escape(value, quote=True)
    value = re.sub(r"\[([^\]]+)\]\((https://[^)]+|mailto:[^)]+)\)",
                   r'<a href="\2">\1</a>', value)
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)


def article(content, language, label, anchor):
    result = [f'<article id="{anchor}" class="lang-block" lang="{language}">',
              f'<div class="lang-label">{label}</div>', '<section>']
    for block in content.strip().split("\n\n"):
        if block.startswith("### "):
            result.extend(['</section><section>', f'<h2>{inline(block[4:])}</h2>'])
        elif block.startswith("- "):
            rows = block.splitlines()
            if not all(row.startswith("- ") for row in rows):
                raise ValueError("List items must each occupy a single source line")
            result.append('<ul>' + ''.join(f'<li>{inline(row[2:])}</li>' for row in rows) + '</ul>')
        elif block.startswith("#"):
            raise ValueError("Unexpected Markdown heading")
        else:
            result.append(f'<p>{inline(block)}</p>')
    return '\n'.join(result + ['</section>', '</article>'])


def main():
    source = (ROOT / "policy.md").read_text()
    preamble, body = source.split("## 简体中文\n", 1)
    chinese, english = body.split("## English\n", 1)
    date = re.search(r"\*\*(生效日期 Effective date: .+)\*\*", preamble).group(1)
    # Keep the existing brand, typography and responsive CSS in index.html.
    head = (ROOT / "index.html").read_text().split("<body>", 1)[0]
    page = head + '<body>\n<div class="wrap">\n<header>\n' \
        + '<div class="brand">Motoo</div>\n<h1>隐私政策 · Privacy Policy</h1>\n' \
        + f'<p class="effective">{inline(date)}</p>\n' \
        + '<nav class="lang-nav" aria-label="Language"><a href="#zh">简体中文</a><a href="#en">English</a></nav>\n' \
        + '</header>\n<main>\n' \
        + article(chinese, "zh-CN", "简体中文", "zh") + '\n' \
        + article(english, "en", "English", "en") + '\n' \
        + '</main>\n<footer>Motoo · Privacy Policy</footer>\n</div>\n</body>\n</html>\n'
    if '<script' in page.lower():
        raise ValueError("The policy page must not embed scripts")
    (ROOT / "index.html").write_text(page)
    print("Generated index.html from policy.md")


if __name__ == "__main__":
    main()
