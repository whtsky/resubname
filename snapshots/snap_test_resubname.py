# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_exclude 1'] = [
    '[ANK-Raws] それでも町は廻っている 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass',
    '[ANK-Raws] それでも町は廻っている 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv',
    '[ANK-Raws] それでも町は廻っている (Ep_05 Creditless ED) (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv',
    '[ANK-Raws] それでも町は廻っている 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass',
    '[ANK-Raws] それでも町は廻っている 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv'
]

snapshots['test_rename 1'] = [
    '[VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].ass',
    '[VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].mkv',
    '[VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].ass',
    '[VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].mkv',
    '[VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].ass',
    '[VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].mkv'
]

snapshots['test_dryrun 1'] = '''
/03.ass -> /[VCB-Studio] GIRLS und PANZER [03][Ma10p_1080p][x265_flac].ass
/05.5.ass -> /[VCB-Studio] GIRLS und PANZER [05.5][Ma10p_1080p][x265_flac].ass
/05.ass -> /[VCB-Studio] GIRLS und PANZER [05][Ma10p_1080p][x265_flac].ass
'''

snapshots['test_exclude 2'] = '''
/[ANE] Soredemo Machi wa Mawatte Iru - EP01 [BD 1920x1080 H.264 FLAC].CASO-SC.ass -> /[ANK-Raws] それでも町は廻っている 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
/[ANE] Soredemo Machi wa Mawatte Iru - EP02 [BD 1920x1080 H.264 FLAC].CASO-SC.ass -> /[ANK-Raws] それでも町は廻っている 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
'''
