import csv
import io
import json
from flask import Response, make_response

def export_to_csv_response(rows: list, fieldnames: list, filename: str = 'export.csv') -> Response:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'
    return response

def export_to_json_response(data, filename: str = 'export.json') -> Response:
    json_str = json.dumps(data, indent=2, default=str)
    response = make_response(json_str)
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response
