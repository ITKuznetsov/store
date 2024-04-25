from typing import Any

class TittleMixin:
    title = None

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super(TittleMixin, self).get_context_data(**kwargs)
        context["title"] = self.title
        return context
    