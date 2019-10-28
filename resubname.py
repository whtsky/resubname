#!/usr/bin/env python3

import sys
from typing import List
from pathlib import Path

VIDEO_SUFFIXES = [".mkv", ".mp4", ".avi"]
SUBTITLE_SUFFIXES = [".ass", ".ssa", ".srt"]


def preprocess_paths(paths: List[str]) -> List[Path]:
    pwd = Path(".")
    rv = []
    for path in paths:
        if "*" in path:
            rv += list(pwd.glob(path))
        else:
            path = Path(path)
            if path.is_dir():
                rv += list(path.iterdir())
            else:
                rv.append(path)
    return rv


def should_exclude(file: Path, exclude_keywords: List[str]):
    name = file.name.lower()
    for keyword in exclude_keywords:
        if keyword in name:
            return True
    return False


def main(files: List[Path], exclude_keywords: List[str], dryrun: bool = True):
    exclude_keywords = [s.lower() for s in exclude_keywords]
    videos: List[Path] = []
    subtitles: List[Path] = []
    for file in files:
        if should_exclude(file, exclude_keywords):
            continue
        if file.is_dir():
            continue
        suffix = file.suffix.lower()
        if suffix in VIDEO_SUFFIXES:
            videos.append(file)
        elif suffix in SUBTITLE_SUFFIXES:
            subtitles.append(file)
        else:
            print(f"Unknown suffix: {suffix} ( {file.name} ), ignore")
    if len(videos) != len(subtitles):
        raise Exception(
            "Videos and subtitles number dismatch.\n\nVideos:\n{videos}\n\nSubtitles:\n{subtitles}".format(
                videos="\n".join([f"\t{f.name}" for f in videos]),
                subtitles="\n".join([f"\t{f.name}" for f in subtitles]),
            )
        )
    videos.sort()
    subtitles.sort()
    for index, subtitle in enumerate(subtitles):
        new_filename = subtitle.with_name(videos[index].stem + subtitle.suffix)
        if str(subtitle) != str(new_filename):
            print(f"{str(subtitle)} -> {new_filename}")
            if not dryrun:
                subtitle.rename(new_filename)
        else:
            print(f"{str(subtitle)} Unchanged.")


def cli(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description="Rename subtitles based on video file names"
    )

    parser.add_argument("--dryrun", action="store_true", help="Don't rename files")
    parser.add_argument(
        "-e",
        "--exclude",
        type=str,
        action="append",
        default=[],
        help="exclude files contain certain keywords",
    )

    parser.add_argument(
        "files", type=str, nargs=argparse.ONE_OR_MORE, help="video & subtitle files"
    )

    args = parser.parse_args(args)

    main(preprocess_paths(args.files), args.exclude, args.dryrun)


if __name__ == "__main__":
    cli()
