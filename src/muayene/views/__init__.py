__all__ = [
    "archive",
    "create",
    "detail",
    "list",
    "prints",
    "update",
    "form",
    "base",
    "search",
]

from muayene.views.archive import (
    MuayeneArchiveView,
    MuayeneLastCreatedView,
    MuayeneWeekArchiveView,
    MuayeneMonthArciveView,
    MuayeneYearArchiveView,
)
from muayene.views.create import (
    MuayeneCreateView,
    IlacCreateView,
    MuayeneAliasCreateView,
)
from muayene.views.detail import (
    MuayeneDetailView,
)
from muayene.views.list import (
    IlacListView,
    LastCreatedLabIstekView,
    MuayeneAliasListView,
)
from muayene.views.prints import (
    RecetePrintView,
    RaporPrintView,
    LabIstekPrintView,
    TTFPrintView,
    MultiTTFPrintView,
    AHSevkPrintView,
    ListPrintView,
    BelgiumMedicalCertPrintView,
)
from muayene.views.update import (
    MuayeneUpdateView,
)
from muayene.views.form import (
    ReceteFormView,
    RaporFormView,
    LabIstekFormView,
    FileUploadFormView,
    LabSonucFormView,
    GetIlacKullanimView,
)
from muayene.views.base import MuayeneBaseView
from muayene.views.search import IlacSearchView
