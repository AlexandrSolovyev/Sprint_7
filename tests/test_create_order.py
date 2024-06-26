import json

import allure
import pytest
import requests

from data import Data
from http import HTTPStatus
from helpers import get_body_request


@pytest.mark.get_url('create_order')
class TestCreateOrder:

    @allure.title('Проверка позитивного сценария заказа самоката '
                  'при разных вариантах указания цвета')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metro_station, phone, rent_time, delivery_date, comment, color',
        [
            (*Data.data_client, color)
            for color in Data.data_color
        ]
    )
    def test_get_order_with_diff_colors_success(
            self, get_url, firstname, lastname, address, metro_station,
            phone, rent_time, delivery_date, comment, color):
        order_lst = [firstname, lastname, address, metro_station,
                     phone, rent_time, delivery_date, comment, color]
        payload = get_body_request(order_lst)
        response = requests.post(get_url, payload)
        assert response.status_code == HTTPStatus.CREATED
        response_data = json.loads(response.text)
        assert 'track' in response_data

    @allure.title('Проверка ответа при успешном заказе самоката')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metro_station, phone, rent_time, delivery_date, comment',
        [Data.data_client]
    )
    def test_get_order_response_contains_track_success(
            self, get_url, firstname, lastname, address, metro_station,
            phone, rent_time, delivery_date, comment):
        color = []
        order_lst = [firstname, lastname, address, metro_station,
                     phone, rent_time, delivery_date, comment, color]
        payload = get_body_request(order_lst)
        response = requests.post(get_url, payload)
        assert 'track' in response.json()
