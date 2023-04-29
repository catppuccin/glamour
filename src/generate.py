from dataclasses import fields
from pathlib import Path
from string import Template

from catppuccin import Flavour

OUT_DIR = Path("build")
OUT_DIR.mkdir(exist_ok=True)
TEMPLATE_STR = Path("src/template.json").read_text()


def palette():
    return {
        flavour_method.__name__: {
            field.name: f"#{getattr(flavour_method(), field.name).hex}"
            for field in fields(flavour_method())
        } for flavour_method in [Flavour.latte, Flavour.frappe, Flavour.macchiato, Flavour.mocha]
    }


if __name__ == "__main__":
    template = Template(TEMPLATE_STR)
    for flavour, colours in palette().items():
        substituted_template = template.substitute(colours)
        open(OUT_DIR / f"{flavour}.json", 'w').write(substituted_template)