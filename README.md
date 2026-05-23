# 📊 datacleaner

**datacleaner** is a tiny, opinionated command‑line utility that reads a CSV/TSV file, applies common cleaning steps (trim whitespace, drop empty rows, infer types, normalize column names) and writes a cleaned file.

---

## Features

- ✅ Drop rows with all empty values
- ✅ Strip leading/trailing whitespace from all cells
- ✅ Convert column names to `snake_case`
- ✅ Auto‑detect delimiter (comma or tab)
- ✅ One‑liner usage via `python -m datacleaner`

## Quick start

```bash
# Clone the repo
git clone https://github.com/youruser/datacleaner.git
cd datacleaner

# Install (editable mode) and run the CLI
pip install -e .
python -m datacleaner --input raw_data.csv --output clean_data.csv
```

## Development

```bash
# Install dependencies for development
pip install -e .[dev]

# Run linters & tests
ruff check .
pytest
```

## CI/CD

GitHub Actions automatically run linting, tests and build a source distribution on every push/PR. See ".github/workflows/ci.yml".

---

## License

MIT – see `LICENSE`.
