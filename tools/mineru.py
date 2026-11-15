"""Parse every file in a folder with the MinerU cloud API: upload in one batch, wait, and unpack each result zip."""
import json, os, sys, time, urllib.request, zipfile, io, pathlib

TOKEN = os.environ["MINERU_TOKEN"]
API = "https://mineru.net/api/v4"

def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.load(r)
    if out.get("code") != 0:
        raise SystemExit(f"{path}: {out}")
    return out["data"]

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
files = sorted(p for p in src.iterdir() if p.is_file())
data = call("POST", "/file-urls/batch", {"files": [{"name": p.name, "data_id": str(i)} for i, p in enumerate(files)],
                                         "model_version": "vlm", "language": "ch", "enable_formula": True, "enable_table": True})
for p, url in zip(files, data["file_urls"]):
    # The signed upload URL must get the bytes with no Content-Type of ours.
    import http.client, urllib.parse
    u = urllib.parse.urlsplit(url)
    conn = http.client.HTTPSConnection(u.netloc, timeout=300)
    conn.putrequest("PUT", u.path + ("?" + u.query if u.query else ""), skip_accept_encoding=True)
    body = p.read_bytes()
    conn.putheader("Content-Length", str(len(body)))
    conn.endheaders()
    conn.send(body)
    resp = conn.getresponse()
    if resp.status != 200:
        raise SystemExit(f"upload {p.name}: HTTP {resp.status} {resp.read()[:200]}")
    print("uploaded", p.name, flush=True)
batch = data["batch_id"]
while True:
    time.sleep(10)
    res = call("GET", f"/extract-results/batch/{batch}")["extract_result"]
    states = {r["file_name"]: r["state"] for r in res}
    print(states, flush=True)
    if all(s in ("done", "failed") for s in states.values()) and len(states) == len(files):
        break
for r in res:
    if r["state"] != "done":
        print("FAILED", r["file_name"], r.get("err_msg")); continue
    z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(r["full_zip_url"], timeout=300).read()))
    out = dst / pathlib.Path(r["file_name"]).stem
    z.extractall(out)
    print("saved", out)
