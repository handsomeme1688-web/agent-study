"""Create a day's 3–4 algorithm exercises without replacing student work."""

import argparse
from pathlib import Path

from algorithm_support import parse_day, scaffold

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "repo-qa-agent"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", help="算法日 A01–A30；A01 接 Hello-Agents Day 3")
    args = parser.parse_args()
    try:
        number = parse_day(args.day)
        scaffold(ROOT, PROJECT, number)
    except (ValueError, KeyError, FileNotFoundError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
