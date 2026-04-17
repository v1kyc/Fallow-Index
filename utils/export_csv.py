import csv

def export_csv(rows, filename):
    if not rows:
        return

    with open(filename, "w", newline="") as f:
        first = rows[0]
        writer = csv.DictWriter(f, fieldnames=first.keys())

        writer.writeheader()
        writer.writerows(rows)