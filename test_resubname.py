import shutil
from pathlib import Path
from uuid import uuid4

import pytest

from resubname import cli

FIXTURES_PATH = Path(__file__).parent / "fixtures"


def sorted_glob(p: Path, pattern="*"):
    """
    return sorted filenames for matched files.
    """
    names = [x.name for x in p.glob(pattern)]
    names.sort()
    return names


def copy_fixtures(src: Path, tmp_path: Path) -> Path:
    fixture_path = tmp_path / uuid4().hex
    shutil.copytree(src, fixture_path)
    return fixture_path


def test_rename(tmp_path: Path):
    fixtures = copy_fixtures(FIXTURES_PATH / "basic", tmp_path)
    files_before = sorted_glob(fixtures)
    cli([str(fixtures)])
    files_after = sorted_glob(fixtures)
    assert files_after != files_before
    videos = sorted(fixtures.glob("*.mkv"))
    expected_files = sorted(
        [video.name for video in videos]
        + [video.with_suffix(".ass").name for video in videos]
    )
    assert files_after == expected_files


def test_dryrun(capsys, tmp_path: Path):
    fixtures = copy_fixtures(FIXTURES_PATH / "basic", tmp_path)
    files_before = sorted_glob(fixtures)
    cli([str(fixtures), "--dryrun"])
    files_after = sorted_glob(fixtures)
    assert files_after == files_before

    out, _err = capsys.readouterr()
    assert (
        out.replace(str(fixtures.resolve()), "")
        == """\
/03.ass -> /[VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].ass
/05.5.ass -> /[VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].ass
/05.ass -> /[VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].ass
"""
    )


def test_raise_when_subtitle_and_videos_number_dismatch():
    path = FIXTURES_PATH / "exclude"
    with pytest.raises(ValueError):
        cli([str(path)])


def test_exclude(capsys, tmp_path: Path):
    fixtures = copy_fixtures(FIXTURES_PATH / "exclude", tmp_path)
    files_before = sorted_glob(fixtures)
    cli([str(fixtures), "-e", "creditless"])
    files_after = sorted_glob(fixtures)
    assert files_after != files_before
    all_videos = sorted(fixtures.glob("*.mkv"))
    videos = [video for video in all_videos if "creditless" not in video.name.lower()]
    expected_files = sorted(
        [video.name for video in all_videos]
        + [video.with_suffix(".ass").name for video in videos]
    )
    assert files_after == expected_files

    out, _err = capsys.readouterr()
    assert len(out.splitlines()) == len(videos)
