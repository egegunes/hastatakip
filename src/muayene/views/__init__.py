__all__ = ["archive", "create", "detail", "list", "prints", "update", "form", "base", "search", "autocomplete"]

from muayene.views.archive  import (
    MuayeneArchiveView, 
    MuayeneLastCreatedView,
    MuayeneWeekArchiveView,
    MuayeneMonthArciveView,
    MuayeneYearArchiveView
)
from muayene.views.create   import (
    MuayeneCreateView, 
    ReceteCreateView,
    TetkikCreateView
)
from muayene.views.detail   import (
    MuayeneDetailView, 
)
from muayene.views.list     import (
    IlacListView,
    LastCreatedLabIstekView,
    MuayeneAliasListView
)
from muayene.views.prints   import (
    RecetePrintView, 
    RaporPrintView, 
    LabIstekPrintView,
    TTFPrintView,
    MultiTTFPrintView,
    AHSevkPrintView,
    ListPrintView
)
from muayene.views.update   import MuayeneUpdateView, LaboratuvarIstekUpdateView
from muayene.views.form     import (
    RaporFormView,
    FileUploadFormView,
    GetIlacKullanimView
)
from muayene.views.base     import (
    MuayeneBaseView        
)
from muayene.views.search   import (
    IlacSearchView
)
from muayene.views.autocomplete import IlacAutocomplete, LabAutocomplete
