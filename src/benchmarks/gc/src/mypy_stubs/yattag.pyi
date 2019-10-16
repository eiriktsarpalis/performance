from typing import Optional
from yattag.simpledoc import SimpleDoc

class Doc:
    def tag(self, tag_name: str, style: Optional[str] = None) -> SimpleDoc.Tag: ...
    def text(self, text: str) -> None: ...
    def line(self, tag_name: str, text: str, colspan: Optional[int] = None) -> None: ...
    def getvalue(self) -> str: ...

def indent(s: str, indent_text: bool = False) -> str: ...