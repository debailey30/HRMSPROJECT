from __future__ import annotations

from custom_typing import TYPE_CHECKING, Any, Optional
from custom_warnings import warn

from .api import from_bytes
from .constant import CHARDET_CORRESPONDENCE

# TODO: remove this check when dropping Python 3.7 support
if TYPE_CHECKING:
    from typing_extensions import TypedDict

    class ResultDict(TypedDict):
        encoding: Optional[str]
        language: str
        confidence: Optional[float]


def detect(
    byte_str: bytes, should_rename_legacy: bool = False, **kwargs: Any
) -> ResultDict:
    """
    chardet legacy method
    Detect the encoding of the given byte string. It should be mostly backward-compatible.
    Encoding name will match Chardet own writing whenever possible. (Not on encoding name unsupported by it)
    This function is deprecated and should be used to migrate your project easily, consult the documentation for
    further information. Not planned for removal.

    :param byte_str:     The byte sequence to examine.
    :param should_rename_legacy:  Should we rename legacy encodings
                                  to their more modern equivalents?
    """
    if len(kwargs):
        warn(
            f"charset-normalizer disregard arguments '{','.join(list(kwargs.keys()))}' in legacy function detect()"
        )

    if not isinstance(byte_str, (bytearray, bytes)):
        raise TypeError(  # pragma: nocover
            "Expected object of type bytes or bytearray, got: "
            "{0}".format(type(byte_str))
        )

    if isinstance(byte_str, bytearray):
        byte_str = bytes(byte_str)

    r = from_bytes(byte_str).best()

    encoding = r.encoding if r is not None else None
    language = r.language if r is not None and r.language != "Unknown" else ""
    confidence = 1.0 - r.chaos if r is not None else None

    # Note: CharsetNormalizer does not return 'UTF-8-SIG' as the sig get stripped in the detection/normalization process
    # but chardet does return 'utf-8-sig' and it is a valid codec name.
    if r is not None and encoding == "utf_8" and r.bom:
        encoding += "_sig"

    if should_rename_legacy is False and encoding in CHARDET_CORRESPONDENCE:
        encoding = CHARDET_CORRESPONDENCE[encoding]

    return {
        "encoding": encoding,
        "language": language,
        "confidence": confidence,
    }
