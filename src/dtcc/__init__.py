import dtcc_model
import dtcc_model as model
import dtcc_io
import dtcc_io as io
import dtcc_builder
import dtcc_builder as builder
import dtcc_viewer
import dtcc_viewer as viewer

# Collect __all__ from submodules
modules = [dtcc_model, dtcc_io]
__all__ = []
for module in modules:
    for name in module.__all__:
        globals()[name] = getattr(module, name)
    __all__ += module.__all__