from typing import List, Optional, Dict, Any
from app.models.domain import DomainCategory, DomainReputation, DomainFilterRule
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class DomainRepository(BaseRepository):
    def __init__(self):
        super().__init__(DomainCategory)

    def get_category_by_name(self, name: str) -> Optional[DomainCategory]:
        return DomainCategory.query.filter_by(name=name, is_deleted=False).first()

    def list_categories(self) -> List[DomainCategory]:
        return DomainCategory.query.filter_by(is_deleted=False).all()

    def get_domain_reputation(self, domain: str) -> Optional[DomainReputation]:
        return DomainReputation.query.filter_by(domain=domain.lower(), is_deleted=False).first()

    def upsert_domain_reputation(self, domain: str, category: str, score: int = 80, is_malicious: bool = False, threat_tags: str = None) -> DomainReputation:
        rep = self.get_domain_reputation(domain)
        if rep:
            rep.query_count += 1
            rep.last_queried_at = utc_now()
            if not rep.is_custom_override:
                rep.category = category
                rep.reputation_score = score
                rep.is_malicious = is_malicious
                rep.threat_tags = threat_tags
        else:
            rep = DomainReputation(
                domain=domain.lower(),
                category=category,
                reputation_score=score,
                is_malicious=is_malicious,
                threat_tags=threat_tags,
                query_count=1
            )
            db.session.add(rep)
        db.session.commit()
        return rep

    def list_filter_rules(self) -> List[DomainFilterRule]:
        return DomainFilterRule.query.filter_by(is_deleted=False).all()
