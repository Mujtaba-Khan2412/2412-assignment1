import json
from app import app


def test_prediction():
    client = app.test_client()
    response = client.post(
        "/predict",
        data=json.dumps({"x": 6}),
        content_type="application/json",
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "prediction" in data
