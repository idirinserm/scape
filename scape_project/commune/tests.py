from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from commune.models import Commune


class CommuneAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.commune_data = {
            'insee': '12345',
            'nom': 'Test Commune',
            'part75_plus': 50,
            'evo75_plus': 5,
            'parretrait': 10,
            'evo65seuls': 2,
            'mediane': 30000,
            'mediane75': 35000,
            'partT5': 15,
            'partmaison': 70,
            'a60ascenseu': 25,
            'popasdense': 5000,
            'partT5rp': 20,
            'diffrevenu': 5000,
            'cadres55an': 100,
            's15_19seuls': 20,
            's20_24seuls': 30,
            't1529total': 500,
            'part1524se': 40,
            'atlasnb': 200,
            'placetud': 300,
            'densitplac': 10,
            'evojeunes': 2.5,
            'T1T2': 30,
            'locataires': 60,
            'geom': 'MULTIPOLYGON (((0 0, 0 1, 1 1, 1 0, 0 0)))'
        }
        self.commune = Commune.objects.create(**self.commune_data)

    def test_create_commune(self):
        url = reverse('commune-list')
        new_commune_data = {
            'insee': '67890',
            'nom': 'New Commune',
            'part75_plus': 60,
            'evo75_plus': 10,
            'parretrait': 20,
            'evo65seuls': 3,
            'mediane': 35000,
            'mediane75': 40000,
            'partT5': 20,
            'partmaison': 80,
            'a60ascenseu': 30,
            'popasdense': 6000,
            'partT5rp': 25,
            'diffrevenu': 6000,
            'cadres55an': 150,
            's15_19seuls': 30,
            's20_24seuls': 40,
            't1529total': 600,
            'part1524se': 50,
            'atlasnb': 300,
            'placetud': 400,
            'densitplac': 15,
            'evojeunes': 3.5,
            'T1T2': 40,
            'locataires': 70,
            'geom': 'MULTIPOLYGON (((0 0, 0 2, 2 2, 2 0, 0 0)))'
        }
        response = self.client.post(url, new_commune_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_commune_list(self):
        url = reverse('commune-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data['features'][0]['properties']['nom'], self.commune.nom)

    def test_get_commune_detail(self):
        url = reverse('commune-detail', args=[self.commune.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_commune(self):
        url = reverse('commune-detail', args=[self.commune.id])
        updated_commune_data = {
            'nom': 'Updated Commune',
            'part75_plus': 70,
            'evo75_plus': 15,
            'parretrait': 30,
            'evo65seuls': 4,
            'mediane': 40000,
            'mediane75': 45000,
            'partT5': 25,
            'partmaison': 90,
            'a60ascenseu': 35,
            'popasdense': 7000,
            'partT5rp': 30,
            'diffrevenu': 7000,
            'cadres55an': 200,
            's15_19seuls': 40,
            's20_24seuls': 50,
            't1529total': 700,
            'part1524se': 60,
            'atlasnb': 400,
            'placetud': 500,
            'densitplac': 20,
            'evojeunes': 4.5,
            'T1T2': 50,
            'locataires': 80,
            'geom': 'MULTIPOLYGON (((0 0, 0 3, 3 3, 3 0, 0 0)))'
        }
        response = self.client.patch(url, updated_commune_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_commune(self):
        url = reverse('commune-detail', args=[self.commune.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Commune.objects.filter(id=self.commune.id).exists())

    def test_get_commune_list_filter(self):
        url = reverse('commune-list')
        response = self.client.get(url, {'nom': 'Test Commune'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data['features'][0]['properties']['nom'], 'Test Commune')

    def test_get_commune_list_search(self):
        url = reverse('commune-list')
        response = self.client.get(url, {'search': 'Test Commune'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data['features'][0]['properties']['nom'], 'Test Commune')

    def tearDown(self):
        self.commune.delete()
