from pathlib import Path
import pytest
import shutil
from uuid import uuid4


from resubname import cli

FIXTURES_PATH = Path(__file__).parent / "fixtures"


def copy_fixtures(src: Path, tmp_path: Path) -> Path:
    fixture_path = tmp_path / uuid4().hex
    shutil.copytree(src, fixture_path)
    return fixture_path


def test_rename(tmp_path: Path, snapshot):
    fixtures = copy_fixtures(FIXTURES_PATH / "basic", tmp_path)
    files_before = [x.name for x in fixtures.glob("*")]
    cli([str(fixtures)])
    files_after = [x.name for x in fixtures.glob("*")]
    assert files_after != files_before
    snapshot.assert_match(files_after)


def test_dryrun(capsys, tmp_path: Path, snapshot):
    fixtures = copy_fixtures(FIXTURES_PATH / "basic", tmp_path)
    files_before = [x.name for x in fixtures.glob("*")]
    cli([str(fixtures), "--dryrun"])
    files_after = [x.name for x in fixtures.glob("*")]
    assert files_after == files_before

    out, err = capsys.readouterr()
    snapshot.assert_match(out.replace(str(fixtures.resolve()), ""))


def test_raise_when_subtitle_and_videos_number_dismatch():
    path = FIXTURES_PATH / "exclude"
    with pytest.raises(Exception):
        cli([str(path)])


def test_exclude(capsys, tmp_path: Path, snapshot):
    fixtures = copy_fixtures(FIXTURES_PATH / "exclude", tmp_path)
    files_before = [x.name for x in fixtures.glob("*")]
    cli([str(fixtures), "-e", "creditless"])
    files_after = [x.name for x in fixtures.glob("*")]
    assert files_after != files_before
    snapshot.assert_match(files_after)

    out, err = capsys.readouterr()
    snapshot.assert_match(out.replace(str(fixtures.resolve()), ""))

