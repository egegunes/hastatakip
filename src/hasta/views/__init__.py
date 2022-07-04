__all__ = ["base", "archive", "create", "detail", "list", "update", "search"]

from hasta.views.base import HastaDetailBaseView
from hasta.views.archive import HastaLastCreatedView
from hasta.views.create import HastaCreateView, SozlesmeCreateView
from hasta.views.detail import (
    HastaDetailView,
)
from hasta.views.list import (
    HastaListView,
    SozlesmeListView,
    MuayeneListView,
    ReceteListView,
    RaporListView,
    LabIstekListView,
    DosyaListView,
    HastaEpikrizView,
)
from hasta.views.update import (
    HastaUpdateView,
)
from hasta.views.search import HastaSearchView
