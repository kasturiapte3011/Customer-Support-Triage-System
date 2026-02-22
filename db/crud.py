from db.database import get_connection
from datetime import datetime
import uuid

def generate_ticket_id():
    return f"TCKT-{datetime.utcnow().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

def create_ticket(message, summary, category, priority, channel, confidence):
    conn = get_connection()
    cursor = conn.cursor()

    ticket_id = generate_ticket_id()

    cursor.execute("""
        INSERT INTO support_tickets (
            ticket_id, customer_message, summary, category, priority, status, channel, confidence_score
        )
        VALUES (?, ?, ?, ?, ?, 'NEW', ?, ?)
    """, (
        ticket_id, message, summary, category, priority, channel, confidence
    ))

    conn.commit()
    conn.close()

    return ticket_id


def fetch_tickets(status: str = None):
    conn = get_connection()
    cursor = conn.cursor()

    if status:
        cursor.execute("""
            SELECT ticket_id, customer_message, summary, category, priority, status, channel, confidence_score, created_at
            FROM support_tickets
            WHERE status = ?
            ORDER BY created_at DESC
        """, (status,))
    else:
        cursor.execute("""
            SELECT ticket_id, customer_message, summary, category, priority, status, channel, confidence_score, created_at
            FROM support_tickets
            ORDER BY created_at DESC
        """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def update_ticket_status(ticket_id: str, status: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE support_tickets
        SET status = ?, updated_at = CURRENT_TIMESTAMP
        WHERE ticket_id = ?
    """, (status, ticket_id))

    conn.commit()
    conn.close()
