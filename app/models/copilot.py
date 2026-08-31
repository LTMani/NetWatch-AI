from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class CopilotConversation(BaseModel):
    """AI Copilot natural language interactive session."""
    __tablename__ = 'nw_copilot_conversations'

    title = Column(String(128), default='Network Investigation Session', nullable=False)
    user_id = Column(String(36), ForeignKey('nw_users.id'), nullable=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    messages = relationship('CopilotMessage', back_populates='conversation', cascade='all, delete-orphan', order_by='CopilotMessage.timestamp.asc()')

class CopilotMessage(BaseModel):
    """Individual question or grounded response in a conversation."""
    __tablename__ = 'nw_copilot_messages'

    conversation_id = Column(String(36), ForeignKey('nw_copilot_conversations.id', ondelete='CASCADE'), nullable=False, index=True)
    sender = Column(String(16), default='USER', nullable=False) # USER, COPILOT
    content = Column(Text, nullable=False)
    
    detected_intent = Column(String(64), nullable=True)
    retrieved_metrics_json = Column(Text, nullable=True)
    confidence_score = Column(Float, default=0.95, nullable=False)
    suggested_actions_json = Column(Text, nullable=True) # list of clickable actions
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    conversation = relationship('CopilotConversation', back_populates='messages')
