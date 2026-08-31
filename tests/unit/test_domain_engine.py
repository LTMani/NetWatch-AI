import pytest
from app.services.domain_engine import DomainClassificationEngine

def test_domain_classification(app):
    engine = DomainClassificationEngine()
    cat, score, mal, reason = engine.classify_domain('github.com')
    assert cat == 'Development'
    assert score >= 90
    assert mal is False

def test_subdomain_inheritance(app):
    engine = DomainClassificationEngine()
    cat, score, mal, reason = engine.classify_domain('api.github.com')
    assert cat == 'Development'

def test_malicious_keyword_heuristic(app):
    engine = DomainClassificationEngine()
    cat, score, mal, reason = engine.classify_domain('c2-beacon-exploit.xyz')
    assert mal is True
