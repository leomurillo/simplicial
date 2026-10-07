"""
kg.py — CLI for the UMC Knowledge Graph (kg_store.KnowledgeGraph).

Usage:
  py kg.py build                       # CONSTELLATE the repo's manuscripts -> kg_store.json
  py kg.py stats                       # node count, capacity shells, gap count
  py kg.py context "<query>" [-n 8]    # minimal capacity-matched context (the agent op)
  py kg.py neighbors <id> [-k 5]       # Fisher-Rao nearest
  py kg.py complement <id>             # exact Boolean Janus opposite
  py kg.py meet <a> <b> | join <a> <b> # concept-lattice navigation
  py kg.py gaps                        # vacant conductor addresses (what's missing)
  py kg.py get <id>                    # fetch a node
  py kg.py add <id> <file>             # RECEIVE a new document
"""
import sys, argparse, json
from kg_store import KnowledgeGraph, build_from_repo

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

def main():
    ap = argparse.ArgumentParser(description="UMC Knowledge Graph CLI")
    ap.add_argument("--store", default="kg_store.json")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    sub.add_parser("stats")
    c = sub.add_parser("context"); c.add_argument("query"); c.add_argument("-n", "--max", type=int, default=8)
    nb = sub.add_parser("neighbors"); nb.add_argument("id"); nb.add_argument("-k", type=int, default=5)
    cp = sub.add_parser("complement"); cp.add_argument("id")
    mt = sub.add_parser("meet"); mt.add_argument("a"); mt.add_argument("b")
    jn = sub.add_parser("join"); jn.add_argument("a"); jn.add_argument("b")
    sub.add_parser("gaps")
    g = sub.add_parser("get"); g.add_argument("id")
    ad = sub.add_parser("add"); ad.add_argument("id"); ad.add_argument("file")
    args = ap.parse_args()

    if args.cmd == "build":
        kg = build_from_repo(store=args.store)
        print(f"built {len(kg.nodes)} nodes -> {args.store}"); return

    kg = KnowledgeGraph(args.store)
    if not kg.nodes:
        print("empty store; run `py kg.py build` first"); return

    if args.cmd == "stats":
        print(f"nodes: {len(kg.nodes)}")
        print("capacity shells (rank w -> Q, log Q):")
        for r, v in kg.shells().items():
            print(f"  w={r}: Q={v['Q']:2d}  log Q={v['capacity_logQ']}")
        print(f"vacant conductor addresses (gaps): {len(kg.gaps())} / {2**6 - 1}")
    elif args.cmd == "context":
        r = kg.context(args.query, max_nodes=args.max)
        print(f"query: {r['query']}")
        print(f"concepts c_q = {r['concepts']}  depth k* = {r['depth']}  loaded {r['loaded_frac']*100:.0f}%")
        for h in r["hits"]:
            print(f"  {h['id']:>6}  FR={h['fr']}  cond={h['conductor']}  | {h['snippet']}")
    elif args.cmd == "neighbors":
        for nid, dd in kg.neighbors(args.id, k=args.k):
            print(f"  {nid:>6}  FR={dd}")
    elif args.cmd == "complement":
        print(json.dumps(kg.complement(args.id), ensure_ascii=False))
    elif args.cmd == "meet":
        print(f"meet({args.a},{args.b}) = {kg.meet(args.a, args.b)}")
    elif args.cmd == "join":
        print(f"join({args.a},{args.b}) = {kg.join(args.a, args.b)}")
    elif args.cmd == "gaps":
        print("vacant conductor addresses:"); print("  " + ", ".join(kg.gaps()))
    elif args.cmd == "get":
        nd = kg.get(args.id)
        print(json.dumps({k: nd[k] for k in ("id", "source", "conductor", "abcd", "coords")}, ensure_ascii=False)
              if nd else "not found")
    elif args.cmd == "add":
        text = open(args.file, encoding="utf-8", errors="ignore").read()
        nd = kg.add(args.id, text, source=args.file)
        print(f"added {nd['id']} (conductor {nd['conductor']}); run `build`/rebuild to re-constellate exactly")

if __name__ == "__main__":
    main()
