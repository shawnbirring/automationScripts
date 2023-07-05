import os
import subprocess

classrooms = [
    "NE01L0143",
    "NE01L0201",
    "NE01L0245",
    "NE01L0246A",
    "NE01L0334",
    "NE01L0338",
    "NE01L0340",
    "NE10L0108",
    "NE12L0201",
    "NE18L0106",
    "NE20L0221",
    "SE12L0318",
    "SE12L0321",
    "SE12L0322",
    "SE12L0324",
]

for classroom in classrooms:
    for i in range(31):  # Adjust range as per your requirements
        station = f"{classroom}-{str(i).zfill(2)}.ad.bcit.ca"
        print(f"Pinging {station}")
        response = subprocess.run(["ping", station], stdout=subprocess.PIPE)
        print(response.stdout.decode())
