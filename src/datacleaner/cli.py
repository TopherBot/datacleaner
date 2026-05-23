import sys
import pathlib
import click
import pandas as pd

def _clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the cleaning pipeline.

    * Strip whitespace from string columns
    * Drop rows that are completely empty
    * Normalize column names to snake_case
    """
    # Trim whitespace
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop all‑NA rows
    df = df.dropna(how="all")

    # Normalize column names
    df.columns = [
        "_".join(
            filter(None, [part.lower() for part in col.replace(" ", "_").split("_")])
        for col in df.columns
    ]
    return df

@click.command()
@click.option("--input", "input_path", required=True, type=click.Path(exists=True, dir_okay=False), help="Path to the raw CSV/TSV file.")
@click.option("--output", "output_path", required=True, type=click.Path(writable=True, dir_okay=False), help="Path where the cleaned file will be written.")
@click.option("--delimiter", "delimiter", default=None, help="Force delimiter (',' or '\t'). Auto‑detect if omitted.")
def main(input_path: str, output_path: str, delimiter: str | None):
    """Clean a CSV/TSV file.

    Example:
        python -m datacleaner --input data.tsv --output clean.csv
    """
    in_path = pathlib.Path(input_path)
    out_path = pathlib.Path(output_path)

    # Auto‑detect delimiter if not forced
    if delimiter is None:
        sample = in_path.read_text(encoding="utf-8", errors="ignore").splitlines()[0]
        delimiter = "\t" if "\t" in sample else ","

    try:
        df = pd.read_csv(in_path, delimiter=delimiter, dtype=str, keep_default_na=False)
    except Exception as e:
        click.echo(f"❌ Failed to read input file: {e}", err=True)
        sys.exit(1)

    cleaned = _clean_dataframe(df)

    try:
        cleaned.to_csv(out_path, index=False, sep=delimiter)
        click.echo(f"✅ Cleaned data written to {out_path}")
    except Exception as e:
        click.echo(f"❌ Failed to write output file: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
