import sys
from pathlib import Path
import matplotlib.image as image
from argparse import ArgumentParser

parser = ArgumentParser(description="Build thumbnails of all images in a directory")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")

outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)

for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
