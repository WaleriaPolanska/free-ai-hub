"""Check every link in data.json and record the result.

For each item with a url it sets:
  checked - date of this check (YYYY-MM-DD)
  alive   - False only when the page is really gone (404/410, DNS or connection error).
            Bot protection (403/429) and other answers count as alive.
Also sets the top-level "updated" date. Uses only the standard library.
"""
import json, os, ssl, sys, datetime, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

PATH = sys.argv[1] if len(sys.argv) > 1 else "data.json"
UA = "Mozilla/5.0 (compatible; free-ai-hub-linkcheck/1.0)"
DEAD = {404, 410}


def alive(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20):
                return True
        except urllib.error.HTTPError as e:
            if e.code in DEAD:
                return False
            if method == "HEAD" and e.code in (405, 501):
                continue  # server does not support HEAD, retry with GET
            return True
        except urllib.error.URLError as e:
            if isinstance(e.reason, ssl.SSLError):
                return True  # TLS mismatch on our side, not proof the page is gone
            if method == "GET":
                return False
        except Exception:
            if method == "GET":
                return False
    return False


def refresh_github(items):
    """Update stars / last push / archived for GitHub repos (needs GITHUB_TOKEN)."""
    token = os.environ.get("GITHUB_TOKEN")
    repos = [o for o in items if o.get("repo")]
    if not token or not repos:
        return 0
    n = 0
    for i in range(0, len(repos), 40):
        chunk = repos[i:i + 40]
        parts = []
        for j, o in enumerate(chunk):
            owner, name = o["repo"].split("/")
            parts.append(f'r{j}: repository(owner:"{owner}", name:"{name}") {{ stargazerCount pushedAt isArchived }}')
        body = json.dumps({"query": "query {" + " ".join(parts) + "}"}).encode()
        req = urllib.request.Request("https://api.github.com/graphql", data=body,
                                     headers={"Authorization": f"bearer {token}", "User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.load(r).get("data") or {}
        for j, o in enumerate(chunk):
            m = res.get(f"r{j}")
            if m:
                o["stars"], o["pushed"] = m["stargazerCount"], m["pushedAt"][:10]
                o["archived"] = m["isArchived"]
                n += 1
    return n


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    today = datetime.date.today().isoformat()
    print("github repos refreshed:", refresh_github(data["patches"] + data["skills"]))
    items = [o for k in ("offers", "ai", "patches", "skills") for o in data[k] if o.get("url")]
    with ThreadPoolExecutor(16) as ex:
        results = list(ex.map(lambda o: alive(o["url"]), items))
    for o, ok in zip(items, results):
        o["alive"], o["checked"] = ok, today
    data["updated"] = today
    json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    dead = [o["n"] for o, ok in zip(items, results) if not ok]
    print(f"checked {len(items)} links, dead: {len(dead)}")
    for n in dead:
        print("  DEAD", n)


if __name__ == "__main__":
    main()
