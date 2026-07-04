import sqlite3

conn = sqlite3.connect('medicines.db')

cursor = conn.cursor()

data = [

    ("fever", "Dolo 650"),
    ("fever", "Crocin"),
    ("fever", "Paracetamol"),

    ("cold", "Cetirizine"),
    ("cold", "Sinarest"),

    ("cough", "Benadryl"),
    ("cough", "Ascoril"),

    ("headache", "Paracetamol"),
    ("headache", "Saridon"),

    ("body pain", "Combiflam"),
    ("body pain", "Paracetamol"),
    ("body pain", "Aceclofenac"),

    ("knee pain", "Aceclofenac"),
    ("knee pain", "Combiflam"),
    ("knee pain", "Paracetamol"),

    ("back pain", "Aceclofenac"),
    ("back pain", "Diclofenac"),
    ("back pain", "Combiflam"),

    ("leg pain", "Paracetamol"),
    ("leg pain", "Combiflam"),
    ("leg pain", "Aceclofenac"),

    ("neck pain", "Diclofenac"),
    ("neck pain", "Combiflam"),

    ("joint pain", "Aceclofenac"),
    ("joint pain", "Paracetamol"),

    ("muscle pain", "Combiflam"),
    ("muscle pain", "Diclofenac"),

    ("tooth pain", "Paracetamol"),
    ("tooth pain", "Combiflam"),

    ("ear pain", "Paracetamol"),

    ("acidity", "Digene"),
    ("acidity", "Gelusil"),

    ("stomach pain", "Meftal Spas"),
    ("stomach pain", "Buscopan"),

    ("allergy", "Cetirizine"),
    ("allergy", "Levocetirizine"),

    ("sore throat", "Strepsils"),
    ("sore throat", "Benadryl"),

    ("vomiting", "Ondem"),
    ("vomiting", "Domstal"),

    ("diarrhea", "ORS"),
    ("diarrhea", "Loperamide")
]

cursor.executemany(
    "INSERT INTO medicines (problem, medicine) VALUES (?, ?)",
    data
)

conn.commit()
conn.close()

print("Medicine Data Inserted Successfully")