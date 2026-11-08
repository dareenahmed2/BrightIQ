from pathlib import Path

content = Path('generator.py').read_text(encoding='utf-8')
print(content.count('"prompt":'))
