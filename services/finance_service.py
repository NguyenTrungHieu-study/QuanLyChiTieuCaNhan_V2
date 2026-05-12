import pandas as pd
from models.database import get_connection
import time

class FinanceService:
    def __init__(self):
        pass

    def get_categories(self) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories ORDER BY id")
        rows = cursor.fetchall()
        conn.close()
        return [dict(r)['name'] for r in rows]

    def add_category(self, name: str):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            conn.commit()
        except Exception:
            pass
        conn.close()

    def update_category_name(self, old_name: str, new_name: str):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE categories SET name=? WHERE name=?", (new_name, old_name))
            cursor.execute("UPDATE transactions SET category=? WHERE category=?", (new_name, old_name))
            conn.commit()
        except Exception:
            pass
        conn.close()

    def delete_category(self, name: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categories WHERE name=?", (name,))
        conn.commit()
        conn.close()

    def add_transaction(self, date: str, amount: float, category: str, t_type: str, note: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (date, amount, category, type, note)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, amount, category, t_type, note))
        conn.commit()
        conn.close()

    def update_transaction(self, t_id: int, date: str, amount: float, category: str, t_type: str, note: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE transactions
            SET date=?, amount=?, category=?, type=?, note=?
            WHERE id=?
        ''', (date, amount, category, t_type, note, t_id))
        conn.commit()
        conn.close()

    def delete_transactions(self, ids: list):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.executemany('DELETE FROM transactions WHERE id=?', [(i,) for i in ids])
        conn.commit()
        
        cursor.execute('SELECT COUNT(*) FROM transactions')
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='transactions'")
            conn.commit()
            
        conn.close()

    def import_from_csv(self, filepath: str):
        time.sleep(3.5) # Mô phỏng tác vụ nặng trên 3 giây
        df = pd.read_csv(filepath)
        conn = get_connection()
        df.to_sql('transactions', conn, if_exists='append', index=False)
        conn.close()

    def export_to_csv(self, filepath: str):
        time.sleep(3.5) # Mô phỏng tác vụ nặng trên 3 giây
        df = self.get_all_transactions()
        df.to_csv(filepath, index=False)

    def get_all_transactions(self) -> pd.DataFrame:
        conn = get_connection()
        df = pd.read_sql_query("SELECT * FROM transactions", conn)
        conn.close()
        
        if not df.empty:
            df['date'] = pd.to_datetime(df['date'], format='mixed')
            df = df.sort_values(by='date')
        return df

    def get_expenses_by_category(self) -> pd.DataFrame:
        df = self.get_all_transactions()
        if df.empty:
            return pd.DataFrame()
            
        expenses = df[df['type'] == 'Chi tiêu']
        if expenses.empty:
            return pd.DataFrame()
            
        return expenses.groupby('category')['amount'].sum().reset_index()

    def get_spending_trend(self) -> pd.DataFrame:
        time.sleep(3.5) # Mô phỏng tác vụ nặng trên 3 giây
        df = self.get_all_transactions()
        if df.empty:
            return pd.DataFrame()
            
        expenses = df[df['type'] == 'Chi tiêu'].copy()
        if expenses.empty:
            return pd.DataFrame()
            
        # Resample by month
        expenses.set_index('date', inplace=True)
        monthly_expenses = expenses.resample('ME')['amount'].sum().reset_index()
        
        # Calculate Moving Average (3 months)
        monthly_expenses['moving_avg'] = monthly_expenses['amount'].rolling(window=3, min_periods=1).mean()
        
        return monthly_expenses

    def get_recent_transactions(self, limit=1000, keyword="") -> list:
        conn = get_connection()
        cursor = conn.cursor()
        if keyword:
            query = "SELECT * FROM transactions WHERE category LIKE ? OR note LIKE ? ORDER BY date DESC, id DESC LIMIT ?"
            cursor.execute(query, (f"%{keyword}%", f"%{keyword}%", limit))
        else:
            cursor.execute("SELECT * FROM transactions ORDER BY date DESC, id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
