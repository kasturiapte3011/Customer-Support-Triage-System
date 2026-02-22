from fastapi import FastAPI, HTTPException, Body
from core.triage_chain import run_triage
from db.crud import create_ticket, fetch_tickets, update_ticket_status

app = FastAPI(title="Customer Support Triage System")


def process_ticket_intake(message: str, channel: str):
    """
    Runs triage, creates ticket, stores in DB.
    """

    triage = run_triage(message)

    create_ticket(
        message=message,
        summary=triage["summary"],
        category=triage["category"],
        priority=triage["priority"],
        channel=channel,
        confidence=triage["confidence"],
    )


@app.post("/ingest/chat")
def ingest_chat(message: str = Body(..., embed=True)):
    """
    Accepts chat-style input.
    Does NOT expose triage details to user.
    """

    if not message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    process_ticket_intake(
        message=message,
        channel="chat"
    )

    return {
        "message": (
            "Thank you for contacting support. Your query has been recorded and our support team will get in touch with you shortly."
        )
    }


@app.post("/ingest/email")
def ingest_email(message: str = Body(..., embed=True)):
    """
    Placeholder for email ingestion.
    In future, this will be triggered by an email listener.
    """

    if not message.strip():
        raise HTTPException(status_code=400, detail="Email body cannot be empty")

    process_ticket_intake(
        message=message,
        channel="email"
    )

    # Placeholder response (email auto-reply simulation)
    return {
        "message": (
            "We have received your email and created a support ticket. Our support team will contact you soon."
        )
    }


@app.get("/admin/tickets")
def get_tickets(status: str = Body(..., embed=True)):
    '''
    Fetch tickets filtered by status.
    '''
    rows = fetch_tickets(status)
    return [
        {
            "ticket_id": r[0],
            "customer_message":r[1],
            "summary":r[2],
            "category": r[3],
            "priority": r[4],
            "status": r[5],
            "channel": r[6],
            "confidence_score":r[7],
            "created_at": r[8]
        }
        for r in rows
    ]


@app.patch("/admin/ticketupdate")
def update_status(ticket_id: str = Body(..., embed=True), status: str = Body(..., embed=True)):
    """
    Updates ticket status (admin only).
    Human-in-the-loop action.
    """

    if status not in {"NEW", "IN_PROCESS", "RESOLVED"}:
        raise HTTPException(status_code=400, detail="Invalid status")

    update_ticket_status(ticket_id, status)

    return {
        "message": "Ticket status updated successfully"
    }
