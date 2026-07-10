import pandas as pd
from pathlib import Path

from config import INPUT_FILE


def load_workbook():
    """
    تحميل ملف Excel وإرجاع جميع الشيتات.
    """

    file_path = Path(INPUT_FILE)

    if not file_path.exists():
        raise FileNotFoundError(
            f"لم يتم العثور على الملف: {INPUT_FILE}"
        )

    return pd.read_excel(
        file_path,
        sheet_name=None,
        dtype=str
    )


def clean_value(value):
    """
    تنظيف القيم الفارغة.
    """

    if pd.isna(value):
        return ""

    value = str(value).strip()

    if value.lower() == "nan":
        return ""

    return value


def get_sheet_data(sheet_name):
    """
    قراءة بيانات شيت معين.
    """

    workbook = load_workbook()

    if sheet_name not in workbook:
        return []

    df = workbook[sheet_name]

    df = df.fillna("")

    records = []

    for _, row in df.iterrows():

        item = {}

        for col in df.columns:
            item[str(col).strip()] = clean_value(row[col])

        records.append(item)

    return records


def get_all_sheets():

    workbook = load_workbook()

    return workbook.keys()
