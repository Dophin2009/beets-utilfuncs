from beets.plugins import BeetsPlugin


class UtilfuncsPlugin(BeetsPlugin):
    def __init__(self):
        super(UtilfuncsPlugin, self).__init__()
        self.template_funcs['dashify'] = self._dashify

    def _dashify(self, text: str) -> str:
        return text.replace(' ', '-')
