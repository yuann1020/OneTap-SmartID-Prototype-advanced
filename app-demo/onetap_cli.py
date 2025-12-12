
import time
import random
import string

SERVICES = {
    "1": "Hospital Check-In",
    "2": "Government Counter (JPN/JPJ)",
}

CLINICS = [
    "General Clinic",
    "Specialist Clinic",
    "Paediatrics",
    "Obstetrics & Gynaecology",
    "ENT Clinic",
]

def slow_print(text, delay=0.4):
    print(text)
    time.sleep(delay)

def generate_queue(prefix):
    # e.g. A021, B104
    num = random.randint(1, 199)
    return f"{prefix}{num:03d}"

def generate_qr_token():
    # simple random token placeholder
    body = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"qr_{body}"

def simulate_nfc_read():
    slow_print("📶 Reading NFC Smart ID ...", 0.6)
    slow_print("🔐 Establishing secure channel ...", 0.6)
    slow_print("🧮 Decrypting identity token ...", 0.6)
    return {
        "name": "Ali Bin Ahmad",
        "nric": "99XXXX-XX-1234",
        "address": "Kuala Lumpur",
    }

def simulate_biometric():
    slow_print("\n📸 Performing face verification ...", 0.6)
    slow_print("✨ Analysing face features ...", 0.6)
    slow_print("✅ Face match successful!\n", 0.5)
    return True

def hospital_flow(user):
    print("\n=== Hospital Check-In ===")
    print(f"Patient: {user['name']} ({user['nric']})")
    print("Select clinic:")
    for i, clinic in enumerate(CLINICS, start=1):
        print(f"[{i}] {clinic}")
    choice = input("Enter clinic number: ").strip()
    try:
        clinic_name = CLINICS[int(choice) - 1]
    except (ValueError, IndexError):
        clinic_name = CLINICS[0]
        print("Invalid choice, defaulting to General Clinic.")
    slow_print(f"Generating queue for {clinic_name} ...", 0.7)
    qnum = generate_queue("A")
    token = generate_qr_token()
    print("\n--- Check-In Summary ---")
    print(f"Clinic       : {clinic_name}")
    print(f"Queue Number : {qnum}")
    print(f"QR Token     : {token}")
    print("-------------------------")
    print("Show this token/QR to the hospital staff.\n")

def government_flow(user):
    print("\n=== Government Counter (JPN/JPJ) ===")
    print(f"Citizen: {user['name']} ({user['nric']})")
    print("Select service:")
    gov_services = [
        "MyKad Renewal",
        "Address Update",
        "Driving License Renewal",
        "Card Replacement",
    ]
    for i, s in enumerate(gov_services, start=1):
        print(f"[{i}] {s}")
    choice = input("Enter service number: ").strip()
    try:
        service_name = gov_services[int(choice) - 1]
    except (ValueError, IndexError):
        service_name = gov_services[0]
        print("Invalid choice, defaulting to MyKad Renewal.")
    slow_print(f"Issuing queue number for {service_name} ...", 0.7)
    qnum = generate_queue("B")
    token = generate_qr_token()
    print("\n--- Counter Check-In ---")
    print(f"Service      : {service_name}")
    print(f"Queue Number : {qnum}")
    print(f"QR Token     : {token}")
    print("-------------------------")
    print("Show this token/QR to the officer at the counter.\n")

def main():
    print("=========================================")
    print("   OneTap Smart ID Verification (CLI)   ")
    print("=========================================\n")
    print("Select service:")
    for key, label in SERVICES.items():
        print(f"[{key}] {label}")
    service_choice = input("Enter option number: ").strip()
    if service_choice not in SERVICES:
        print("Invalid selection. Exiting.")
        return

    # Simulate Smart ID verification
    user = simulate_nfc_read()
    slow_print(f"👤 Identity detected: {user['name']} ({user['nric']})", 0.6)

    # Biometric step
    if not simulate_biometric():
        print("Biometric verification failed. Access denied.")
        return

    # Route to chosen flow
    if service_choice == "1":
        hospital_flow(user)
    elif service_choice == "2":
        government_flow(user)

    print("Thank you for using OneTap. Goodbye!")

if __name__ == "__main__":
    main()
