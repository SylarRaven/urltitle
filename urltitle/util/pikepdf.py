"""Get PDF title using pikepdf in a separate process."""

from concurrent.futures import ProcessPoolExecutor
from io import BytesIO


def _get_pdf_title(pdf_bytes: bytes) -> str:
    import pikepdf  # This must be imported only here. Workaround for https://github.com/pikepdf/pikepdf/issues/27
    pdf = pikepdf.open(BytesIO(pdf_bytes))

    title = str(pdf.docinfo.get('/Title', '')).strip()
    if not title:
        metadata = pdf.open_metadata()
        try:
            title = metadata.get('dc:title')
        except AttributeError:  # Workaround for https://github.com/pikepdf/pikepdf/issues/23
            pass
        else:
            title = str(title or '').strip()  # Workaround for https://github.com/pikepdf/pikepdf/issues/28
    return title


def get_pdf_title(pdf_bytes: bytes) -> str:
    with ProcessPoolExecutor(max_workers=1) as executor:
        return next(executor.map(_get_pdf_title, [pdf_bytes]))
