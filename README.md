# resubname

Rename subtitle filenames to match videos.

## Install with `pipx`

Using [pipx](https://pipxproject.github.io/pipx/) to install `resubname` is recommended.

```bash
pipx install resubname
```

## Example

```bash
> ls
 03.ass    '[VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].mkv'
 05.5.ass  '[VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].mkv'
 05.ass    '[VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].mkv'

> resubname *.ass *.mkv
03.ass -> [VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].ass
05.5.ass -> [VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].ass
05.ass -> [VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].ass
> ls
'[VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].ass'
'[VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].mkv'
'[VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].ass'
'[VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].mkv'
'[VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].ass'
'[VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].mkv'
```

And you can exclude certain files:

```bash
> ls
'[ANE] Soredemo Machi wa Mawatte Iru - EP01 [BD 1920x1080 H.264 FLAC].CASO-SC.ass'
'[ANE] Soredemo Machi wa Mawatte Iru - EP02 [BD 1920x1080 H.264 FLAC].CASO-SC.ass'
'[ANK-Raws] それでも町は廻っている (Ep_05 Creditless ED) (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv'
'[ANK-Raws] それでも町は廻っている 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv'
'[ANK-Raws] それでも町は廻っている 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv'
> resubname *.ass *.mkv -e creditless --dryrun
[ANE] Soredemo Machi wa Mawatte Iru - EP01 [BD 1920x1080 H.264 FLAC].CASO-SC.ass -> [ANK-Raws] それでも町は廻っている 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
[ANE] Soredemo Machi wa Mawatte Iru - EP02 [BD 1920x1080 H.264 FLAC].CASO-SC.ass -> [ANK-Raws] それでも町は廻っている 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
```

## Help

```
resubname -h
```

## Changelog

### v0.2.0

- Show videos and subtitiles file list when their number dismatch.
- Stop complain about "Unknown suffix" for folders. Will just ignore them.

### v0.1.0

- Initial Release
