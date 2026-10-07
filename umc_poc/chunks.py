"""
chunks.py — section-granularity nodes for token-minimal retrieval.

The KG was indexed over whole manuscripts (~10-30k tokens each), so "load k* whole docs"
is not token-minimal. Here a NODE = a section (split on markdown headers), so capacity-matched
retrieval genuinely yields a few hundred tokens, not whole papers. The cores
(fisher_kg, conductor_kg, embed) are unchanged — only the unit of indexing changes.

Returns a list of units (chunk_id, text, doc_id). chunk_id = "<doc>#<k>"; doc_id lets the
benchmark map a retrieved chunk back to its source paper for gold scoring.
"""
import re
from poc import load_corpus

HEADER = re.compile(r"^#{1,4}[ \t]+(.+)$", re.M)

def split_sections(text):
    marks = [(m.start(), m.group(1).strip()) for m in HEADER.finditer(text)]
    if not marks:
        return [("(body)", text)]
    secs = []
    if marks[0][0] > 0:
        secs.append(("(intro)", text[:marks[0][0]]))
    for k, (pos, hdr) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(text)
        secs.append((hdr, text[pos:end]))
    return secs

# boilerplate sections that are retrieval noise (lists of other papers' titles, etc.)
SKIP_HDR = ("references", "bibliography", "acknowledg", "changelog",
            "data availab", "data and code", "keywords", "msc 2020")

def load_chunks(min_tok=80, max_tok=1000):
    ids, stems, fams, texts = load_corpus()
    units = []
    for di, doc in enumerate(ids):
        # drop boilerplate, then merge tiny sections forward, then hard-split oversize ones
        secs = [(h, b) for (h, b) in split_sections(texts[di])
                if not h.lower().strip().startswith(SKIP_HDR)]
        merged = []
        for hdr, body in secs:
            if merged and len(merged[-1][1].split()) < min_tok:
                merged[-1] = (merged[-1][0], merged[-1][1] + "\n" + body)
            else:
                merged.append((hdr, body))
        final = []
        for hdr, body in merged:
            w = body.split()
            if len(w) <= max_tok:
                final.append((hdr, body))
            else:
                for s in range(0, len(w), max_tok):
                    final.append((hdr if s == 0 else hdr + " (cont)", " ".join(w[s:s + max_tok])))
        for k, (hdr, body) in enumerate(final):
            units.append((f"{doc}#{k}", f"[{doc}] {hdr}\n{body}", doc))
    return units
