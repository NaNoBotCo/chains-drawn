"""Wrap page.html (the artifact body) into docs/index.html with the head GitHub Pages needs."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
page = (root / "page.html").read_text()
title = re.search(r"<title>(.*?)</title>", page).group(1)
page = page.replace(f"<title>{title}</title>\n", "", 1)
url = "https://nanobotco.github.io/chains-drawn/"
desc = "ChainsAtlas and the other ways blockchains talk, as toys: a stove in every town, recipe cards with fingerprints, a planner's levers, crooked judges, a mule pen and a key rack. English and Thai."
head = f"""<!doctype html>
<html lang="en" translate="no" class="notranslate">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="google" content="notranslate">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="NaNoBotCo">
<meta property="og:title" content="Chains, Drawn · โซ่ วาดให้ดู">
<meta property="og:description" content="Carry the mule, or carry the stove? ChainsAtlas and its cousins, as toys. · จูงล่อข้ามไป หรือแบกเตาไปเอง">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{url}card.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Five towns across a creek, a stove in each, with the words Chains, Drawn in English and Thai.">
<meta property="og:locale" content="en_US"><meta property="og:locale:alternate" content="th_TH">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{url}card.jpg">
<link rel="alternate" type="text/plain" href="{url}llms.txt" title="llms.txt">
"""
body_start = page.index("<div data-root>")
out = head + page[:body_start] + "</head>\n<body>\n" + page[body_start:] + "\n</body>\n</html>\n"
(root / "docs" / "index.html").write_text(out)
print(root / "docs" / "index.html")
