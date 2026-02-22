from db.database import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS support_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id TEXT UNIQUE NOT NULL,
        customer_message TEXT NOT NULL,
        summary TEXT,
        category TEXT CHECK(category IN ('Billing', 'Technical', 'Account', 'Other')) NOT NULL,
        priority TEXT CHECK(priority IN ('High', 'Medium', 'Low')) NOT NULL,
        status TEXT CHECK(status IN ('NEW', 'IN_PROCESS', 'RESOLVED')) NOT NULL DEFAULT 'NEW',
        channel TEXT CHECK(channel IN ('email', 'chat')) NOT NULL,
        confidence_score REAL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
