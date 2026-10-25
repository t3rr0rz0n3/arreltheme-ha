"""Expand room templates into a single card for the Home Assistant UI editor.

Requires PyYAML. Run after editing cards/arrel-rooms.yaml.
"""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

class CardDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def represent_string(dumper, value):
    return dumper.represent_scalar('tag:yaml.org,2002:str', value,
                                 style='|' if '\n' in value else None)

CardDumper.add_representer(str, represent_string)

def build():
    templates = yaml.safe_load((ROOT / 'cards/arrel-room-templates.yaml').read_text())
    panel = yaml.safe_load((ROOT / 'cards/arrel-rooms.yaml').read_text())

    def replace(value, variables):
        if isinstance(value, str):
            for key, replacement in variables.items():
                value = value.replace('[[' + key + ']]', str(replacement))
            return value
        if isinstance(value, list):
            return [replace(item, variables) for item in value]
        if isinstance(value, dict):
            return {key: replace(item, variables) for key, item in value.items()}
        return value

    def expand(value):
        if isinstance(value, list):
            return [expand(item) for item in value]
        if not isinstance(value, dict):
            return value
        if value.get('type') == 'custom:decluttering-card':
            template = templates[value['template']]
            variables = {}
            for item in template.get('default', []) + value.get('variables', []):
                variables.update(item)
            return expand(replace(template['card'], variables))
        return {key: expand(item) for key, item in value.items()}

    output = yaml.dump(expand(panel), Dumper=CardDumper, sort_keys=False, allow_unicode=True)
    assert '[[' not in output and 'custom:decluttering-card' not in output
    destination = ROOT / 'cards/arrel-rooms-paste.yaml'
    destination.write_text('# COPIA TODO ESTE ARCHIVO EN UNA TARJETA MANUAL.\n'
                           '# Requiere Bubble Card >= 3.2.0 y card-mod.\n'
                           '# Generado por scripts/build_rooms_card.py; no usa !include.\n' + output)
    print(destination)

if __name__ == '__main__':
    build()
