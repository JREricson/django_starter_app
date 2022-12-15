from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_core_landing_page(client):
    res = client.get(reverse("core-landing"))
    assert res.status_code == 200
    assertTemplateUsed(res, 'core_landing_page.html' )
