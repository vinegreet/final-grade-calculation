def sort_by_SID(data):
    return sorted(data, key=lambda row: row['SID'].upper())
