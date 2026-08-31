import re
from typing import Dict, Any, Tuple, Optional
from app.models.domain import DomainCategory, DomainReputation, DomainFilterRule
from app.repositories.domain_repository import DomainRepository
from app.constants import DomainCategoryEnum
from app.utils.validators import validate_domain_name

# Comprehensive Enterprise Known Domain Categorization Database
KNOWN_DOMAIN_DATABASE = {
    # Development & Engineering
    'github.com': ('Development', 95, False),
    'gitlab.com': ('Development', 95, False),
    'bitbucket.org': ('Development', 90, False),
    'stackoverflow.com': ('Development', 95, False),
    'stackexchange.com': ('Development', 90, False),
    'npmjs.com': ('Development', 90, False),
    'pypi.org': ('Development', 90, False),
    'docker.com': ('Development', 90, False),
    'hub.docker.com': ('Development', 90, False),
    'postman.com': ('Development', 90, False),
    'sentry.io': ('Development', 90, False),
    'datadoghq.com': ('Development', 90, False),
    'grafana.com': ('Development', 90, False),
    'jetbrains.com': ('Development', 95, False),
    
    # Documentation & Learning
    'docs.python.org': ('Documentation', 95, False),
    'developer.mozilla.org': ('Documentation', 95, False),
    'react.dev': ('Documentation', 95, False),
    'flask.palletsprojects.com': ('Documentation', 95, False),
    'docs.microsoft.com': ('Documentation', 95, False),
    'cloud.google.com': ('Documentation', 95, False),
    'docs.aws.amazon.com': ('Documentation', 95, False),
    'wikipedia.org': ('Documentation', 90, False),
    
    # Cloud Services & Infrastructure
    'aws.amazon.com': ('Cloud Services', 95, False),
    'amazonaws.com': ('Cloud Services', 95, False),
    'azure.microsoft.com': ('Cloud Services', 95, False),
    'cloudflare.com': ('Cloud Services', 95, False),
    'digitalocean.com': ('Cloud Services', 90, False),
    'gcp.google.com': ('Cloud Services', 95, False),
    'vercel.com': ('Cloud Services', 90, False),
    
    # Business & Productivity
    'microsoft.com': ('Business', 95, False),
    'office.com': ('Business', 95, False),
    'google.com': ('Business', 95, False),
    'atlassian.com': ('Business', 95, False),
    'jira.com': ('Business', 95, False),
    'notion.so': ('Business', 90, False),
    'salesforce.com': ('Business', 95, False),
    'workday.com': ('Business', 95, False),
    'servicenow.com': ('Business', 95, False),
    'docusign.com': ('Business', 95, False),
    
    # Communication
    'slack.com': ('Communication', 95, False),
    'zoom.us': ('Communication', 90, False),
    'teams.microsoft.com': ('Communication', 95, False),
    'discord.com': ('Communication', 75, False),
    'webex.com': ('Communication', 90, False),
    
    # Social Media
    'twitter.com': ('Social Media', 60, False),
    'x.com': ('Social Media', 60, False),
    'facebook.com': ('Social Media', 50, False),
    'instagram.com': ('Social Media', 50, False),
    'linkedin.com': ('Social Media', 85, False),
    'reddit.com': ('Social Media', 55, False),
    'tiktok.com': ('Social Media', 40, False),
    
    # Streaming & Entertainment
    'youtube.com': ('Streaming', 65, False),
    'netflix.com': ('Streaming', 50, False),
    'spotify.com': ('Streaming', 60, False),
    'twitch.tv': ('Streaming', 45, False),
    'hulu.com': ('Streaming', 45, False),
    'disneyplus.com': ('Streaming', 45, False),
    
    # Shopping
    'amazon.com': ('Shopping', 70, False),
    'ebay.com': ('Shopping', 65, False),
    'walmart.com': ('Shopping', 70, False),
    
    # Cryptocurrency
    'binance.com': ('Cryptocurrency', 50, False),
    'coinbase.com': ('Cryptocurrency', 60, False),
    'kraken.com': ('Cryptocurrency', 50, False),
    
    # Known Suspicious / Malicious patterns
    'evil-c2-server.net': ('Malicious', 5, True),
    'malware-drop-zone.cc': ('Malicious', 2, True),
    'phishing-verify-auth.xyz': ('Suspicious', 10, True),
    'crypto-miner-pool.top': ('Suspicious', 15, True),
    'dns-tunneling-probe.biz': ('Suspicious', 20, True)
}

class DomainClassificationEngine:
    def __init__(self, domain_repo: DomainRepository = None):
        self.domain_repo = domain_repo or DomainRepository()

    def classify_domain(self, domain_raw: str) -> Tuple[str, int, bool, str]:
        """
        Classifies domain into category, reputation score, malicious flag, and description.
        Uses exact match -> Suffix match -> Heuristic regex match -> Default Unknown.
        """
        try:
            clean_domain = validate_domain_name(domain_raw)
        except Exception:
            return DomainCategoryEnum.UNKNOWN.value, 50, False, 'Invalid Domain Syntax'

        # 1. Check direct database overrides
        rep = self.domain_repo.get_domain_reputation(clean_domain)
        if rep and rep.is_custom_override:
            return rep.category, rep.reputation_score, rep.is_malicious, 'Custom Override'

        # 2. Check Static Knowledgebase
        if clean_domain in KNOWN_DOMAIN_DATABASE:
            cat, score, mal = KNOWN_DOMAIN_DATABASE[clean_domain]
            return cat, score, mal, 'Static Knowledge Base'

        # 3. Suffix / Subdomain Matching (e.g. api.github.com -> github.com)
        parts = clean_domain.split('.')
        for i in range(1, len(parts) - 1):
            parent = '.'.join(parts[i:])
            if parent in KNOWN_DOMAIN_DATABASE:
                cat, score, mal = KNOWN_DOMAIN_DATABASE[parent]
                return cat, score, mal, f'Inherited from {parent}'

        # 4. Threat Keyword Classifiers
        if any(k in clean_domain for k in ('c2', 'botnet', 'payload', 'exploit', 'ransom')):
            return DomainCategoryEnum.SUSPICIOUS.value, 20, True, 'Suspicious Keyword Pattern'

        # 5. Heuristic TLD & Keyword Classifiers
        if any(clean_domain.endswith(tld) for tld in ('.top', '.xyz', '.cc', '.buzz', '.work', '.gq', '.tk')):
            return DomainCategoryEnum.SUSPICIOUS.value, 35, False, 'High-Risk Generic TLD'

        if any(k in clean_domain for k in ('git', 'code', 'dev', 'api', 'repo', 'build', 'ci')):
            return DomainCategoryEnum.DEVELOPMENT.value, 80, False, 'Developer Keyword Heuristic'

        if any(k in clean_domain for k in ('doc', 'learn', 'tutorial', 'wiki', 'guide')):
            return DomainCategoryEnum.DOCUMENTATION.value, 85, False, 'Documentation Keyword Heuristic'

        return DomainCategoryEnum.UNKNOWN.value, 70, False, 'Uncategorized Enterprise Traffic'

    def evaluate_filter_rules(self, domain: str) -> Optional[Dict[str, Any]]:
        """Evaluates administrator domain filtering and blocking rules."""
        rules = self.domain_repo.list_filter_rules()
        clean = domain.lower().strip()
        for rule in rules:
            if not rule.is_enabled:
                continue
            pattern = rule.domain_pattern.lower()
            if pattern == clean or (pattern.startswith('*.') and clean.endswith(pattern[1:])):
                return {
                    'blocked': rule.action == 'BLOCK',
                    'action': rule.action,
                    'reason': rule.reason,
                    'rule_id': rule.id
                }
        return None
