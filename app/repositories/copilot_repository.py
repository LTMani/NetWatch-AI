from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy import desc
from app.models.copilot import CopilotConversation, CopilotMessage
from app.models.base import db

class CopilotRepository:
    def get_or_create_conversation(self, conv_id: str = None, user_id: str = None, title: str = 'Network Investigation') -> CopilotConversation:
        if conv_id:
            c = CopilotConversation.query.get(conv_id)
            if c:
                return c
        c = CopilotConversation(title=title, user_id=user_id)
        db.session.add(c)
        db.session.commit()
        return c

    def add_message(self, conv_id: str, sender: str, content: str, intent: str = None, metrics_json: str = None, actions_json: str = None) -> CopilotMessage:
        msg = CopilotMessage(
            conversation_id=conv_id,
            sender=sender,
            content=content,
            detected_intent=intent,
            retrieved_metrics_json=metrics_json,
            suggested_actions_json=actions_json
        )
        db.session.add(msg)
        db.session.commit()
        return msg

    def list_user_conversations(self, user_id: str = None) -> List[CopilotConversation]:
        query = CopilotConversation.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        return query.order_by(desc(CopilotConversation.created_at)).limit(20).all()
