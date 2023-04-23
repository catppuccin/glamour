from dataclasses import fields
from pathlib import Path
from string import Template

from catppuccin import Flavour

OUT_DIR = Path("themes")
OUT_DIR.mkdir(exist_ok=True)
TEMPLATE_STR = Path("template.json").read_text()


def palette():
    all_flavours = {}
    for flavour_method in [Flavour.latte, Flavour.frappe, Flavour.macchiato, Flavour.mocha]:
        flavour_name = flavour_method.__name__
        flavour_colours = flavour_method()

        # convert `Colour(r, g, b)` -> #abcdef
        hexes = {field.name: "#" + getattr(flavour_colours, field.name).hex for field in fields(flavour_colours)}

        all_flavours[flavour_name] = hexes
    return all_flavours


if __name__ == "__main__":
    template = Template(TEMPLATE_STR)
    for flavour, colours in palette().items():
        substituted_template = template.substitute(colours)
        open(OUT_DIR / f"{flavour}.json", 'w').write(substituted_template)