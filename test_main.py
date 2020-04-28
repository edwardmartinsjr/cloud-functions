import unittest
from unittest.mock import patch
import main

patch_requests_get = 'requests.get'

# START TESTS
class Test(unittest.TestCase):

    def test_get_data_engineer_stories_without_args(self):
        data_engineer_stories = main.get_data_engineer_stories([])
        self.assertEqual(data_engineer_stories, [])

    def test_get_data_engineer_stories_404(self):
        with patch(patch_requests_get) as mock_request:
            url = main.item_url.format(1)

            # set a `status_code` attribute on the mock object
            # with value 404
            mock_request.return_value.status_code = 404

            self.assertEqual(main.get_data_engineer_stories([1]), [])

            # test if requests.get was called 
            # with the given url or not
            mock_request.assert_called_once_with(url)

    def test_get_data_engineer_stories_success(self):
        with patch(patch_requests_get) as mock_request:
            url = main.item_url.format(101)

            # set a `status_code` attribute on the mock object
            # with value 200
            mock_request.return_value.status_code = 200

            self.assertEqual(main.get_data_engineer_stories([101]), [])

            # test if requests.get was called 
            # with the given url or not
            mock_request.assert_called_once_with(url)

    def test_get_top_stories_without_args(self):
        with self.assertRaises(SystemExit): main.get_top_stories("")

    def test_get_top_stories_404(self):
        with patch(patch_requests_get) as mock_request:
            url = main.top_stories_url

            # set a `status_code` attribute on the mock object
            # with value 404
            mock_request.return_value.status_code = 404

            self.assertEqual(main.get_top_stories(url), [])

            # test if requests.get was called 
            # with the given url or not
            mock_request.assert_called_once_with(url)     

    def test_get_top_stories_success(self):
        with patch(patch_requests_get) as mock_request:
            url = main.top_stories_url

            # set a `status_code` attribute on the mock object
            # with value 200
            mock_request.return_value.status_code = 200

            self.assertNotEqual(main.get_top_stories(url), [])

            # test if requests.get was called 
            # with the given url or not
            mock_request.assert_called_once_with(url)



unittest.main()
        
