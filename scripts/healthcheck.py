import json
import urllib.request


def main() -> int:
    data: dict[str, str | dict[str, str]]

    with open("webring.json") as file:
        data = json.load(file)

    print("webring version:", data["version"])
    print("webring instance:", data["name"])
    print("webring root:", data["root"])
    print("webring rings:", len(data["ring"]))

    status: dict[str, str] = {"version": data["version"], "anomalies": {}}

    for ring in data["ring"]:
        name, link = ring["name"], "https://{}".format(ring["link"])

        print("checking ring:", name, end="")

        req = urllib.request.Request(link, headers={"User-Agent": "Mozilla/5.0"})

        with urllib.request.urlopen(req) as res:
            try:
                if res.status == 200:
                    print("...ok")
                else:
                    status["anomalies"][ring["link"]] = {"dead": True}
                    print("...failed")
            except Exception as e:
                status["anomalies"][ring["link"]] = {"dead": True, "error": str(e)}
                print("...error")

    with open("webring.status.json", "w") as file:
        json.dump(status, file, indent=4)

    return 0


if __name__ == "__main__":
    exit(main())
