
from fastapi import FastAPI
from pydantic import BaseModel
import random
import string

app = FastAPI(title="OneTap Smart ID Mock Backend")

class NFCReadResponse(BaseModel):
    name: str
    nric: str
    address: str

class BiometricRequest(BaseModel):
    session_id: str

class BiometricResponse(BaseModel):
    success: bool
    message: str

class QueueRequest(BaseModel):
    session_id: str
    clinic: str | None = None
    service: str | None = None

class QueueResponse(BaseModel):
    queue_number: str
    token: str

def generate_queue(prefix: str) -> str:
    num = random.randint(1, 199)
    return f"{prefix}{num:03d}"

def generate_token() -> str:
    body = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"qr_{body}"

@app.post("/nfc/read", response_model=NFCReadResponse)
async def nfc_read():
    """Simulate reading Smart ID data from NFC."""
    return NFCReadResponse(
        name="Ali Bin Ahmad",
        nric="99XXXX-XX-1234",
        address="Kuala Lumpur",
    )

@app.post("/verify/biometric", response_model=BiometricResponse)
async def verify_biometric(req: BiometricRequest):
    """Simulate biometric verification (always success in this mock)."""
    return BiometricResponse(success=True, message="Face match successful.")

@app.post("/queue/hospital", response_model=QueueResponse)
async def queue_hospital(req: QueueRequest):
    """Issue a hospital queue number."""
    qnum = generate_queue("A")
    token = generate_token()
    return QueueResponse(queue_number=qnum, token=token)

@app.post("/queue/government", response_model=QueueResponse)
async def queue_government(req: QueueRequest):
    """Issue a government counter queue number."""
    qnum = generate_queue("B")
    token = generate_token()
    return QueueResponse(queue_number=qnum, token=token)
