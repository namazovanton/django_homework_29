import csv
import json


def csv_to_json(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            del row["id"]
            if "price" in row:
                row["price"] = int(row["price"])

            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False

            if "location_id" in row:
                row["location"] = [row["location_id"]]
                del row["location_id"]

            result.append({"model": model, "fields": row})

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


csv_to_json("data_29/category.csv", "data_29/category.json", "ads.category")
csv_to_json("data_29/ad.csv", "data_29/ad.json", "ads.ad")

csv_to_json("data_29/user.csv", "data_29/user.json", "users.user")
csv_to_json("data_29/location.csv", "data_29/location.json", "users.location")
