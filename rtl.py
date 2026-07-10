import arabic_reshaper
from bidi.algorithm import get_display

def rtl(text):
    """
    تحويل النص العربي ليظهر بشكل صحيح داخل PDF.
    """
    if text is None:
        return ""

    text = str(text).strip()

    if text == "" or text.lower() == "nan":
        return ""

    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)
