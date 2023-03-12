from jinja2 import nodes
from jinja2.ext import Extension
from pathlib import Path


class IncludeFileExtension(Extension):
    """
    Create a Jinja2 `{% include_file_raw <path> %}` tag. `<path>` is relative to
    the templates directory. The included file will not be processed at all. The
    files contents will be inserted raw into the location of the tag.
    """

    tags = set(['include_file_raw'])

    def _include_file_raw(self, name, caller):
        contents = Path('./templates/' + name).read_text()
        return contents

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        name = [parser.parse_expression()]  # string
        node = self.call_method('_include_file_raw', name, lineno=lineno)
        return nodes.CallBlock(node, [], [], [], lineno=lineno)
