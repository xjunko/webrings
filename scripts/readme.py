import json


def main() -> int:
    data: dict[str, str | dict[str, str]]

    with open("webring.json") as file:
        data = json.load(file)

    with open("README.md.tmpl") as file:
        template = file.read()

    members: str = ""

    for ring in data["ring"]:
        name, link = ring["name"], "https://{}".format(ring["link"])

        members += f"- [{name}]({link}) \n"

    with open("README.md", "w") as file:
        file.write(template.format(members=members))


if __name__ == "__main__":
    exit(main())
