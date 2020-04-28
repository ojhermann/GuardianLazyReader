from typing import Tuple

from guardian_api.main.guardian_content import GuardianContent


def tuple_to_guardian_dict(t: Tuple[str, str, str, str, bool, str, str, str, str, str, str, str, str]) -> dict:
    return {
        'apiUrl': t[0],
        'fields': {'bodyText': t[1]},
        'id': t[2],
        'isHosted': t[3],
        'pillarId': t[4],
        'pillarName': t[5],
        'sectionId': t[6],
        'sectionName': t[7],
        'type': t[8],
        'webPublicationDate': t[9],
        'webTitle': t[10],
        'webUrl': t[11]
    }


def tuple_to_guardian_content(
        t: Tuple[str, str, str, str, bool, str, str, str, str, str, str, str, str]) -> GuardianContent:
    guardian_dict: dict = tuple_to_guardian_dict(t)
    return GuardianContent(guardian_dict=guardian_dict)
