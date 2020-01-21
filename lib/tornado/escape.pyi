# Stubs for tornado_py3.escape (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Callable, Dict, List, Union

def xhtml_escape(value: Union[str, bytes]) -> str: ...
def xhtml_unescape(value: Union[str, bytes]) -> str: ...
def json_encode(value: Any) -> str: ...
def json_decode(value: Union[str, bytes]) -> Any: ...
def squeeze(value: str) -> str: ...
def url_escape(value: Union[str, bytes], plus: bool=...) -> str: ...
def url_unescape(value: Union[str, bytes], encoding: None, plus: bool=...) -> bytes: ...
def parse_qs_bytes(qs: Union[str, bytes], keep_blank_values: bool=..., strict_parsing: bool=...) -> Dict[str, List[bytes]]: ...
def utf8(value: bytes) -> bytes: ...
def to_unicode(value: str) -> str: ...
native_str = to_unicode
to_basestring = to_unicode

def recursive_unicode(obj: Any) -> Any: ...
def linkify(text: Union[str, bytes], shorten: bool=..., extra_params: Union[str, Callable[[str], str]]=..., require_protocol: bool=..., permitted_protocols: List[str]=...) -> str: ...