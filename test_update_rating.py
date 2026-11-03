import pytest


# Test boundary values when updating a rating.
@pytest.mark.parametrize(
    "stars, expected_status",
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400),
    ],
)
def test_update_rating_boundary_values(
    api, auth, rating, stars, expected_status
):
    path = f"/api/ratings/{rating['id']}"

    # Try to update the rating.
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    # Read the rating back to check whether it changed.
    saved = api.get(path, headers=auth)
    assert saved.status_code == 200

    expected_stars = stars if expected_status == 200 else 3
    assert saved.json()["stars"] == expected_stars
