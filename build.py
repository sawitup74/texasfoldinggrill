"""texasfoldinggrill.com build. Run: python3 build.py
To switch on visit counting, replace texasfoldinggrill in GOATCOUNTER below with the real GoatCounter code, then rebuild."""
GOATCOUNTER = "https://texasfoldinggrill.goatcounter.com/count"
DOMAIN = "https://texasfoldinggrill.com"
UTM_SOURCE = "texasfoldinggrill"
SITE_NAME = "Texas Folding Grill"
LASTMOD = "2026-10-31"
THEME_COLOR = "#2b1d16"
HOME_IMG = "full01"
HOME_TITLE = "Texas Folding Grill: Texas-Style BBQ on a Small Folding Charcoal Grill"
HOME_DESC = "Texas BBQ cooking adapted to a small folding charcoal grill: brisket, sausage and ribs approaches, fire management, tailgates, deer camp and river trips."
BRAND_HTML = '<span class="star" aria-hidden="true">★</span><span class="wm">TEXAS <em>Folding</em> GRILL</span>'
FOOTER_BLURB = "<b>Texas Folding Grill</b> covers Texas-style cooking on a small, folding charcoal grill: post oak and mesquite, beef and sausage, tailgates, deer leases and river weekends. It's published by Slot Grill, which builds its grills in Buna, Texas."
NOTE = "Product specs and prices are from SlotGrill.com. Cook outdoors only, on stable, non-combustible ground, and check county burn bans before you light."
CATS = {
 "fire": ("texas-fire-management", "Fire &amp; Wood", "Post oak, mesquite, hickory and charcoal: building and holding a Texas-style fire in a small folding grill.", "Fire &amp; wood"),
 "bbq": ("texas-bbq-on-a-small-grill", "Texas BBQ on a Small Grill", "Brisket, sausage, ribs, beef and the Texas basics, adapted honestly to a lidless folding charcoal grill.", "BBQ"),
 "recipes": ("texas-recipes", "Texas Recipes", "Fajitas, links, chicken, breakfast tacos, venison and sides, written for a small charcoal grill.", "Recipes"),
 "trips": ("texas-trips", "Tailgates, Camp &amp; River", "Football tailgates, deer camp, lake and river weekends, Hill Country and coastal trips with a folding grill.", "Trips"),
 "gear": ("gear-and-the-grill", "The Grill &amp; Gear", "The Slot Grill sizes, griddle plates, care for carbon steel, what to pack, and where it's made.", "The grill"),
 "about": ("about-texas-folding-grill", "About &amp; Reference", "About the site, the FAQ and a glossary of Texas BBQ terms.", "About"),
}
NAV_CATS = ["fire", "bbq", "recipes", "trips", "gear"]
FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#2b1d16"/><path d="M32 8l6.5 15.5H55l-13.3 9.8 5 16.2L32 39.8 17.3 49.5l5-16.2L9 23.5h16.5z" fill="#b5462a"/><rect x="8" y="54" width="48" height="4" fill="#efe2c8"/></svg>'
CSS = """
:root{--brown:#2b1d16;--brown2:#3d2a1f;--rust:#b5462a;--rust2:#d0653f;--cream:#f6eedd;--paper:#fbf6ec;--ink:#24180f;--mute:#6b5a4b;--line:#e1d3b9;--gold:#c8962e}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:18px/1.7 Georgia,'Times New Roman',serif;color:var(--ink);background:var(--paper)}
h1,h2,h3,.wm,.btn,nav,.kicker,summary,th{font-family:Rockwell,'Roboto Slab','Courier New',Georgia,serif}
h1,h2,h3{line-height:1.15;font-weight:700}
a{color:var(--rust)}img{max-width:100%;height:auto;display:block}
.top{background:var(--brown);border-bottom:5px double var(--gold)}
.nav{max-width:1100px;margin:auto;display:flex;align-items:center;gap:1.2rem;padding:.8rem 1rem}
.brand{display:flex;align-items:center;gap:.5rem;text-decoration:none;color:var(--cream)}
.star{color:var(--rust2);font-size:1.6rem;line-height:1}.wm{font-weight:700;letter-spacing:.12em;font-size:1rem}.wm em{font-style:italic;letter-spacing:.02em;color:var(--gold);text-transform:none;font-size:1.1rem}
.nav nav{flex:1;display:flex;gap:1.1rem;justify-content:flex-end}.nav nav a{color:#e6d6bb;text-decoration:none;font-size:.9rem;text-transform:uppercase;letter-spacing:.08em}.nav nav a:hover{color:#fff}
.btn{display:inline-block;background:var(--rust);color:#fff!important;text-decoration:none;font-weight:700;padding:.75rem 1.2rem;border-radius:2px;letter-spacing:.06em;text-transform:uppercase;font-size:.9rem;box-shadow:3px 3px 0 var(--brown)}
.btn:hover{background:#9c3a22}.btn.small{padding:.45rem .8rem;font-size:.78rem;box-shadow:none;border:1px solid var(--gold)}.btn.ghost{background:var(--cream);color:var(--brown)!important}
main{max-width:760px;margin:auto;padding:1.2rem 1rem 2rem}main.wide{max-width:1100px}
.crumbs{font-size:.85rem;color:var(--mute);font-style:italic}.crumbs a{color:var(--mute)}
h1{font-size:clamp(2rem,4.6vw,2.9rem);margin:.4rem 0 .5rem;color:var(--brown)}h2{margin-top:2.4rem;font-size:1.55rem;color:var(--brown)}h2::before{content:"★ ";color:var(--rust);font-size:.8em}
.lede{font-size:1.15rem;color:var(--mute);font-style:italic}
.hero-img{border:6px solid #fff;box-shadow:0 2px 0 var(--line),0 8px 24px rgba(43,29,22,.15);margin:1rem 0 1.4rem;aspect-ratio:16/9;object-fit:cover;width:100%}
.facts{display:flex;flex-wrap:wrap;gap:.5rem 1.4rem;background:var(--cream);border:1px dashed var(--rust);padding:.7rem 1rem;margin:1rem 0}
.tbl{overflow-x:auto;margin:1rem 0}table{border-collapse:collapse;width:100%;background:#fff;font-size:.95rem}th,td{border:1px solid var(--line);padding:.55rem .65rem;text-align:left;vertical-align:top}th{background:var(--brown2);color:var(--cream);font-weight:700}tr:nth-child(even) td{background:#fcf8f0}
.note{background:var(--cream);border-left:6px solid var(--gold);padding:.8rem 1rem}
details{background:#fff;border:1px solid var(--line);margin:.5rem 0;padding:.6rem .9rem}summary{cursor:pointer;font-weight:700;color:var(--brown)}
.product{display:grid;grid-template-columns:200px 1fr;gap:1.2rem;align-items:center;background:#fff;border:2px solid var(--brown);padding:1.1rem;margin:2.2rem 0;box-shadow:6px 6px 0 var(--line)}
.product img{aspect-ratio:1;object-fit:cover}.product h3{margin:.1rem 0 .3rem;font-size:1.35rem}.kicker{text-transform:uppercase;letter-spacing:.16em;font-size:.72rem;color:var(--rust);font-weight:700;margin:0}
.price{font-weight:700;font-size:1.3rem}.price s{color:var(--mute);font-weight:400;font-size:.95rem;margin-left:.5rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(245px,1fr));gap:1.1rem}
.card{background:#fff;border:1px solid var(--line);border-bottom:4px solid var(--rust);text-decoration:none;color:var(--ink);overflow:hidden}.card:hover{border-color:var(--brown)}
.card img{aspect-ratio:4/3;object-fit:cover;width:100%;filter:sepia(.15)}.card div{padding:.8rem 1rem}.card h3{margin:0 0 .3rem;font-size:1.1rem;color:var(--brown)}.card p{margin:0;font-size:.92rem;color:var(--mute)}
.hero{background:var(--brown) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40'%3E%3Cpath d='M0 40L40 0' stroke='%233d2a1f' stroke-width='2'/%3E%3C/svg%3E");color:var(--cream);display:grid;grid-template-columns:1.1fr 1fr;gap:2rem;align-items:center;padding:2.4rem;margin:.6rem 0 1.2rem;border:5px double var(--gold)}
.hero h1{color:#fff;font-size:clamp(2.1rem,5vw,3.3rem)}.hero p{color:#e6d6bb}.hero img{border:5px solid var(--cream)}.hero .kicker{color:var(--gold)}.hero h2::before{content:none}
.hsec h2 a{color:inherit;text-decoration:none}.related ul{columns:2;gap:2rem}
footer{background:var(--brown);color:#cbb89a;padding:2.4rem 1rem;margin-top:3rem;font-size:.92rem;border-top:5px double var(--gold)}footer .in{max-width:1100px;margin:auto}footer a{color:var(--cream)}.fbrand{margin-bottom:.6rem;color:var(--cream)}
.small-note{font-size:.85rem;color:var(--mute);font-style:italic}
@media(max-width:780px){.nav nav{display:none}.nav{justify-content:space-between}.hero{grid-template-columns:1fr;padding:1.4rem}.product{grid-template-columns:1fr}.related ul{columns:1}body{font-size:17px}}
"""
# ---------------- engine (shared by all guide sites; config is at the top of this file) ----------------
import json, html, os, sys, re, glob
SG = "https://slotgrill.com"
UTM = "utm_source=%s&amp;utm_medium=referral&amp;utm_campaign=guide-site" % UTM_SOURCE
def sg(path=""):
    return SG + path + ("&amp;" if "?" in path else "?") + UTM
COMPACT = sg("/products/slot-grill-compact-carbon-steel-free-shipping")
FULL = sg("/products/slot-grill-carbon-steel-collapsible-bbq-grill")
GRID = sg("/products/slot-grill-griddle-plancha")
BALM = sg("/products/seasoning-balm-for-slot-grill")
THERMO = sg("/products/slot-grill-instant-read-digital-meat-thermometer")
BUNDLE = sg("/products/seasoning-balm-meat-thermometer-bundle")
SHOP = sg("/collections/all")
SPECS = sg("/pages/slot-grill-specs-setup-care")
ABOUTSG = sg("/pages/about-slot-grill")
MADE = sg("/pages/made-in-usa")
SGFAQ = sg("/pages/faq-frequently-asked-questions")
CONTACT = sg("/pages/contact")
HOME = sg("/")
CDN = "https://cdn.shopify.com/s/files/1/0721/8833/0172/files/"
IMG = {k: CDN + v for k, v in dict(
    c07="compact-07.jpg?v=1792382833", c28="compact-28.jpg?v=1792382861", c08="compact-08.jpg?v=1792382834",
    c13="compact-13.jpg?v=1792382834", both16="both-16.jpg?v=1792382825", both02="both-02.jpg?v=1792382824",
    full01="full-size-01.jpg?v=1792382862", full08="full-size-08.jpg?v=1792382863", full10="full-size-10.jpg?v=1792382864",
    full13="full-size-13.jpg?v=1792382866", grid1="griddle-add-on.jpg?v=1793024225", grid2="griddle-add-on-two.jpg?v=1793024983",
    balm="seasoning-balm-main.jpg?v=1791978819", thermo="thermometer-red-clean.jpg?v=1791939312",
    bundle="balm-thermometer-bundle-v3.jpg?v=1791943793").items()}
# Product facts below are copied from slotgrill.com product and specs pages (checked 2026-10-31).
PRODUCTS = {
 "compact": dict(name="Slot Grill Compact", url=COMPACT, img="c07", alt="Slot Grill Compact carbon steel charcoal grill",
    facts='12-gauge carbon steel · about 14 lb · 16.25" × 9" cooking area · packs about 1" thick · made in the USA (Texas)',
    price="$89.97", was="$99.97", btn="See the Compact at SlotGrill.com"),
 "full": dict(name="Slot Grill Full Size", url=FULL, img="full01", alt="Slot Grill Full Size carbon steel charcoal grill",
    facts='10-gauge carbon steel · about 27.6 lb · 20.5" × 11.25" cooking area · packs about 1.25" thick · made in the USA (Texas)',
    price="$149.97", was="$159.97", btn="See the Full Size at SlotGrill.com"),
 "griddle": dict(name="Slot Grill Griddle Add-On", url=GRID, img="grid1", alt="Slot Grill griddle plancha add-on plates",
    facts="Carbon steel flat-top plates made for the Slot Grill two-piece top. One or two plates, for the Compact or the Full Size. Stacks flat with the grill. Grill not included.",
    price="from $20.00", was="", btn="See the griddle at SlotGrill.com"),
}
PAGES = []
def page(slug, title, desc, img, body, cat, faq=None):
    global PAGES
    PAGES = [p for p in PAGES if p[0] != slug]
    PAGES.append((slug, title, desc, img, body, cat, faq or []))
def esc(s): return html.escape(s, quote=True)
def L(slug, text): return '<a href="/%s.html">%s</a>' % (slug, text)
def X(url, text): return '<a href="%s">%s</a>' % (url, text)
def ul(items): return "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"
def ol(items): return "<ol>" + "".join("<li>%s</li>" % i for i in items) + "</ol>"
def table(head, rows):
    return '<div class="tbl"><table><tr>' + "".join("<th>%s</th>" % h for h in head) + "</tr>" + "".join(
        "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows) + "</table></div>"
def tip(t): return '<p class="note">%s</p>' % t
TEMPS_ROWS = [("Beef, pork, lamb and veal steaks, chops and roasts", "145°F, then rest 3 minutes"),
    ("Ground beef, pork, lamb and veal (burgers, fresh sausage)", "160°F"),
    ("Chicken and turkey, whole, pieces or ground", "165°F"),
    ("Fish and shellfish", "145°F, or flesh opaque and flakes with a fork"),
    ("Egg dishes", "160°F; cook eggs until yolks and whites are firm"),
    ("Precooked sausage, hot dogs and leftovers", "Reheat to 165°F")]
def temps():
    return ("<h2>Safe internal temperatures</h2><p>Check the thickest part with an instant-read thermometer, away from bone. These are USDA minimum safe temperatures; tougher cuts like brisket and ribs are cooked well past them for tenderness.</p>"
            + table(["Food", "Minimum internal temperature"], TEMPS_ROWS))
def recipe(intro, serves, time, ingr, steps, tips=None, extra="", size="compact"):
    p = PRODUCTS[size]
    h = intro + '<div class="facts"><span><b>Serves</b> %s</span><span><b>Time</b> %s</span><span><b>Grill</b> <a href="%s">%s</a></span></div>' % (serves, time, p["url"], p["name"])
    h += "<h2>Ingredients</h2>" + ul(ingr) + "<h2>Method</h2>" + ol(steps) + extra
    if tips: h += "<h2>Tips</h2>" + ul(tips)
    return h + temps()
def faqld(faq):
    if not faq: return ""
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": html.unescape(re.sub("<[^>]+>", "", q)), "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub("<[^>]+>", "", a))}} for q, a in faq]}) + "</script>"
def faqhtml(faq, h="Questions people ask"):
    return ("<h2>%s</h2>" % h + "".join('<details><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in faq)) if faq else ""
def productbox(kind="compact"):
    p = PRODUCTS[kind]
    was = "<s>%s</s>" % p["was"] if p["was"] else ""
    return ('<aside class="product"><img src="%s" alt="%s" loading="lazy"><div><p class="kicker">From the maker in Buna, Texas</p><h3>%s</h3><p>%s</p><p class="price">%s%s</p><a class="btn" href="%s">%s</a></div></aside>'
            % (IMG[p["img"]], esc(p["alt"]), p["name"], p["facts"], p["price"], was, p["url"], p["btn"]))
def crumbs(items):
    return '<p class="crumbs">' + " › ".join(('<a href="%s">%s</a>' % (u, t)) if u else t for t, u in items) + "</p>"
def shell(title, desc, slug, inner, img=None, faq=None, kind="Article", trail=None, wide=False):
    canon = DOMAIN + ("/" if slug == "index" else "/%s.html" % slug)
    img = img or IMG["c07"]
    ld = [{"@context": "https://schema.org", "@type": "WebSite" if slug == "index" else kind, "name": html.unescape(title),
           "url": canon, "description": html.unescape(desc), "image": img,
           "publisher": {"@type": "Organization", "name": SITE_NAME, "url": DOMAIN + "/"},
           "about": {"@type": "Product", "name": "Slot Grill", "brand": {"@type": "Brand", "name": "Slot Grill"}, "url": SG + "/"}}]
    if kind == "Article" and slug != "index": ld[0]["headline"] = html.unescape(title)
    if trail:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub("<[^>]+>", "", t)), "item": DOMAIN + (u if u else "/%s.html" % slug)} for i, (t, u) in enumerate(trail)]})
    lds = "".join('<script type="application/ld+json">%s</script>' % json.dumps(x) for x in ld)
    nav = "".join('<a href="/%s.html">%s</a>' % (CATS[k][0], CATS[k][3]) for k in NAV_CATS) + '<a href="/faq.html">FAQ</a>'
    foot = " · ".join('<a href="/%s.html">%s</a>' % (c[0], c[1]) for c in CATS.values()) + ' · <a href="/faq.html">FAQ</a> · <a href="/glossary.html">Glossary</a> · <a href="/about.html">About</a> · <a href="/compact-vs-full-size-slot-grill.html">Compact vs Full Size</a>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(html.unescape(title))}</title><meta name="description" content="{esc(html.unescape(desc))}"><link rel="canonical" href="{canon}">
<meta property="og:type" content="{'website' if slug=='index' else 'article'}"><meta property="og:site_name" content="{SITE_NAME}"><meta property="og:title" content="{esc(html.unescape(title))}"><meta property="og:description" content="{esc(html.unescape(desc))}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{img}">
<meta name="theme-color" content="{THEME_COLOR}"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css">{lds}{faqld(faq)}</head><body>
<header class="top"><div class="nav"><a class="brand" href="/" aria-label="{SITE_NAME} home">{BRAND_HTML}</a><nav>{nav}</nav><a class="btn small" href="{HOME}">SlotGrill.com</a></div></header>
<main class="{'wide' if wide else ''}">{inner}</main>
<footer><div class="in"><div class="fbrand">{BRAND_HTML}</div><p>{FOOTER_BLURB}</p><p>Slot Grill is a collapsible carbon steel charcoal grill made in the USA by Keith in Buna, Texas. Slot Grill® is a registered trademark. Genuine Slot Grills are sold at <a href="{HOME}">SlotGrill.com</a>, the @SlotGrill TikTok Shop and @SlotGrill on the Shop app. Questions about an order or the grill? Use the <a href="{CONTACT}">Slot Grill contact form</a>.</p><p class="flinks"><a href="/">Home</a> · {foot}</p></div></footer>
<script data-goatcounter="{GOATCOUNTER}" async src="//gc.zgo.at/count.js"></script><script>document.addEventListener("click",function(e){{var a=e.target.closest&&e.target.closest('a[href*="//slotgrill.com"]');if(a&&window.goatcounter&&window.goatcounter.count){{window.goatcounter.count({{path:"click-to-slotgrill/"+location.pathname,title:"Click to slotgrill.com",event:true}})}}}});</script></body></html>
'''
def related(slug, cat):
    rel = [p for p in PAGES if p[5] == cat and p[0] != slug][:8]
    if not rel: return ""
    c = CATS[cat]
    return '<nav class="related"><h2>More in %s</h2><ul>' % c[1] + "".join('<li><a href="/%s.html">%s</a></li>' % (p[0], p[1]) for p in rel) + '</ul><p><a href="/%s.html">All %s →</a></p></nav>' % (c[0], c[1])
def article(slug, title, desc, img, body, cat, faq):
    c = CATS[cat]
    wc = lambda b: len(re.sub("<[^>]+>", " ", b).split())
    for blk in globals().get("EXTRA", {}).get(cat, []):
        if wc(body) >= 520: break
        if blk[:60] not in body: body += blk
    trail = [("Home", "/"), (c[1], "/%s.html" % c[0]), (title, None)]
    kind = "big" if "full" in img else "compact"
    box = productbox("full" if kind == "big" else "compact")
    if "griddle" in body.lower() and cat != "about": box += productbox("griddle")
    inner = (crumbs(trail) + '<article><h1>%s</h1><p class="lede">%s</p><img class="hero-img" src="%s" alt="%s">' % (title, desc, IMG[img], esc(html.unescape(title)) + " – Slot Grill")
             + body + (faqhtml(faq) if slug != "faq" else "") + "</article>" + box + related(slug, cat) + '<p class="small-note">%s</p>' % NOTE)
    return shell(title, desc, slug, inner, img=IMG[img], faq=faq, trail=trail)
def cardgrid(ps):
    return '<div class="grid">' + "".join('<a class="card" href="/%s.html"><img src="%s" alt="" loading="lazy"><div><h3>%s</h3><p>%s</p></div></a>' % (s, IMG[i], t, d) for s, t, d, i, *_ in ps) + "</div>"
def build():
    open("style.css", "w").write(CSS)
    open("favicon.svg", "w").write(FAVICON)
    open("CNAME", "w").write(DOMAIN.split("//")[1] + "\n")
    for f in sorted(glob.glob("content_*.py")): exec(open(f).read(), globals())
    # FAQ page aggregates every page's questions
    allq = [(q, a, p) for p in PAGES for q, a in p[6] if p[0] != "faq"]
    base = [p for p in PAGES if p[0] == "faq"]
    if base:
        b = base[0]
        body = b[4] + "".join('<h2>%s</h2>' % CATS[k][1] + "".join('<details><summary>%s</summary><p>%s <a href="/%s.html">Read: %s</a></p></details>' % (q, a, p[0], p[1]) for q, a, p in allq if p[5] == k) for k in CATS)
        page("faq", b[1], b[2], b[3], body, b[5], b[6])
    for f in glob.glob("*.html"): os.remove(f)
    for p in PAGES: open(p[0] + ".html", "w").write(article(*p))
    for k, c in CATS.items():
        ps = [p for p in PAGES if p[5] == k]
        trail = [("Home", "/"), (c[1], None)]
        open(c[0] + ".html", "w").write(shell(c[1] + " | " + SITE_NAME, c[2], c[0], crumbs(trail) + "<h1>%s</h1><p class=\"lede\">%s</p>" % (c[1], c[2]) + cardgrid(ps) + productbox(), kind="CollectionPage", trail=trail, wide=True))
    open("index.html", "w").write(shell(HOME_TITLE, HOME_DESC, "index", home_html(), img=IMG[HOME_IMG], wide=True))
    open("404.html", "w").write(shell("Page not found | " + SITE_NAME, "That page isn't here. Browse the guides instead.", "404",
        "<h1>That page isn't here</h1><p>The link may be old or mistyped. Try one of these:</p>" + ul(['<a href="/">Home</a>'] + ['<a href="/%s.html">%s</a>' % (c[0], c[1]) for c in CATS.values()] + ['<a href="/faq.html">FAQ</a>']), kind="WebPage"))
    urls = [DOMAIN + "/"] + ["%s/%s.html" % (DOMAIN, c[0]) for c in CATS.values()] + ["%s/%s.html" % (DOMAIN, p[0]) for p in PAGES]
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join("  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, LASTMOD) for u in urls) + "</urlset>\n")
    open("robots.txt", "w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    print(len(PAGES), "articles +", len(CATS), "hubs + home")
def home_html():
    secs = "".join('<section class="hsec"><h2><a href="/%s.html">%s</a></h2><p>%s</p>%s</section>' % (c[0], c[1], c[2], cardgrid([p for p in PAGES if p[5] == k][:6])) for k, c in CATS.items())
    return HOME_HERO + secs + '<section class="hsec"><h2>The two Slot Grills, side by side</h2><p>Both are tab-and-slot, carbon steel, made in Texas. ' + L("compact-vs-full-size-slot-grill", "Full comparison →") + "</p>" + productbox("compact") + productbox("full") + "</section>"
if __name__ == "__main__":
    build()
