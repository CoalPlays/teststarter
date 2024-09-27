import unittest
from unittest.mock import patch, mock_open, Mock

from services import TranslateService


class TranslateServiceTests(unittest.TestCase):

	@patch('services.LanguageConfiguration', return_value='mock-lang/de.json')
	@patch('services.TranslateService', return_value='mock-lang/de.json')
	@patch('builtins.open', new_callable=mock_open, read_data='file')
	@patch('json.load', return_value={'translateKey': 'translateValue'})
	def setUp(self, mock_json_load: Mock, mock_open: Mock, mock_load_language: Mock, mock_lang_config: Mock):
		self.translate_service = TranslateService(mock_lang_config)

	@patch('services.TranslateService.get_resource_path', return_value='mock-lang/de.json')
	@patch('builtins.open', new_callable=mock_open, read_data='file')
	@patch('json.load', return_value={'translateKey': 'translateValue'})
	def test_load_language(self, mock_json_load: Mock, mock_open: Mock, mock_get_resource_path: Mock):
		self.translate_service.load_language('de')

		mock_get_resource_path.assert_called_once_with('lang/de.json')
		mock_open.assert_called_once_with('mock-lang/de.json', 'r', encoding='utf-8')
		mock_json_load.assert_called_once_with(mock_open())

		self.assertIsInstance(self.translate_service.translations.get('de'), dict)

