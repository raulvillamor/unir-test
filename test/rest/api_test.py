import http.client
import os
import unittest
from urllib.request import urlopen
# Importamos excepcion de urllib
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error    
    def test_api_add_fails_with_nan_parameter(self):
        
        url = f"{BASE_URL}/calc/add/4/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/add/A/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/add/A/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
    
    # Haremos uso de la excepcion Not found para comprobar que la url es imcompleta
    def test_api_add_incomplete_url(self):   
        url = f"{BASE_URL}/calc/add"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/add/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_substract_fails_with_nan_parameter(self):
        
        url = f"{BASE_URL}/calc/substract/4/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/substract/A/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/substract/A/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Not found para comprobar que la url es imcompleta    
    def test_api_substract_incomplete_url(self):   
        url = f"{BASE_URL}/calc/substract"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/substract/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_multiply_fails_with_nan_parameter(self):
        
        url = f"{BASE_URL}/calc/multiply/4/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/multiply/A/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/multiply/A/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Not found para comprobar que la url es imcompleta
    def test_api_multiply_incomplete_url(self):   
        url = f"{BASE_URL}/calc/multiply"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/multiply/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_divide_fails_with_division_by_zero(self):
        
        url = f"{BASE_URL}/calc/divide/4/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        
        url = f"{BASE_URL}/calc/divide/4/-0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

        url = f"{BASE_URL}/calc/divide/0/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        
        url = f"{BASE_URL}/calc/divide/A/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_divide_fails_with_nan_parameter(self):
        url = f"{BASE_URL}/calc/divide/4/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/divide/A/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/divide/A/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Not found para comprobar que la url es imcompleta
    def test_api_divide_incomplete_url(self):   
        url = f"{BASE_URL}/calc/divide"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/divide/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_power_fails_with_nan_parameter(self):
        url = f"{BASE_URL}/calc/power/4/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/power/A/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/power/A/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Not found para comprobar que la url es imcompleta
    def test_api_power_incomplete_url(self):   
        url = f"{BASE_URL}/calc/power"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )
        url = f"{BASE_URL}/calc/power/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )

    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )   
    
    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_square_root_method_fails_with_negative_number(self):
        # Error de operando = -1
        url = f"{BASE_URL}/calc/square_root/-1"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_square_root_fails_with_nan_parameter(self):
        url = f"{BASE_URL}/calc/square_root/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Not found para comprobar que la url es imcompleta
    def test_api_root_square_incomplete_url(self):   
        url = f"{BASE_URL}/calc/root_square"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )  

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_log10_fails_with_number_lower_zero_or_equal_zero(self):
        # Error de operando = 0
        url = f"{BASE_URL}/calc/log10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
        # Error de operando < 0
        url = f"{BASE_URL}/calc/log10/-1"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )    

    # Haremos uso de la excepcion Bad request para comprobar que aparece el error
    def test_api_log10_fails_with_nan_parameter(self):
        url = f"{BASE_URL}/calc/log10/A"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # Haremos uso de la excepcion Not found para comprobar que la url es imcompleta
    def test_api_log10_incomplete_url(self):   
        url = f"{BASE_URL}/calc/log10"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print("HttpException Occurred", e)
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Error en la petición API a {url}"
            )
