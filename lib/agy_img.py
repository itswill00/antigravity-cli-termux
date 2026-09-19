#!/usr/bin/env python3
# ponytail: stdlib only. agy-img: chat + image via @ (agy vision native).
import sys, pathlib, mimetypes, subprocess, shutil, os, argparse

AGY = shutil.which("agy") or "agy"

def guess_mime(p: pathlib.Path):
    m,_ = mimetypes.guess_type(str(p))
    return m or "application/octet-stream"

def main():
    ap = argparse.ArgumentParser(description="agy-img — kirim foto ke agy (wrapper agy -p + @image)")
    ap.add_argument("image", help="path to image (jpg/png/webp)")
    ap.add_argument("prompt", nargs="*", default=[], help="prompt text")
    ap.add_argument("--model", default="", help="model id (see agy models)")
    ap.add_argument("--effort", choices=["low","medium","high"], default="", help="effort")
    ap.add_argument("--open-image", action="store_true", help="open image with termux-open after send (debug)")
    args = ap.parse_args()

    img = pathlib.Path(args.image).expanduser()
    if not img.exists():
        print(f"[agy-img] not found: {img}", file=sys.stderr); sys.exit(1)
    if img.stat().st_size > 10*1024*1024:
        print(f"[agy-img] too large >10MB: {img.stat().st_size}", file=sys.stderr); sys.exit(1)
    mime = guess_mime(img)
    if not mime.startswith("image/"):
        print(f"[agy-img] not an image ({mime}): {img}", file=sys.stderr); sys.exit(1)

    prompt = " ".join(args.prompt).strip() or "describe this image in detail, be concise"
    # agy vision via @path: agy --model X --effort Y -p "@img prompt"
    agy_prompt = f"@{img.resolve()} {prompt}"

    cmd = [AGY]
    if args.model:
        cmd += ["--model", args.model]
    if args.effort:
        cmd += ["--effort", args.effort]
    cmd += ["-p", agy_prompt]

    # run and stream
    proc = subprocess.run(cmd)
    sys.exit(proc.returncode)

if __name__ == "__main__":
    main()
