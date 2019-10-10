#!/usr/bin/env python3

import sys
from typing import List
from pathlib import Path

VIDEO_SUFFIXES = [".mkv", ".mp4", ".avi"]
SUBTITLE_SUFFIXES = [".ass", ".ssa", ".srt"]


def main(filenames: List[str], dryrun: bool = True):
    videos: List[Path] = []
    subtitles: List[Path] = []
    for filename in filenames:
        file = Path(filename)
        suffix = file.suffix.lower()
        if suffix in VIDEO_SUFFIXES:
            videos.append(file)
        elif suffix in SUBTITLE_SUFFIXES:
            subtitles.append(file)
        else:
            raise Exception(f"Unknown suffix: {suffix} ( {filename} )")
    if len(videos) != len(subtitles):
        raise Exception("len(videos) != len(subtitles)")
    videos.sort()
    subtitles.sort()
    for index, subtitle in enumerate(subtitles):
        new_filename = subtitle.with_name(videos[index].stem + subtitle.suffix)
        if str(subtitle) != new_filename:
            print(f"{str(subtitle)} -> {new_filename}")
            if not dryrun:
                subtitle.rename(new_filename)


def cli():
    import argparse

    parser = argparse.ArgumentParser(
        description="Rename subtitles based on video file names"
    )
    parser.add_argument(
        "files", type=str, nargs=argparse.ONE_OR_MORE, help="video & subtitle files"
    )
    parser.add_argument("--dryrun", action="store_true", help="Don't rename files")
    parser.set_defaults(feature=True)

    args = parser.parse_args()
    main(args.files, args.dryrun)


if __name__ == "__main__":
    cli()
