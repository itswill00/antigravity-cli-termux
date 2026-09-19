#!/usr/bin/env python3
import sys, os, pathlib

def _ensure_web():
    if "web.server" in sys.modules:
        return
    cands = []
    try:
        cands.append(pathlib.Path(__file__).resolve().parent)
    except Exception:
        pass
    pfx = os.environ.get("PREFIX") or "/data/data/com.termux/files/usr"
    for base in (pathlib.Path(pfx) / "share/agy", pathlib.Path(pfx) / "lib/agy", pathlib.Path(pfx) / "bin/lib", pathlib.Path(__file__).resolve().parent.parent / "lib"):
        cands.append(base)
    for base in cands:
        try:
            if (base / "web" / "server.py").is_file():
                s = str(base)
                if s not in sys.path:
                    sys.path.insert(0, s)
                break
        except Exception:
            continue
    # last resort: parent of this shim if web sibling
    try:
        par = pathlib.Path(__file__).resolve().parent
        if (par / "web" / "server.py").is_file() and str(par) not in sys.path:
            sys.path.insert(0, str(par))
    except Exception:
        pass

_ensure_web()
from web.server import main

if __name__ == "__main__":
    main()
