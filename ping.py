import subprocess

classrooms = [
    "SE10L0102",
    "SE10L0130",
    "SE10L0131",
]


for classroom in classrooms:
    for i in range(31):  # Adjust range as per your requirements
        station = f"{classroom}-{str(i).zfill(2)}.ad.bcit.ca"
        print(f"Pinging {station}")
        response = subprocess.run(["ping", station], stdout=subprocess.PIPE)
        print(response.stdout.decode())
