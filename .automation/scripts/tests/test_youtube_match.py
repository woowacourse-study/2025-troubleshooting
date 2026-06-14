"""youtube_match 순수 매칭 로직 테스트 (표준 라이브러리 unittest)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from youtube_match import (
    normalize,
    parse_video_title,
    find_matches,
    build_register_url,
)


class TestNormalize(unittest.TestCase):
    def test_removes_all_whitespace(self):
        self.assertEqual(normalize("메시지 저장 구조 설계"), "메시지저장구조설계")

    def test_removes_tabs_and_multiple_spaces(self):
        self.assertEqual(normalize("a  b\tc"), "abc")

    def test_none_returns_empty(self):
        self.assertEqual(normalize(None), "")


class TestParseVideoTitle(unittest.TestCase):
    def test_splits_title_and_presenter(self):
        self.assertEqual(
            parse_video_title("메시지 저장 구조 설계 | 모코"),
            ("메시지 저장 구조 설계", "모코"),
        )

    def test_no_pipe_returns_none(self):
        self.assertIsNone(parse_video_title("파이프 없는 제목"))

    def test_uses_last_pipe_as_separator(self):
        # 제목 안에 |가 있어도 마지막 |를 발표자 구분자로
        self.assertEqual(
            parse_video_title("A | B | 새로이"),
            ("A | B", "새로이"),
        )


class TestFindMatches(unittest.TestCase):
    def _pres(self, title, presenter, youtube=None):
        return {"title": title, "presenter": presenter, "youtube": youtube}

    def _vid(self, raw_title, vid):
        return {"title": raw_title, "video_id": vid}

    def test_auto_match_when_title_equal_ignoring_spaces(self):
        presentations = [self._pres("메시지 저장 구조 설계", "모코")]
        videos = [self._vid("메시지저장구조설계 | 모코", "AAA")]

        result = find_matches(presentations, videos)

        self.assertEqual(len(result["auto"]), 1)
        pres, url = result["auto"][0]
        self.assertEqual(pres["presenter"], "모코")
        self.assertEqual(url, "https://www.youtube.com/watch?v=AAA")
        self.assertEqual(result["candidates"], [])

    def test_word_difference_is_not_auto_but_candidate(self):
        presentations = [self._pres("신비로운 인덱스지식", "새로이")]
        videos = [self._vid("신비한 인덱스 지식 | 새로이", "BBB")]

        result = find_matches(presentations, videos)

        self.assertEqual(result["auto"], [])
        self.assertEqual(len(result["candidates"]), 1)
        pres, cands = result["candidates"][0]
        self.assertEqual(pres["presenter"], "새로이")
        self.assertEqual(cands[0]["video_id"], "BBB")

    def test_presenter_mismatch_excluded_from_candidates(self):
        presentations = [self._pres("어떤 발표", "메이")]
        videos = [self._vid("어떤 발표 | 모코", "CCC")]

        result = find_matches(presentations, videos)

        self.assertEqual(result["auto"], [])
        self.assertEqual(len(result["candidates"]), 1)
        pres, cands = result["candidates"][0]
        self.assertEqual(cands, [])  # 발표자 다른 영상은 후보에서 제외

    def test_already_filled_is_skipped_not_touched(self):
        presentations = [
            self._pres("메시지 저장 구조 설계", "모코", youtube="https://youtu.be/old")
        ]
        videos = [self._vid("메시지저장구조설계 | 모코", "AAA")]

        result = find_matches(presentations, videos)

        self.assertEqual(result["auto"], [])
        self.assertEqual(result["candidates"], [])
        self.assertEqual(result["skipped_filled"], presentations)

    def test_presenter_match_ignores_spaces(self):
        presentations = [self._pres("제목", "새 로이")]
        videos = [self._vid("제목 | 새로이", "DDD")]

        result = find_matches(presentations, videos)

        self.assertEqual(len(result["auto"]), 1)


class TestBuildRegisterUrl(unittest.TestCase):
    def test_includes_template_and_encoded_fields(self):
        from urllib.parse import quote

        url = build_register_url("owner/repo", 20, "모코", "https://youtu.be/x?y=1")

        self.assertTrue(url.startswith("https://github.com/owner/repo/issues/new?"))
        self.assertIn("template=youtube-presentation.yml", url)
        self.assertIn("week=20", url)
        self.assertIn("presenter=" + quote("모코"), url)
        # youtube URL의 ? & = 가 인코딩되어 쿼리 구조를 깨지 않아야 함
        self.assertIn("youtube=" + quote("https://youtu.be/x?y=1"), url)


if __name__ == "__main__":
    unittest.main()
