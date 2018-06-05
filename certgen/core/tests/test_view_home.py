import pytest
from django.shortcuts import resolve_url as r

from certgen.django_assertions import dj_assert_template_used


@pytest.fixture
def home_resp(client):
    return client.get(r('home'))


def test_status_code_200_ok(home_resp):
    assert 200 == home_resp.status_code


def test_home_template_used(home_resp):
    dj_assert_template_used(home_resp, template_name='core/index.html')
